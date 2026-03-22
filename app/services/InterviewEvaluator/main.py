from dotenv import load_dotenv
from openai import OpenAI, conversations
from .interviewEvaluatorService import (
    InterviewEvaluatorConfig,
    InterviewEvaluatorService,
)
import streamlit as st

load_dotenv()

conversation = conversations.create()

client = OpenAI()

def EvaluateIntervieweeResponse(interviewEvaluatorConfig : InterviewEvaluatorConfig, interview_question: str, interviewee_answer : str):
    
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
