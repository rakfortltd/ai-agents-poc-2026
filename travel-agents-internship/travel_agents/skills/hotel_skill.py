from google.adk.tools import Tool

class HotelSearchTool(Tool):

    def __init__(self):
        super().__init__(
            name="hotel_search",
            description="Suggest hotels based on location and budget"
        )

    async def run(self, input: str) -> str:
        # Mock implementation
        return (
            "Suggested Hotels:\n"
            "1. Bloom Suites, Calangute - €60/night\n"
            "2. Zostel Goa - €25/night (budget hostel)\n"
        )
