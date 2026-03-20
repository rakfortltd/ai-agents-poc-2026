import os
import vertexai
from dotenv import load_dotenv
from vertexai import agent_engines
from agents.planner_agent import planner_agent

load_dotenv()

PROJECT = os.environ.get("GOOGLE_CLOUD_PROJECT")
LOCATION = os.environ.get("GOOGLE_CLOUD_LOCATION")
STAGING_BUCKET = f"gs://{PROJECT}-agent-engine"

def deploy():
    print(f"Initialising Vertex AI...")
    print(f"Project: {PROJECT}")
    print(f"Location: {LOCATION}")
    print(f"Staging bucket: {STAGING_BUCKET}")

    vertexai.init(
        project=PROJECT,
        location=LOCATION,
        staging_bucket=STAGING_BUCKET,
    )

    print("Deploying planner agent to Agent Engine...")
    remote_agent = agent_engines.create(
        planner_agent,
        requirements=[
            "google-adk==0.5.0",
            "google-cloud-aiplatform[agent_engines,adk]==1.93.0",
            "google-genai==1.16.0",
            "cloudpickle==3.1.1",
            "deprecated==1.2.14",
            "pydantic==2.11.1",
        ],
        extra_packages=[
            "./agents",
            "./skills",
        ],
        display_name="Travel Planner Agent",
        description="Multi-agent travel planner with flight, hotel and security agents.",
    )

    print("=" * 60)
    print("Agent deployed successfully!")
    print(f"Resource name: {remote_agent.resource_name}")
    print("=" * 60)
    print("Save this resource name — you need it to call the agent!")

if __name__ == "__main__":
    deploy()