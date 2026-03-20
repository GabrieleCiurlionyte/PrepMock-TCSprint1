import streamlit as st
from components.DifficultySelector import render_difficulty_selector
from components.Header import render_header
from components.SideBar import render_OpenAPIConfigurationSideBar

# Page configuration
st.set_page_config(
    page_title="PrepMock - Interview Prep Assistant",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="auto"
)

# TODO: setup streamlit theming

render_OpenAPIConfigurationSideBar()

render_header(
    title="PrepMock",
    subheader="AI interview practice for software engineers",
    description="Configure OpenAPI key. Select your level, answer technical interview questions, and receive structured feedback."
)

# TODO: set up side bar where to configure your openAPI key

difficulty = render_difficulty_selector()

# How does streamlit styling work?





### Let's define the instructions on
# how ot use the app

# Onboarding section

startInterviewButtonState = st.button("Start Interview")
print(startInterviewButtonState)


# TODO: if enough time create custom icon styling for streamlit components
with st.chat_message("user"):
    st.write("Hello 👋")


prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")


