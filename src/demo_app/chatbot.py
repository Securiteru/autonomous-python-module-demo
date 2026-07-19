def respond(message: str) -> str:
    return "Hello! How can I help?" if message.strip().lower() == "hello" else "I am here to help."
