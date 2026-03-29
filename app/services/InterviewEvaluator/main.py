from openai import OpenAI
from .InterviewEvaluatorConfig import InterviewEvaluatorConfig
from .interviewEvaluatorService import InterviewEvaluatorService
from .schemas import QuestionEvaluation

def EvaluateIntervieweeResponse(
    interviewEvaluatorConfig: InterviewEvaluatorConfig,
    interview_question: str,
    interviewee_answer: str,
    openai_api_key: str,
) -> QuestionEvaluation :
    client = OpenAI(api_key=openai_api_key)
    
    evaluator = InterviewEvaluatorService(
        client=client,
        config=interviewEvaluatorConfig
    )
    
    result = evaluator.evaluate(
        interview_question=interview_question,
        interviewee_answer=interviewee_answer
    )
    
    return result
