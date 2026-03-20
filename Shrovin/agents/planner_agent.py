import os
from dotenv import load_dotenv
from google.adk.agents.llm_agent import LlmAgent
from agents.flight_agent import flight_agent
from agents.hotel_agent import hotel_agent

load_dotenv()

MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")

planner_agent = LlmAgent(
    name="planner_agent",
    model=MODEL,
    description="Travel Planner Agent. Coordinates flights and hotels to create full travel plans.",
    instruction=(
        "You are a Travel Planner Agent. Your job is to create complete, detailed travel plans. "
        "When a user asks for a travel plan: "
        "1. Use the flight_agent to find suitable flights. "
        "2. Use the hotel_agent to find suitable hotels. "
        "3. Combine both results into a clear, structured travel plan with a budget summary. "
        "Always be helpful, friendly, and present information in a clear format."
    ),
    sub_agents=[flight_agent, hotel_agent],
)