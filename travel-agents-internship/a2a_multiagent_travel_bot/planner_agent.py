import os
import requests
from dotenv import load_dotenv
from google.genai import types
from google.adk.runners import InMemoryRunner
from google.adk.agents.llm_agent import Agent

load_dotenv()

MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")

# Local agent URLs (A2A servers)
FLIGHT_AGENT_URL = "http://127.0.0.1:8001/run"
HOTEL_AGENT_URL  = "http://127.0.0.1:8002/run"

# Planner Agent
planner_agent = Agent(
    name="planner_agent",
    model=MODEL,
    description="Planner agent combining specialist outputs",
    instruction=(
        "You are the Planner Agent. "
        "Combine outputs into a full travel plan with sections:"
        " Trip Summary, Flights, Hotels, Budget Tips."
    ),
)

runner = InMemoryRunner(agent=planner_agent)
runner.auto_create_session = True


def call_agent(url, task):
    resp = requests.post(url, json={"task": task})
    resp.raise_for_status()
    return resp.json()["result"]


def main():

    print("\n" + "="*70)
    print("GOOGLE ADK REAL A2A TRAVEL BOT")
    print("="*70)

    user_request = input("Trip request: ").strip()

    print("\nCalling Flight Agent via A2A...")
    flights_text = call_agent(FLIGHT_AGENT_URL, user_request)

    print("Calling Hotel Agent via A2A...")
    hotels_text = call_agent(HOTEL_AGENT_URL, user_request)

    final_prompt = f"""
User request:
{user_request}

Flights Specialist output:
{flights_text}

Hotels Specialist output:
{hotels_text}

Create the final integrated travel plan.
"""

    events = list(runner.run(
        user_id="user1",
        session_id="session1",
        new_message=types.UserContent(parts=[types.Part(text=final_prompt)])
    ))

    final = events[-1].content.parts[0].text

    print("\n--- FINAL TRAVEL PLAN ---\n")
    print(final)


if __name__ == "__main__":
    main()
