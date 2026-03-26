import streamlit as st

from services.InterviewEvaluator.InterviewEvaluatorConfig import InterviewEvaluatorConfig
from services.InterviewQuestionGenerator.InterviewQuestionGenerator import (
    InterviewQuestionGenerator,
)
from services.InterviewQuestionGenerator.interviewQuestion import Difficulty
from services.InterviewQuestionGenerator.questionBank import QUESTION_BANK


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
