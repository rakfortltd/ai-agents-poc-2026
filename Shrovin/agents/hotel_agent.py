import os
from dotenv import load_dotenv
from google.adk.agents.llm_agent import LlmAgent
from skills.hotel_skill import hotel_search

load_dotenv()

MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")

hotel_agent = LlmAgent(
    name="hotel_agent",
    model=MODEL,
    description="Hotels specialist. Suggests hotels based on location and budget.",
    instruction=(
        "You are a hotel search specialist. "
        "When asked about accommodation, use the hotel_search tool to find options. "
        "Always present results clearly with hotel name, location, and price per night."
    ),
    tools=[hotel_search],
)