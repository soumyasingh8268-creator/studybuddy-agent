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
