import random
from dataclasses import dataclass, field

from .interviewQuestion import InterviewQuestion

@dataclass(slots=True)
class InterviewQuestionGenerator:
    question_bank: list[InterviewQuestion]
    asked_question_ids: set[str] = field(default_factory=set)

    def provide_interview_question(self, difficulty: str | None = None) -> InterviewQuestion | None:
        available_questions = [
            q for q in self.question_bank
            if q.id not in self.asked_question_ids
            and (difficulty is None or q.difficulty == difficulty)
        ]

        if not available_questions:
            return None

        question = random.choice(available_questions)
        self.asked_question_ids.add(question.id)
        return question

    def reset_session(self) -> None:
        self.asked_question_ids.clear()
        
