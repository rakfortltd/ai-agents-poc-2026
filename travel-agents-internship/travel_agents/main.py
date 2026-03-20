import os
from dotenv import load_dotenv

from google.genai import types
from google.adk.runners import InMemoryRunner

from travel_agents.agents.flight_agent.agent import flight_agent
from travel_agents.agents.hotel_agent.agent import hotel_agent
from travel_agents.agents.planner_agent.agent import planner_agent
from travel_agents.agents.security_agent.agent import security_agent


load_dotenv()


def run_agent(agent, user_id, session_id, message_text):
    """
    Helper function to execute any ADK agent safely.
    """
    runner = InMemoryRunner(agent=agent)
    runner.auto_create_session = True

    events = list(runner.run(
        user_id=user_id,
        session_id=session_id,
        new_message=types.UserContent(
            parts=[types.Part(text=message_text)]
        )
    ))

    if not events:
        raise Exception("No response from agent")

    return events[-1].content.parts[0].text


def main():
    print("=" * 60)
    print("ADK Secure Multi-Agent Travel Bot")
    print("=" * 60)

    user_input = input("Trip request: ").strip()

    if not user_input:
        print("No input provided.")
        return

    try:
        # SECURITY BROKER LAYER 
        print("\nRunning Security Broker Agent")

        safe_input = run_agent(
            agent=security_agent,
            user_id="user1",
            session_id="security_session",
            message_text=user_input
        )

        # If security agent blocks
        if "BLOCKED" in safe_input.upper():
            print("\nRequest blocked by Security Broker Agent")
            print(safe_input)
            return
        print("Input validated successfully.\n")

        # FLIGHT AGENT
        print("Calling Flight Agent")

        flights = run_agent(
            agent=flight_agent,
            user_id="user1",
            session_id="flight_session",
            message_text=safe_input
        )

        # HOTEL AGENT
        print("Calling Hotel Agent")

        hotels = run_agent(
            agent=hotel_agent,
            user_id="user1",
            session_id="hotel_session",
            message_text=safe_input
        )

        # PLANNER AGENT (ORCHESTRATOR)
        print("Generating Final Travel Plan...")

        final_prompt = f"""
User request:
{safe_input}

Flights Specialist Output:
{flights}

Hotels Specialist Output:
{hotels}

Create a complete structured travel plan with:
- Trip Summary
- Flights
- Hotels
- Budget Tips
"""

        final_plan = run_agent(
            agent=planner_agent,
            user_id="user1",
            session_id="planner_session",
            message_text=final_prompt
        )

        # FINAL OUTPUT
        print("\n" + "=" * 60)
        print("FINAL TRAVEL PLAN")
        print("=" * 60)
        print(final_plan)

    except Exception as e:
        print("\nError occurred:")
        print(str(e))


if __name__ == "__main__":
    main()
