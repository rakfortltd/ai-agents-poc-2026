from google.adk.tools import Tool

class FlightSearchTool(Tool):

    def __init__(self):
        super().__init__(
            name="flight_search",
            description="Search and suggest flight routes with estimated prices"
        )

    async def run(self, input: str) -> str:
        # In real production this would call a flight API
        # Example mock response
        return (
            "Sample Flights:\n"
            "Dublin → Goa via Doha (Qatar Airways) - €720\n"
            "Dublin → Goa via Dubai (Emirates) - €760\n"
        )
