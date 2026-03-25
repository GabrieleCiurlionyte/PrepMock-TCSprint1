from dotenv import load_dotenv
from openai import OpenAI
from .interviewEvaluatorService import (
    InterviewEvaluatorConfig,
    InterviewEvaluatorService,
)
import streamlit as st

load_dotenv()

def EvaluateIntervieweeResponse(
    interviewEvaluatorConfig: InterviewEvaluatorConfig,
    interview_question: str,
    interviewee_answer: str,
    openai_api_key: str | None = None,
):
    client = OpenAI(api_key=openai_api_key) if openai_api_key else OpenAI()
    
    evaluator = InterviewEvaluatorService(
        client=client,
        config=interviewEvaluatorConfig
    )
    
    result = evaluator.evaluate(
        previous_messages=st.session_state["messages"],
        interview_question=interview_question,
        interviewee_answer=interviewee_answer
    )
    
    return result
