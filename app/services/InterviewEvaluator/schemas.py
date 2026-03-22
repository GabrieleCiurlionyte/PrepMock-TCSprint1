from pydantic import BaseModel
from typing import Optional

class QuestionEvaluation(BaseModel):
    off_topic: bool
    message: Optional[str] = None
    correct_answer: Optional[list[str]] = None
    incorrect_answer: Optional[list[str]] = None
    overall_score: Optional[int] = None
    explanation: Optional[str] = None