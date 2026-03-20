from langchain_core.prompts import ChatPromptTemplate #structured prompt
from langchain_core.output_parsers import StrOutputParser #convert LLM to plain string

from common.vertex_llm import get_llm #helper function creates gemini LLM
from common.prompts import TRAVEL_SYSTEM #system prompt
from common.io import ask, banner

def main(): #start
    banner("01) Single Agent Travel Bot")

    user_request = ask("Describe your trip request (e.g., '3 days Goa under €500'): ") #take user input

    llm = get_llm(temperature=0.3) #initializing gemini via vertex AI

    prompt = ChatPromptTemplate.from_messages([
        ("system", TRAVEL_SYSTEM),
        ("user", "{request}")
    ]) #combination of system message and user message 

    chain = prompt | llm | StrOutputParser() # langchain pipeline
    result = chain.invoke({"request": user_request}) #send input to Vertex AI gemini

    print("\n--- RESPONSE ---\n")
    print(result)

if __name__ == "__main__":
    main()


#python -m single_agent_travel_bot.run
