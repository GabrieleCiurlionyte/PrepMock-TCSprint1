from dataclasses import dataclass
from typing import Any
from openai import OpenAI
from openai.types.responses import ResponseInputParam

from .prompts.few_shot_examples import FEW_SHOT_EXAMPLES
from .prompts.instructions import DEVELOPER_INSTRUCTIONS
from .schemas import QuestionEvaluation

@dataclass(slots=True)
class InterviewEvaluatorConfig:
    model: str = "gpt-4.1-nano"
    top_p: float = 0.9
    temperature: float = 0.5
    max_output_tokens: int = 300
    store: bool = False
    
class InterviewEvaluatorService:
    def __init__(self, client: OpenAI, config: InterviewEvaluatorConfig | None = None):
        self.client = client
        self.config = config or InterviewEvaluatorConfig()

    def _build_message(self, role: str, content: Any) -> dict[str, Any]:
        if isinstance(content, list):
            normalized_content = content
        else:
            normalized_content = [{"type": "input_text", "text": str(content)}]

        return {
            "role": role,
            "content": normalized_content,
        }

    def _normalize_previous_messages(
        self, previous_messages: ResponseInputParam
    ) -> list[dict[str, Any]]:
        normalized_messages: list[dict[str, Any]] = []

        for message in previous_messages:
            role = message.get("role", "user")
            content = message.get("content", "")
            normalized_messages.append(self._build_message(role=role, content=content))

        return normalized_messages

    def build_input(
        self,
        previous_messages: ResponseInputParam,
        interview_question: str,
        interviewee_answer: str,
    ) -> list:
        return [
            *[
                self._build_message(role=example["role"], content=example["content"])
                for example in FEW_SHOT_EXAMPLES
            ],
            *self._normalize_previous_messages(previous_messages),
            self._build_message(
                role="user",
                content=(
                    "Interview question and reference answer:\n\n"
                    f"{interview_question}"
                ),
            ),
            self._build_message(
                role="user",
                content=(
                    "Interviewee answer:\n\n"
                    f"{interviewee_answer}"
                ),
            ),
        ]

    def evaluate(
        self,
        previous_messages: ResponseInputParam,
        interview_question: str,
        interviewee_answer: str,
    ) -> QuestionEvaluation:
        response = self.client.responses.parse(
            model=self.config.model,
            instructions=DEVELOPER_INSTRUCTIONS,
            input=self.build_input(
                previous_messages=previous_messages,
                interview_question=interview_question,
                interviewee_answer=interviewee_answer,
            ),
            text_format=QuestionEvaluation,
            store=self.config.store,
            top_p=self.config.top_p,
            temperature=self.config.temperature,
            max_output_tokens=self.config.max_output_tokens,
        )
        return response.output_parsed
