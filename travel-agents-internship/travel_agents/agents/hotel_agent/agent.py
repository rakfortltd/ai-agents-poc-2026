import os
from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent
from skills.hotel_skill import HotelSearchTool


load_dotenv()
MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")

hotel_agent = Agent(
    name="hotel_agent",
    model=MODEL,
    description="Hotels specialist agent",
    instruction="Suggest budget-friendly hotels and good locations.",
    tools=[HotelSearchTool()]

)

root_agent = hotel_agent
