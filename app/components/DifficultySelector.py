import streamlit as st
from services.InterviewQuestionGenerator.interviewQuestion import Difficulty

def render_difficulty_selector(key: str = "difficulty") -> Difficulty:
    if key not in st.session_state:
        st.session_state[key] = Difficulty.EASY

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Easy", key=f"{key}_easy", use_container_width=True):
            st.session_state[key] = Difficulty.EASY

    with col2:
        if st.button("Medium", key=f"{key}_medium", use_container_width=True):
            st.session_state[key] = Difficulty.MEDIUM

    with col3:
        if st.button("Hard", key=f"{key}_hard", use_container_width=True):
            st.session_state[key] = Difficulty.HARD

    return st.session_state[key]
