from dataclasses import dataclass, field
import re


MAX_ANSWER_LENGTH = 4000

BLOCK_PATTERNS: tuple[tuple[str, str], ...] = (
    (r"\bignore\s+(all\s+)?(previous|prior|above)\s+instructions\b", "instruction_override"),
    (r"\breveal\s+(the\s+)?(system|developer)\s+prompt\b", "prompt_exfiltration"),
    (r"\bshow\s+(me\s+)?(your\s+)?(system|developer)\s+prompt\b", "prompt_exfiltration"),
    (r"\bact\s+as\b", "role_override"),
    (r"^\s*(system|assistant|developer)\s*:", "role_prefix"),
    (r"\b(change|set|override)\s+(the\s+)?(score|rules?)\b", "score_manipulation"),
    (r"\bdo\s+not\s+follow\s+(the\s+)?(rubric|instructions|rules)\b", "instruction_override"),
)

@dataclass(slots=True)
class GuardResult:
    allowed: bool
    sanitized_answer: str
    reason: str | None = None
    flags: list[str] = field(default_factory=list)


def _normalize_answer(answer: str) -> str:
    stripped = answer.strip()
    collapsed_blank_lines = re.sub(r"\n\s*\n+", "\n\n", stripped)
    return collapsed_blank_lines


def validate_interview_answer(answer: str) -> GuardResult:
    sanitized_answer = _normalize_answer(answer)

    if not sanitized_answer:
        return GuardResult(
            allowed=False,
            sanitized_answer=sanitized_answer,
            reason="Please enter an actual interview answer before submitting.",
            flags=["empty_answer"],
        )

    if len(sanitized_answer) > MAX_ANSWER_LENGTH:
        return GuardResult(
            allowed=False,
            sanitized_answer=sanitized_answer,
            reason="Your answer is too long. Please keep it under 4000 characters.",
            flags=["answer_too_long"],
        )

    lowered_answer = sanitized_answer.lower()
    matched_flags: list[str] = []

    for pattern, flag in BLOCK_PATTERNS:
        if re.search(pattern, lowered_answer, flags=re.MULTILINE):
            matched_flags.append(flag)

    if matched_flags:
        return GuardResult(
            allowed=False,
            sanitized_answer=sanitized_answer,
            reason=(
                "Your message looks like it is trying to control the evaluator rather than "
                "answer the interview question. Please answer the question directly."
            ),
            flags=matched_flags,
        )

    return GuardResult(
        allowed=True,
        sanitized_answer=sanitized_answer,
    )
