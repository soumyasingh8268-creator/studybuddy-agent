import os
from dotenv import load_dotenv

load_dotenv()

MOCK_AI = os.getenv("MOCK_AI", "false").lower() == "true"

def mock_explain(topic: str) -> str:
    return (
        f"[MOCK MODE]\n\n"
        f"{topic.capitalize()} is a concept where a function calls itself to solve a problem.\n\n"
        f"It works by breaking a big problem into smaller subproblems of the same type.\n\n"
        f"Key parts:\n"
        f"• Base case – stops the recursion\n"
        f"• Recursive case – function calls itself\n\n"
        f"Example:\n"
        f"factorial(n) = n × factorial(n-1)"
    )

def explain_topic(topic: str) -> str:
    if MOCK_AI:
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
