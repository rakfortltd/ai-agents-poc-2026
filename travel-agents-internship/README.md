# AI Travel Agents Internship Project

Author: Shraddha Gawade  
Company: Rakfort Ltd  
Year: 2026


The project demonstrates the evolution from a simple AI agent to a distributed multi-agent architecture using Google ADK.

-----------------------------------------------------

PROJECT STRUCTURE

travel_agents_internship

1) single-agent-travel-bot  
2) mcp-travel-agent  
3) adk-multi-agent-travel-system

-----------------------------------------------------

1) SINGLE AGENT TRAVEL BOT

A simple AI agent built using Gemini (Vertex AI) that generates travel plans based on user input.

Features
- Single AI agent
- Uses Gemini model
- Generates travel suggestions

How to run

cd single-agent-travel-bot

Install dependencies

pip install -r requirements.txt

Run

python main.py

Example input

Plan a 3 day Goa trip with budget €500

-----------------------------------------------------

2) MCP TRAVEL AGENT

This implementation uses MCP (Model Context Protocol) tools.

The agent can call external tools to fetch travel related information.

Features
- AI agent + MCP tools
- Tool calling
- Modular architecture

Files
agent.py → main AI agent  
mcp_tools.py → external tool functions  
main.py → program entry point

How to run

cd mcp-travel-agent

Install dependencies

pip install -r requirements.txt

Run

python main.py

-----------------------------------------------------

3) ADK MULTI AGENT TRAVEL SYSTEM

This is a distributed multi-agent system built using Google ADK.

Agents communicate with each other and perform specialized tasks.

Agents included

Planner Agent  
Coordinates all other agents

Flight Agent  
Suggests flights

Hotel Agent  
Suggests accommodation

Security Broker Agent  
Validates prompts using LLM Guard to prevent malicious input.

Architecture

User
 ↓
Planner Agent
 ↓
Security Broker Agent
 ↓
Flight Agent
 ↓
Hotel Agent

Skills

Flight Skill
Search flights

Hotel Skill
Search hotels

Security Skill
Validate prompts using LLM Guard

-----------------------------------------------------

Running the Multi Agent System

cd adk-multi-agent-travel-system

Install dependencies

pip install -r requirements.txt

Run locally

python main.py

-----------------------------------------------------

Cloud Deployment

Agents can be deployed using Docker and Google Cloud Run.

Security Agent runs as an independent service.

Example deployment

gcloud builds submit --tag IMAGE_URL

gcloud run deploy SERVICE_NAME --image IMAGE_URL

-----------------------------------------------------

Technologies Used

Python  
Google ADK  
Vertex AI Gemini  
FastAPI  
Docker  
Google Cloud Run  
LLM Guard  

