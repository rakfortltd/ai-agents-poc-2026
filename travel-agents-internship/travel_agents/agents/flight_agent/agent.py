import os
from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent
from skills.flight_skill import FlightSearchTool



load_dotenv()
MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")

flight_agent = Agent(
    name="flight_agent",
    model=MODEL,
    description="Flights specialist agent",
    instruction=(
        "Provide realistic flight routes and price estimates."
    ),
    tools=[FlightSearchTool()]   # REGISTERED TOOL

)

root_agent = flight_agent
