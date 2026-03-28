import streamlit as st

from services.InterviewEvaluator.InterviewEvaluatorConfig import InterviewEvaluatorConfig
from services.InterviewQuestionGenerator.InterviewQuestionGenerator import (
    InterviewQuestionGenerator,
)
from services.InterviewQuestionGenerator.interviewQuestion import Difficulty
from services.InterviewQuestionGenerator.questionBank import QUESTION_BANK


def _reset_inactive_interview_state() -> None:
    """Keep the landing state clean when no interview is in progress."""
    st.session_state["generator"].reset_session()
    st.session_state["current_question"] = None
    st.session_state["messages"] = []


def init_session_state() -> None:
    if "difficulty" not in st.session_state:
        st.session_state["difficulty"] = Difficulty.EASY

    if "generator" not in st.session_state:
        st.session_state["generator"] = InterviewQuestionGenerator(question_bank=QUESTION_BANK)

    if "current_question" not in st.session_state:
        st.session_state["current_question"] = None

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    if "interview_active" not in st.session_state:
        st.session_state["interview_active"] = False

    if "interview_evaluator_config" not in st.session_state:
        st.session_state["interview_evaluator_config"] = InterviewEvaluatorConfig()

    if not st.session_state["interview_active"]:
        _reset_inactive_interview_state()
