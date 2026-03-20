import os
from dotenv import load_dotenv
from google.adk.agents.llm_agent import LlmAgent
from skills.flight_skill import flight_search

load_dotenv()

MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")

flight_agent = LlmAgent(
    name="flight_agent",
    model=MODEL,
    description="Flights specialist. Searches and suggests flight routes with price estimates.",
    instruction=(
        "You are a flight search specialist. "
        "When asked about flights, use the flight_search tool to find options. "
        "Always present results clearly with airline, route, and price."
    ),
    tools=[flight_search],
)
