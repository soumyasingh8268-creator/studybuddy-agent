from fastapi import FastAPI
from agents.explanation_agent import explain_topic
from agents.planner_agent import plan_action
from agents.question_agent import ask_question

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "StudyBuddy backend running"}

@app.get("/chat")
def chat(user_input: str):
    action = plan_action(user_input)

    if action == "explain":
        response = explain_topic(user_input)
    elif action == "solve":
        response = "Step-by-step solving coming next phase 🛠️"
    else:
        response = ask_question(user_input)

    return {
        "input": user_input,
        "action": action,
        "response": response
    }
