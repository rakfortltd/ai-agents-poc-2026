# llm_guard_scanners.py
from llm_guard.input_scanners import PromptInjection, Secrets, Toxicity
from llm_guard.output_scanners import Sensitive, Relevance, Toxicity as OutputToxicity

class LLMGuardScanners:
    def __init__(self):
        # Initialize input scanners
        self.input_scanners = [
            PromptInjection(),
            Secrets(),
            Toxicity()
        ]
        # Initialize output scanners
        self.output_scanners = [
            Sensitive(),
            Relevance(),
            OutputToxicity()
        ]

    def scan_input(self, prompt: str):
        """Scan input using all configured input scanners."""
        for scanner in self.input_scanners:
            sanitized, is_valid, risk_score = scanner.scan(prompt)
            print(f"[DEBUG] LLM-Guard Input Scanner: {scanner.__class__.__name__}, valid={is_valid}, risk_score={risk_score}")
            if not is_valid:
                return f"[BLOCKED] LLM-Guard Input: {scanner.__class__.__name__} flagged this input. Risk score: {risk_score}"
        return None

    def scan_output(self, prompt: str, output: str):
        """Scan output using all configured output scanners."""
        for scanner in self.output_scanners:
            sanitized, is_valid, risk_score = scanner.scan(prompt, output)
            print(f"[DEBUG] LLM-Guard Output Scanner: {scanner.__class__.__name__}, valid={is_valid}, risk_score={risk_score}")
            if not is_valid:
                return f"[BLOCKED] LLM-Guard Output: {scanner.__class__.__name__} flagged this output. Risk score: {risk_score}"
        return None
