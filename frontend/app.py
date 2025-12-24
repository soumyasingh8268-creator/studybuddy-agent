import streamlit as st
import requests

st.set_page_config(page_title="StudyBuddy Agent", page_icon="📘")
st.title("📘 StudyBuddy Agent")
st.caption("Agent-based study assistant (planner + tools)")

BACKEND_URL = "https://studybuddy-backend-cysc.onrender.com/chat"


if "history" not in st.session_state:
    st.session_state.history = []
mode = st.radio(
    "AI Mode",
    ["Mock", "Live"],
    horizontal=True
)


user_input = st.text_input("Ask something (e.g., 'explain recursion')")

if st.button("Send") and user_input.strip():
    with st.spinner("Thinking..."):
        try:
            resp = requests.get(
                BACKEND_URL,
                params={
                    "user_input": user_input,
                    "mode": mode.lower()
                },
                timeout=10
            )
            data = resp.json()
        except Exception:
            data = {
                "action": "error",
                "response": "Backend not reachable. Is it running?"
            }

    st.session_state.history.append({
        "user": user_input,
        "action": data.get("action"),
        "response": data.get("response")
    })

# Display chat history
for item in st.session_state.history[::-1]:
    st.markdown(f"**You:** {item['user']}")
    st.markdown(f"**Agent ({item['action']}):** {item['response']}")
    st.markdown("---")
