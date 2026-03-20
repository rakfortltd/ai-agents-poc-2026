from mcp.server.fastmcp import FastMCP

mcp = FastMCP("travel-tools") #name of tool group

@mcp.tool()
def get_weather(city: str, dates: str) -> str:
    """Get a simple weather summary (mocked). Args: city, dates (e.g. '2026-02-10 to 2026-02-14')"""
    return f"Weather in {city} for {dates}: Mostly sunny, 24-28°C. (mock)"

@mcp.tool()
def estimate_flight_cost(origin: str, destination: str) -> str:
    """Estimate flight cost (mocked)."""
    return f"Estimated return flight {origin} ↔ {destination}: €320-€480 (mock)"

@mcp.tool()
def suggest_hotels(city: str, budget_per_night_eur: int) -> str:
    """Suggest hotels (mocked)."""
    return (
        f"Hotel suggestions in {city} under €{budget_per_night_eur}/night (mock):\n"
        f"- Central Stay Inn (€{budget_per_night_eur - 10})\n"
        f"- Comfort Suites (€{budget_per_night_eur})\n"
        f"- Budget Rooms (€{max(40, budget_per_night_eur - 30)})"
    )

def main():
    mcp.run(transport="stdio")  # stdio transport = no port :contentReference[oaicite:11]{index=11}

if __name__ == "__main__":
    main()
