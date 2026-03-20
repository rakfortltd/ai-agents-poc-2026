from langchain_google_vertexai import ChatVertexAI #langchain wrapper
from common.config import PROJECT, LOCATION, MODEL

def get_llm(temperature: float = 0.2) -> ChatVertexAI: #used by all agents 
    # ChatVertexAI is LangChain’s wrapper for Vertex AI chat models
    return ChatVertexAI(
        project=PROJECT,
        location=LOCATION,
        model=MODEL,
        temperature=temperature,
    )
