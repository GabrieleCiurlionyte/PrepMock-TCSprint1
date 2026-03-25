import streamlit as st

def _start_interview() -> None:
    st.session_state["generator"].reset_session()
    st.session_state["messages"] = []

    q = st.session_state["generator"].provide_interview_question(
        difficulty=st.session_state["difficulty"]
    )
    st.session_state["current_question"] = q

    if q is None:
        st.session_state["messages"].append(
            {"role": "assistant", "content": "No questions available for this difficulty."}
        )
        return

    st.session_state["messages"].append(
        {
            "role": "assistant",
            "content": f"**Interview Question #{st.session_state['generator'].asked_count}**\n{q.question}",
        }
    )

