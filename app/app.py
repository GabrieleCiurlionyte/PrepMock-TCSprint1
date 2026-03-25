import streamlit as st
from components.DifficultySelector import render_difficulty_selector
from components.Header import render_header
from components.SideBar import render_openai_configuration_sidebar
config, openai_api_key = render_openai_configuration_sidebar()

from services.InterviewEvaluator.main import EvaluateIntervieweeResponse
from services.InterviewEvaluator.interviewEvaluatorService import InterviewEvaluatorConfig
from services.InterviewQuestionGenerator.InterviewQuestionGenerator import (
    InterviewQuestionGenerator,
)
from services.InterviewQuestionGenerator.questionBank import QUESTION_BANK

# Page configuration
st.set_page_config(
    page_title="PrepMock - Interview Prep Assistant",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="auto"
)

interviewConfig, openai_api_key = render_openai_configuration_sidebar()
print(interviewConfig)
print(openai_api_key)

render_header(
    title="PrepMock",
    subheader="AI interview practice for software engineers",
    description="Configure OpenAPI key. Select your level, answer technical interview questions, and receive structured feedback."
)


def format_evaluation_response(evaluation) -> str:
    lines = [f"Score: {evaluation.overall_score}" if evaluation.overall_score is not None else "Score: N/A"]

    if evaluation.message:
        lines.append(f"Message: {evaluation.message}")

    if evaluation.correct_answer:
        lines.append("Correct points:")
        lines.extend(f"- {item}" for item in evaluation.correct_answer)

    if evaluation.incorrect_answer:
        lines.append("Needs improvement:")
        lines.extend(f"- {item}" for item in evaluation.incorrect_answer)

    if evaluation.explanation:
        lines.append(f"Explanation: {evaluation.explanation}")

    return "\n".join(lines)

if "difficulty" not in st.session_state:
    st.session_state["difficulty"] = render_difficulty_selector()
    
if "generator" not in st.session_state:
    st.session_state["generator"] = InterviewQuestionGenerator(question_bank=QUESTION_BANK)
    
print(st.session_state["generator"])

if "current_question" not in st.session_state:
    st.session_state["current_question"] = None

if st.button("Start Interview"):
    st.session_state["current_question"] = st.session_state["generator"].provide_interview_question(
        difficulty=st.session_state["difficulty"]
    )

print(st.session_state["current_question"])

current_question = st.session_state["current_question"]

if current_question:
    st.markdown(f"### {current_question.question}")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if interviewee_answer := st.chat_input("What is up?"):
    with st.chat_message("user"):
        st.markdown(interviewee_answer)
    st.session_state.messages.append({"role": "user", "content": interviewee_answer})

    if not openai_api_key:
        st.error("OpenAI API key is required. Add OPENAI_API_KEY in .env or enter it in the sidebar.")
        st.stop()

    evaluation = EvaluateIntervieweeResponse(
        interviewEvaluatorConfig=InterviewEvaluatorConfig(),
        interview_question=(
            f"QUESTION: {st.session_state['current_question'].question}\n\n"
            f"ANSWER:\n{st.session_state['current_question'].answer}"
        ),
        interviewee_answer=interviewee_answer,
        openai_api_key=openai_api_key,
    )
    response = format_evaluation_response(evaluation)

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})


