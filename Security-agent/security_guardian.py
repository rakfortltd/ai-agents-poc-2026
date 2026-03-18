# # security_guardian.py

# import re
# from agents import Agent, Runner
# from session_utils import get_session, add_history
# from llm_guard_scanners import LLMGuardScanners

# class SecurityGuardian:
#     def __init__(self):
#         self.agent = Agent(
#             name="SecurityAgent",
#             instructions="""..."""
#         )
#         self.llm_guard = LLMGuardScanners()

#     def static_filter(self, text):
#         if re.search(r'([A-Za-z0-9+/]{40,}={0,2})', text):
#             print("[DEBUG] SecurityAgent static filter hit (base64/blob).")
#             return "[BLOCKED] Suspiciously long encoded string detected."
#         controversial = re.search(
#             r"(india\s*(vs|versus)\s*pakistan).*(fight|attack|war|violence|riot|terror|hate|bloodshed)",
#             text.lower()
#         )
#         if controversial:
#             print("[DEBUG] SecurityAgent static filter hit (geopolitical).")
#             return "[BLOCKED] Sensitive geopolitical topic in controversial context."
#         return None

#     async def _run_with_history(self, user_id, message):
#         session = get_session(user_id)
#         hist = session.get("guardian_history", [])
#         session["guardian_history"] = hist
#         add_history(hist, "user", message)
#         prompt = "\n".join([m["content"] for m in hist])
#         print("[DEBUG] SecurityAgent triggered with prompt:")
#         print(prompt)
#         result = await Runner.run(self.agent, prompt)   # <-- Add this line
#         add_history(hist, "assistant", result.final_output)
#         return result.final_output


#     async def pre_check(self, user_id, prompt):
#         print("[DEBUG] SecurityAgent pre-check running.")
#         # 1. LLM-Guard input scan
#         llm_guard_result = self.llm_guard.scan_input(prompt)
#         if llm_guard_result:
#             return llm_guard_result
#         # 2. Your static filter
#         static = self.static_filter(prompt)
#         if static:
#             return static
#         # 3. Contextual agent
#         return await self._run_with_history(user_id, prompt)

#     async def post_check(self, user_id, output):
#         print("[DEBUG] SecurityAgent post-check running.")
#         # 1. LLM-Guard output scan
#         session = get_session(user_id)
#         hist = session.get("history", [])
#         prompt = "\n".join([m["content"] for m in hist if m["role"] == "user"])
#         llm_guard_result = self.llm_guard.scan_output(prompt, output)
#         if llm_guard_result:
#             return llm_guard_result
#         # 2. Your static filter
#         static = self.static_filter(output)
#         if static:
#             return static
#         # 3. Contextual agent
#         return await self._run_with_history(user_id, output)

#     async def log_delegation(self, user_id):
#         print("[DEBUG] SecurityAgent logging delegation.")
#         return await self._run_with_history(user_id, "Delegating to another agent")
