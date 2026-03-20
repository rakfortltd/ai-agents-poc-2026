from fastapi import FastAPI
from travel_agents.agents.security_agent.agent import security_agent
from google.adk.runners import InMemoryRunner
from google.genai import types

app = FastAPI(title="Security Agent")

runner = InMemoryRunner(agent=security_agent)
runner.auto_create_session = True

@app.post("/validate")
def validate(req: dict):
    events = list(runner.run(
        user_id="user1",
        session_id="security_session",
        new_message=types.UserContent(
            parts=[types.Part(text=req["task"])]
        )
    ))
    return {"result": events[-1].content.parts[0].text}