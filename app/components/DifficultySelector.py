import streamlit as st

def render_difficulty_selector(key: str = "difficulty") -> str:
    if key not in st.session_state:
        st.session_state[key] = "Easy"

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Easy", key=f"{key}_easy", use_container_width=True):
            st.session_state[key] = "Easy"

    with col2:
        if st.button("Medium", key=f"{key}_medium", use_container_width=True):
            st.session_state[key] = "Medium"

    with col3:
        if st.button("Hard", key=f"{key}_hard", use_container_width=True):
            st.session_state[key] = "Hard"

    return st.session_state[key]
