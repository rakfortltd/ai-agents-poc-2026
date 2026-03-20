import os
import chainlit as cl
import vertexai
from vertexai import agent_engines
from google.adk.agents.llm_agent import LlmAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part
from dotenv import load_dotenv
import uuid

load_dotenv()

# Initialise Vertex AI
vertexai.init(
    project=os.environ.get("GOOGLE_CLOUD_PROJECT"),
    location=os.environ.get("GOOGLE_CLOUD_LOCATION")
)

# Connect to deployed planner agent on Agent Engine
AGENT_RESOURCE_NAME = "projects/247920035196/locations/us-central1/reasoningEngines/5475681156022140928"
planner = agent_engines.get(AGENT_RESOURCE_NAME)

# Test Agent
MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
session_service = InMemorySessionService()

test_agent = LlmAgent(
    name="test_agent",
    model=MODEL,
    description="Test agent that formats and validates user travel requests before sending to planner.",
    instruction=(
        "You are a Travel Request Formatter. Your job is to: "
        "1. Take the user's raw travel request "
        "2. Format it clearly with all necessary details "
        "3. Make sure it includes: destination, dates, number of travellers, and budget if mentioned "
        "4. If any details are missing, add placeholder text like 'dates TBD' "
        "5. Return ONLY the formatted request, nothing else "
        "Example input: 'I want to go to Goa' "
        "Example output: 'Plan a trip to Goa for 2 adults. Dates TBD. Budget flexible.' "
    ),
)

async def run_test_agent(user_message: str) -> str:
    """Run test agent to format the user request."""
    session_id = str(uuid.uuid4())
    user_id = "test_agent_user"

    runner = Runner(
        agent=test_agent,
        app_name="test_agent_app",
        session_service=session_service,
    )

    session_service.create_session(
        app_name="test_agent_app",
        user_id=user_id,
        session_id=session_id,
    )

    message = Content(role="user", parts=[Part(text=user_message)])
    formatted = ""

    async for event in runner.run_async(
        user_id=user_id,
        session_id=session_id,
        new_message=message,
    ):
        if hasattr(event, "content") and event.content:
            for part in event.content.parts:
                if hasattr(part, "text") and part.text:
                    formatted += part.text

    return formatted if formatted else user_message


@cl.on_chat_start
async def on_chat_start():
    """Called when a new chat session starts."""
    # Create a new session for this user
    session = planner.create_session(user_id="chainlit_user")
    cl.user_session.set("session_id", session["id"])

    # Initialise empty conversation history
    cl.user_session.set("history", [])

    await cl.Message(
        content=(
            "👋 Welcome to the **Travel Planner Agent**!\n\n"
            "I can help you plan your perfect trip including:\n"
            "✈️ Flights\n"
            "🏨 Hotels\n"
            "💰 Budget estimates\n\n"
            "Just tell me where you want to go!\n\n"
            "💡 *I remember everything you tell me during our conversation.*"
        )
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    """Called when user sends a message."""
    session_id = cl.user_session.get("session_id")
    history = cl.user_session.get("history", [])

    response_text = ""

    try:
        # Step 1: Build message with conversation history context
        if history:
            # Include history so test agent understands context
            history_text = "\n".join([
                f"{'User' if h['role'] == 'user' else 'Assistant'}: {h['content']}"
                for h in history[-6:]  # Last 6 messages for context
            ])
            full_message = (
                f"Previous conversation:\n{history_text}\n\n"
                f"New message: {message.content}"
            )
        else:
            full_message = message.content

        # Step 2: Test agent formats the request
        async with cl.Step(name="🔍 Test Agent formatting request..."):
            formatted_request = await run_test_agent(full_message)

        # Step 3: Send formatted request to planner on Agent Engine
        async with cl.Step(name="✈️ Planner Agent working..."):
            response = planner.stream_query(
                user_id="chainlit_user",
                session_id=session_id,
                message=formatted_request
            )

            for event in response:
                if "content" in event and "parts" in event["content"]:
                    for part in event["content"]["parts"]:
                        if "text" in part:
                            response_text += part["text"]

        # Step 4: Update conversation history
        history.append({"role": "user", "content": message.content})
        history.append({"role": "assistant", "content": response_text})
        cl.user_session.set("history", history)

    except Exception as e:
        response_text = f"❌ Error: {str(e)}"

    await cl.Message(content=response_text).send()