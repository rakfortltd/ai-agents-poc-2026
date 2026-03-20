from google.adk.agents.llm_agent import Agent
from dotenv import load_dotenv
import os

load_dotenv()

MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")

flight_agent = Agent(
    name="flight_agent",
    model=MODEL,
    description="Flights specialist agent",
    instruction=(
        "You are a Flights Specialist Agent. "
        "Suggest realistic flight routes and approximate prices. "
        "Be concise."
    ),
)

root_agent = flight_agent
