from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain_topic(topic: str) -> str:
    try:
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
        return "⚠️ AI service unavailable or quota exhausted. Please try later."
