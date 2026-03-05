StudyBuddy 

StudyBuddy is a small project I built to explore how **AI agents can help students learn better**. Instead of a single AI doing everything, the system uses **multiple specialized agents** that each handle a specific task like explaining topics, generating questions, or planning a study path.

The goal was to experiment with **agent-based architecture** while building something practical for students.

---

## What StudyBuddy Can Do

* Explain difficult topics in simple language
* Generate practice questions for revision
* Switch between **mock responses** and **live AI responses**

This makes it easy to test the system without always calling an external AI API.

---

## How It Works

The project has two main parts:

**Frontend**

* Built using **Streamlit**
* Provides a simple interface where users can enter a topic or concept

**Backend**

* Handles requests from the frontend
* Routes them to the appropriate AI agent

Each agent focuses on a specific task:

* **Planner Agent** → Decides which agent should handle the request
* **Explanation Agent** → Explains concepts
* **Question Agent** → Generates practice questions for revision

---

## Project Structure

```id="4caz29"
studybuddy-agent
│
├── backend
│   ├── agents
│   │   ├── explanation_agent.py
│   │   ├── planner_agent.py
│   │   └── question_agent.py
│   │
│   ├── api.py
│   ├── main.py
│   └── requirements.txt
│
├── frontend
│   ├── app.py
│   └── requirements.txt
│
└── README.md
```

---

## Tech Stack

FastAPI backend for API services
Streamlit frontend for interaction
Modular multi-agent architecture
Optional OpenAI API integration

---

## Running the Project

Clone the repository

```bash id="7q7y8d"
git clone https://github.com/your-username/studybuddy-agent.git
cd studybuddy-agent
```

### Backend

```bash id="ypryjo"
cd backend
pip install -r requirements.txt
python main.py
```

### Frontend

```bash id="h4nq7d"
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

---

## Why I Built This

I wanted to experiment with **AI agents and modular system design**, while building something useful for learning. The idea was to separate different study tasks into independent agents instead of relying on a single monolithic system.

---

## Possible Improvements

* Add quiz scoring
* Track learning progress
* Add more agents (summarization, flashcards, etc.)
* Improve UI

---

## Author

Soumya Singh
Computer Science Engineering Student
