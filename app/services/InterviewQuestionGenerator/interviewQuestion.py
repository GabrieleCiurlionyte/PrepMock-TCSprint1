from dataclasses import dataclass
from typing import Optional

@dataclass(slots=True, frozen=True)
class InterviewQuestion:
    id: str
    question: str
    answer: str
    difficulty: str
    topic: Optional[str] = None
