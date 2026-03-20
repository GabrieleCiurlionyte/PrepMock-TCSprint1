import streamlit as st

def render_header(title: str, subheader: str, description: str | None = None): 
    st.title(title)
    st.subheader(subheader)
    
    if description is not None:
        st.markdown(description)