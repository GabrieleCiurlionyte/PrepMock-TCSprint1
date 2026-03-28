from dataclasses import dataclass

@dataclass(slots=True)
class InterviewEvaluatorConfig:
    model: str = "gpt-4.1-nano"
    top_p: float = 0.9
    temperature: float = 0.5
    max_output_tokens: int = 300
    store: bool = False
