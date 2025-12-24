import os
from dotenv import load_dotenv

load_dotenv()


def mock_explain(topic: str) -> str:
    return (
        "[MOCK MODE]\n\n"
        f"{topic.capitalize()} is a concept where a function calls itself to solve a problem.\n\n"
        "It works by breaking a big problem into smaller subproblems of the same type.\n\n"
        "Key parts:\n"
        "• Base case – stops the recursion\n"
        "• Recursive case – function calls itself\n\n"
        "Example:\n"
        "factorial(n) = n × factorial(n-1)"
    )


def explain_topic(topic: str, use_mock: bool = False) -> str:
    if use_mock:
        return mock_explain(topic)

    try:
        from openai import OpenAI

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful engineering tutor."},
                {"role": "user", "content": f"Explain this topic simply: {topic}"}
            ],
            max_tokens=300
        )

        return response.choices[0].message.content

    except Exception:
        return mock_explain(topic)
