from fastapi import FastAPI
from google.genai import types
from google.adk.runners import InMemoryRunner
from agent import hotel_agent

app = FastAPI(title="Hotel Agent Server")

runner = InMemoryRunner(agent=hotel_agent)
runner.auto_create_session = True

@app.post("/run")
def run_agent(req: dict):

    text = req["task"]

    events = list(runner.run(
        user_id="user1",
        session_id="session1",
        new_message=types.UserContent(parts=[types.Part(text=text)])
    ))

    result = events[-1].content.parts[0].text

    return {"result": result}
