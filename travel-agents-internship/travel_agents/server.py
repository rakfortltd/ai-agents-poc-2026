from fastapi import FastAPI
from google.genai import types
from google.adk.runners import InMemoryRunner

from travel_agents.agents.flight_agent.agent import flight_agent
from travel_agents.agents.hotel_agent.agent import hotel_agent
from travel_agents.agents.planner_agent.agent import planner_agent
import os
import requests

SECURITY_URL = os.environ.get("SECURITY_URL")

app = FastAPI(title="ADK Multi-Agent Travel System")

flight_runner = InMemoryRunner(agent=flight_agent)
hotel_runner = InMemoryRunner(agent=hotel_agent)
planner_runner = InMemoryRunner(agent=planner_agent)

flight_runner.auto_create_session = True
hotel_runner.auto_create_session = True
planner_runner.auto_create_session = True


@app.post("/flight")
def run_flight(req: dict):
    events = list(flight_runner.run(
        user_id="user1",
        session_id="flight_session",
        new_message=types.UserContent(parts=[types.Part(text=req["task"])])
    ))
    return {"result": events[-1].content.parts[0].text}


@app.post("/hotel")
def run_hotel(req: dict):
    events = list(hotel_runner.run(
        user_id="user1",
        session_id="hotel_session",
        new_message=types.UserContent(parts=[types.Part(text=req["task"])])
    ))
    return {"result": events[-1].content.parts[0].text}


@app.post("/planner")
def run_planner(req: dict):

    user_input = req["task"]

    # CALL SECURITY AGENT OVER HTTP
    security_response = requests.post(
        f"{SECURITY_URL}/validate",
        json={"task": user_input}
    )

    if security_response.status_code != 200:
        return {"error": "Security service unavailable"}

    safe_input = security_response.json()["result"]

    # Flight
    flight_events = list(flight_runner.run(
        user_id="user1",
        session_id="flight_session",
        new_message=types.UserContent(
            parts=[types.Part(text=safe_input)]
        )
    ))

    flights = flight_events[-1].content.parts[0].text

    # Hotel
    hotel_events = list(hotel_runner.run(
        user_id="user1",
        session_id="hotel_session",
        new_message=types.UserContent(
            parts=[types.Part(text=safe_input)]
        )
    ))

    hotels = hotel_events[-1].content.parts[0].text

    final_prompt = f"""
User request:
{safe_input}

Flights:
{flights}

Hotels:
{hotels}
"""

    planner_events = list(planner_runner.run(
        user_id="user1",
        session_id="planner_session",
        new_message=types.UserContent(
            parts=[types.Part(text=final_prompt)]
        )
    ))

    return {"result": planner_events[-1].content.parts[0].text}


@app.get("/agent-card")
def agent_card():
    return {
        "name": "multi_agent_travel_system",
        "version": "1.0",
        "skills": [
            "flight_search",
            "hotel_search",
            "travel_planning",
            "prompt_validation"
        ]
    }