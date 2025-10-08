# backend_model.py
"""
Backend processing logic for BU Guide chatbot.
This will receive a string message from the frontend UI (chat_window.py)
and return a processed string as the bot's reply.
"""

def process_user_input(user_message: str) -> str:
    """
    This function name MUST match the one expected by chat_window.py.
    - user_message: str - The message typed by the user.
    - return: str - The reply to send back to the UI.
    """
    # ✅ TEST IMPLEMENTATION (for connection check)
    return f"✅ Message fetched: {user_message}"
