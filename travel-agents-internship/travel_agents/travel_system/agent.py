from google.adk.agents import SequentialAgent

from travel_agents.agents.flight_agent.agent import flight_agent
from travel_agents.agents.hotel_agent.agent import hotel_agent
from travel_agents.agents.planner_agent.agent import planner_agent


travel_system = SequentialAgent(
    name="travel_system",
    agents=[
        flight_agent,
        hotel_agent,
        planner_agent
    ]
)

root_agent = travel_system