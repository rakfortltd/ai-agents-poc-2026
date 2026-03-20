import os
from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent
from skills.security_skill import security_validation_tool

load_dotenv()
MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")


security_agent = Agent(
    name="security_broker_agent",
    model=MODEL,
    description="Security Broker Agent for validating messages",
    instruction="Validate inter-agent messages and block malicious inputs.",
    tools=[security_validation_tool],  # REGISTERED SKILL
)

root_agent = security_agent
