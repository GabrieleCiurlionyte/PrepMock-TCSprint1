from typing import Any
from openai import OpenAI

from .InterviewEvaluatorConfig import InterviewEvaluatorConfig
from .prompts.few_shot_examples import FEW_SHOT_EXAMPLES
from .prompts.instructions import DEVELOPER_INSTRUCTIONS
from .schemas import FallbackQuestionEvaluation, QuestionEvaluation
    
class InterviewEvaluatorService:
    def __init__(self, client: OpenAI, config: InterviewEvaluatorConfig | None = None):
        self.client = client
        self.config = config or InterviewEvaluatorConfig()

    def _build_message(self, role: str, content: Any) -> dict[str, Any]:
        if isinstance(content, list):
            normalized_content = content
        else:
            content_type = "output_text" if role == "assistant" else "input_text"
            normalized_content = [{"type": content_type, "text": str(content)}]

        return {
            "role": role,
            "content": normalized_content,
        }

    def build_input(
        self,
        interview_question: str,
        interviewee_answer: str,
    ) -> list[dict[str, Any]]:
        inputList = []

        self._add_few_shot_examples(inputList)
        inputList.append(self._build_message(
                role="user",
                content=(
                    "Interview question and reference answer:\n\n"
                    f"{interview_question}"
                ),
            ))
        inputList.append(self._build_message(
                role="user",
                content=(
                    "Interviewee answer:\n\n"
                    f"{interviewee_answer}"
                ),
            ))
        return inputList

    def _add_few_shot_examples(self, input_list: list[dict[str, Any]]) -> None:
        for example in FEW_SHOT_EXAMPLES:
            input_list.append(
                self._build_message(role=example["role"], content=example["content"])
            )

    def evaluate(
        self,
        interview_question: str,
        interviewee_answer: str,
    ) -> QuestionEvaluation:
        response = self.client.responses.parse(
            model=self.config.model,
            instructions=DEVELOPER_INSTRUCTIONS,
            input=self.build_input(
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