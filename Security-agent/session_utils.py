# session_utils.py
_sessions = {}
def get_session(user_id):
    if user_id not in _sessions:
        _sessions[user_id] = {"history": []}
    return _sessions[user_id]
def add_history(hist, role, content):
    hist.append({"role": role, "content": content})
    if len(hist) > 10:
        hist.pop(0)
