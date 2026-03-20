from llm_guard.input_scanners import PromptInjection

scanner = PromptInjection()

def security_validation_tool(prompt: str) -> str:
    """
    Validates prompt against injection attacks.
    Raises error if malicious.
    """
    sanitized_prompt, is_valid, risk_score = scanner.scan(prompt)

    if not is_valid:
        raise ValueError("Blocked by Security Broker - Prompt Injection detected")

    return sanitized_prompt
