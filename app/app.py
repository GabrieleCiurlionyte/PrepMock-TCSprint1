import streamlit as st

from components.actions.interview_state import (
    advance_to_next_question,
    is_interview_active,
    can_submit_answer,
    end_interview,
    repeat_same_question,
    start_interview,
)
from components.DifficultySelector import render_difficulty_selector
from components.Header import render_header
from components.SideBar import render_openai_configuration_sidebar
from services.InterviewEvaluator.main import EvaluateIntervieweeResponse
from services.InterviewEvaluator.promptGuardModule import validate_interview_answer
from state import init_session_state
from utils.evaluation_formatter import format_evaluation_response

# Page configuration
st.set_page_config(
    page_title="PrepMock - Interview Prep Assistant",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="auto",
)

init_session_state()
interview_config, openai_api_key = render_openai_configuration_sidebar()

render_header(
    title="PrepMock",
    subheader="AI interview practice for software engineers",
    description="Configure OpenAI key. Select your level, answer technical interview questions, and receive structured feedback.",
)

render_difficulty_selector()
st.markdown(f"Current difficulty: **{st.session_state['difficulty'].name.title()}**")

col1, col2 = st.columns(2)
with col1:
    st.button("Start Interview", 
              key="start_interview", 
              on_click=start_interview, 
              use_container_width=True,
              disabled=not is_interview_active())
with col2:
    st.button("End Interview",
              key="end_interview",
              on_click=end_interview, 
              use_container_width=True,
              disabled=is_interview_active())

for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if st.session_state["interview_complete"]:
    st.info("No more questions are available for this difficulty. Start a new interview to continue.")

if interviewee_answer := st.chat_input(
    (
        "No more questions are available for this difficulty."
        if st.session_state["interview_complete"]
        else "What is your answer to the interview question?"
    ),
    disabled=not can_submit_answer(),
):
    guard_result = validate_interview_answer(interviewee_answer)
    sanitized_answer = guard_result.sanitized_answer

    with st.chat_message("user"):
        st.markdown(sanitized_answer)
    st.session_state["messages"].append({"role": "user", "content": sanitized_answer})

    if not st.session_state["current_question"]:
        st.error("Start an interview first so there is a question to evaluate.")
        st.stop()

    if not openai_api_key:
        st.error("OpenAI API key is required. Add OPENAI_API_KEY in .env or enter it in the sidebar.")
        st.stop()

    if not guard_result.allowed:
        with st.chat_message("assistant"):
            st.markdown(guard_result.reason)

        st.session_state["messages"].append(
            {"role": "assistant", "content": guard_result.reason}
        )
        st.stop()

    evaluation = EvaluateIntervieweeResponse(
        interviewEvaluatorConfig=interview_config,
        interview_question=(
            f"QUESTION: {st.session_state['current_question'].question}\n\n"
            f"ANSWER:\n{st.session_state['current_question'].answer}"
        ),
        interviewee_answer=sanitized_answer,
        openai_api_key=openai_api_key,
    )
    response = format_evaluation_response(evaluation)
    
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state["messages"].append({"role": "assistant", "content": response})
    
    if evaluation.off_topic:
        repeat_same_question()
    else:
        advance_to_next_question()

    st.rerun()
