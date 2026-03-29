from dataclasses import dataclass

@dataclass(slots=True)
class InterviewEvaluatorConfig:
    model: str = "gpt-4.1-nano"
    top_p: float = 1.0
    temperature: float = 0.2
    max_output_tokens: int = 700
    store: bool = False
