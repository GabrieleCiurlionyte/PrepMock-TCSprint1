from dataclasses import dataclass
from typing import Optional
from enum import Enum

class Difficulty(Enum):
    NONE = 0
    EASY = 1
    MEDIUM = 2
    HARD = 3

@dataclass(slots=True, frozen=True)
class InterviewQuestion:
    id: int
    question: str
    answer: str
    difficulty: Difficulty = None
    topic: Optional[str] = None
