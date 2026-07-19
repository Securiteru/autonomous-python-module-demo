from demo_app.greetings import greeting


def test_greeting_uses_project_format() -> None:
    assert greeting("Ada") == "Hello, Ada!"
