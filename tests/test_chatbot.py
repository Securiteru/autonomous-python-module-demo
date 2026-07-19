from demo_app.chatbot import respond

def test_hello():
    assert respond("hello") == "Hello! How can I help?"

def test_fallback():
    assert respond("bye") == "I am here to help."
