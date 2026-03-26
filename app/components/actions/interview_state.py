import streamlit as st

def _append_question_message(render_immediately: bool = False) -> None:
    question = st.session_state["current_question"]
    content: str
    should_rerun = False

    if question is None:
        content = "No questions available for this difficulty. Select different difficulty."
        st.session_state["interview_active"] = False
        should_rerun = True
    else:
        content = (
            f"**Interview Question #{st.session_state['generator'].asked_count}**\n"
            f"{question.question}"
        )

    st.session_state["messages"].append({"role": "assistant", "content": content})

    if render_immediately:
        with st.chat_message("assistant"):
            st.markdown(content)

    if should_rerun:
        st.rerun()


def start_interview() -> None:
    st.session_state["generator"].reset_session()
    st.session_state["messages"] = []
    st.session_state["interview_active"] = True

    q = st.session_state["generator"].provide_interview_question(
        difficulty=st.session_state["difficulty"]
    )
    st.session_state["current_question"] = q
    _append_question_message(render_immediately=False)


def advance_to_next_question() -> None:
    q = st.session_state["generator"].provide_interview_question(
        difficulty=st.session_state["difficulty"]
    )
    st.session_state["current_question"] = q
    _append_question_message(render_immediately=True)


def end_interview() -> None:
    st.session_state["interview_active"] = False
    st.session_state["current_question"] = None
    st.session_state["messages"].append(
        {"role": "assistant", "content": "Interview ended."}
    )
    st.rerun()
