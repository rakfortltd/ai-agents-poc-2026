import os
import chainlit as cl
import vertexai
from vertexai import agent_engines
from dotenv import load_dotenv

load_dotenv()

# Initialise Vertex AI
vertexai.init(
    project=os.environ.get("GOOGLE_CLOUD_PROJECT"),
    location=os.environ.get("GOOGLE_CLOUD_LOCATION")
)

# Connect to deployed planner agent on Agent Engine
AGENT_RESOURCE_NAME = "projects/247920035196/locations/us-central1/reasoningEngines/5475681156022140928"
agent = agent_engines.get(AGENT_RESOURCE_NAME)

@cl.on_chat_start
async def on_chat_start():
    """Called when a new chat session starts."""
    # Create a new session for this user
    session = agent.create_session(user_id="chainlit_user")
    cl.user_session.set("session_id", session["id"])
    
    await cl.Message(
        content=(
            "👋 Welcome to the **Travel Planner Agent**!\n\n"
            "I can help you plan your perfect trip including:\n"
            "✈️ Flights\n"
            "🏨 Hotels\n"
            "💰 Budget estimates\n\n"
            "Just tell me where you want to go!"
        )
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    """Called when user sends a message."""
    session_id = cl.user_session.get("session_id")
    
    # Show thinking indicator
    async with cl.Step(name="Travel Planner Agent is thinking..."):
        
        # Send message to planner agent on Agent Engine
        response_text = ""
        try:
            response = agent.stream_query(
                user_id="chainlit_user",
                session_id=session_id,
                message=message.content
            )
            
            # Collect streaming response
            for event in response:
                if "content" in event and "parts" in event["content"]:
                    for part in event["content"]["parts"]:
                        if "text" in part:
                            response_text += part["text"]
        
        except Exception as e:
            response_text = f"❌ Error: {str(e)}"
    
    # Send response back to user
    await cl.Message(content=response_text).send()