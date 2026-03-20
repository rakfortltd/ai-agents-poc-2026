import os
import asyncio
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from common.vertex_llm import get_llm
from common.prompts import TRAVEL_SYSTEM
from common.io import ask, banner

from langchain_mcp_adapters.client import MultiServerMCPClient #create bridge between langchain and MCP
 
async def main(): # MCP asynchronous
    banner("02) Travel Bot + MCP Tools")

    user_request = ask("Trip request: ")

    # 1) Start MCP server and discover tools
    server_path = os.path.join(os.path.dirname(__file__), "mcp_server_travel_tools.py")
    client = MultiServerMCPClient(
        {
            "travel-tools": {
                "command": "python",
                "args": [server_path],
                "transport": "stdio", #communication through standard io
            }
        }
    )

    tools = await client.get_tools()  # tool definitions from MCP server

    # 2) Build an agent that can call these tools
    llm = get_llm(temperature=0.2) #initializing gemini via vertex AI

    prompt = ChatPromptTemplate.from_messages([
        ("system", TRAVEL_SYSTEM + "\nYou may use tools when useful."),
        ("user", "{request}")
    ])

    response = llm.invoke(
    prompt.format_messages(request=user_request)
    )
    print("\n--- RESPONSE ---\n")
    print(response.content)



if __name__ == "__main__":
    asyncio.run(main())


#python -m mcp_travel_bot.run
