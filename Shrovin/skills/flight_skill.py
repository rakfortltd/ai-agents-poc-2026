def flight_search(input: str) -> str:
    """
    Search and suggest flight routes with estimated prices.
    Args:
        input: The flight search query
    Returns:
        A string with flight options and price estimates.
    """
    return (
        "Sample Flights:\n"
        "Dublin → Goa via Doha (Qatar Airways) - €720\n"
        "Dublin → Goa via Dubai (Emirates) - €760\n"
        "Dublin → Goa via London (British Airways + IndiGo) - €680\n"
    )