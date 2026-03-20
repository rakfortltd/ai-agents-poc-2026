import os
from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent
from skills.security_skill import security_validation_tool

load_dotenv()
MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")

planner_agent = Agent(
    name="planner_agent",
    model=MODEL,
    description="Travel Planner Agent",
    instruction=(
        "You are a Travel Planner Agent. "
        "Create detailed travel plans including flights, hotels, and budget tips. "
        "Be helpful and structured."
    ),
)


root_agent = planner_agent
