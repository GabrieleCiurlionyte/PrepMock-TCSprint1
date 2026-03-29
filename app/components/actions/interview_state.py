import streamlit as st


def is_interview_active() -> bool:
    return not st.session_state["interview_active"]


def can_submit_answer() -> bool:
    return (
        st.session_state["interview_active"]
        and not st.session_state["interview_complete"]
    )

def _append_question_message() -> None:
    question = st.session_state["current_question"]
    content: str

    if question is None:
        content = (
            "No more questions are available for this difficulty. "
            "Your interview is complete."
        )
        st.session_state["interview_active"] = False
        st.session_state["interview_complete"] = True
    else:
        st.session_state["interview_complete"] = False
        content = (
            f"**Interview Question #{st.session_state['generator'].asked_count}**\n"
            f"{question.question}"
        )

    st.session_state["messages"].append({"role": "assistant", "content": content})


def start_interview() -> None:
    st.session_state["generator"].reset_session()
    st.session_state["messages"] = []
    st.session_state["interview_active"] = True
    st.session_state["interview_complete"] = False

    q = st.session_state["generator"].provide_interview_question(
        difficulty=st.session_state["difficulty"]
    )
    st.session_state["current_question"] = q
    _append_question_message()


def advance_to_next_question() -> None:
    q = st.session_state["generator"].provide_interview_question(
        difficulty=st.session_state["difficulty"]
    )
    st.session_state["current_question"] = q
    _append_question_message()


def repeat_same_question() -> None:
    question = st.session_state["current_question"]

    if question is None:
        return

    st.session_state["messages"].append(
        {
            "role": "assistant",
            "content": (
                "Please answer the same question again with a relevant technical answer.\n\n"
                f"**Interview Question #{st.session_state['generator'].asked_count}**\n"
                f"{question.question}"
            ),
        }
    )


def end_interview() -> None:
    st.session_state["interview_active"] = False
    st.session_state["interview_complete"] = False
    st.session_state["current_question"] = None
    st.session_state["messages"].append(
        {"role": "assistant", "content": "Interview ended."}
    )
