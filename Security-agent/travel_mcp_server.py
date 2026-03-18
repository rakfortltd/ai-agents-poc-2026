from mcp.server.fastmcp import FastMCP
import httpx
import json

mcp = FastMCP("Travel MCP")

@mcp.tool(name="Google Hotels")
def google_hotels(destination: str, budget: str) -> str:
    """Returns 2-3 hotel suggestions based on a given destination and budget."""
    # A mock implementation for the demonstration
    return f"""
    Here are the top hotel recommendations in {destination} for a {budget} budget:
    1. Grand Plaza {destination}
       - Price: {budget} (Approx $140/night)
       - Rating: 4.5/5
       - Area: Downtown Central
    2. Sea View Budget Inn
       - Price: {budget} (Approx $75/night)
       - Rating: 3.8/5
       - Area: South Beach District
    3. The Historic {destination} Hotel
       - Price: {budget} (Approx $200/night)
       - Rating: 4.8/5
       - Area: Old Town
    """

@mcp.tool()
def search_activities(destination: str, interests: str) -> str:
    """Returns 2-3 activity and attraction suggestions for a given destination and interests."""
    # A mock implementation for the demonstration
    return f"""
    Based on your interest in '{interests}' in {destination}, here are some great activities:
    1. {interests} City Tour
       - Description: An immersive 2-hour guided walking tour focusing on {interests}.
       - Price Estimate: $25
       - Duration: 2 Hours
    2. The National {destination} Museum
       - Description: Discover the rich history and beautiful {interests} exhibits.
       - Price Estimate: $15
       - Duration: 3-4 Hours
    3. Extreme {interests} Adventure
       - Description: Get your adrenaline pumping with our signature {destination} experience!
       - Price Estimate: $80
       - Duration: Half Day (4-5 hours)
    """

if __name__ == "__main__":
    mcp.run()
