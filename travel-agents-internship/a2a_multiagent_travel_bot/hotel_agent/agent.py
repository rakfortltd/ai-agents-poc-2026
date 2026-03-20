from google.adk.agents.llm_agent import Agent
from dotenv import load_dotenv
import os

load_dotenv()

MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")

hotel_agent = Agent(
    name="hotel_agent",
    model=MODEL,
    description="Hotels specialist agent",
    instruction=(
        "You are a Hotels Specialist Agent. "
        "Suggest budget friendly hotel options and good locations."
    ),
)

root_agent = hotel_agent
