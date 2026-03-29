def format_evaluation_response(evaluation) -> str:
    is_teaching_response = evaluation.overall_score is None

    lines = [
        f"**Score:** {evaluation.overall_score}"
        if evaluation.overall_score is not None
        else "**Score:** N/A"
    ]

    if evaluation.message:
        lines.append(f"**Message:** {evaluation.message}")

    if evaluation.correct_answer:
        lines.append("")
        lines.append("**Correct points:**")
        lines.extend(f"- {item}" for item in evaluation.correct_answer)

    if evaluation.incorrect_answer and not is_teaching_response:
        lines.append("")
        lines.append("**Needs improvement:**")
        lines.extend(f"- {item}" for item in evaluation.incorrect_answer)

    if evaluation.explanation:
        lines.append("")
        lines.append(f"**Explanation:** {evaluation.explanation}")

    if evaluation.code_examples:
        lines.append("")
        lines.append("**Code examples:**")

        for example in evaluation.code_examples:
            lines.append("")
            lines.append(f"**{example.title}:**")
            lines.append("```csharp")
            lines.append("\n".join(example.code_lines).strip())
            lines.append("```")

    return "\n".join(lines)
