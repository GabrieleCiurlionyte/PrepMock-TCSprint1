import os
from dotenv import load_dotenv
import streamlit as st

from services.InterviewEvaluator.InterviewEvaluatorConfig import (
    InterviewEvaluatorConfig,
    PromptType,
)

prompt_type_options = {
    "Using zero-shot": PromptType.ZERO_SHOT,
    "Using few-shot with generic examples": PromptType.FEW_SHOT_WITH_GENERIC_EXAMPLES,
    "Using few-shot with difficulty examples": PromptType.FEW_SHOT_WITH_DIFFICULTY_EXAMPLES,
    "Using simple": PromptType.SIMPLE,
    "Using chain-of-thought": PromptType.CHAIN_OF_THOUGHT,
}

def render_openai_configuration_sidebar() -> tuple[InterviewEvaluatorConfig, str | None]:
    load_dotenv()

    if "interview_evaluator_config" not in st.session_state:
        st.session_state["interview_evaluator_config"] = InterviewEvaluatorConfig()

    cfg: InterviewEvaluatorConfig = st.session_state["interview_evaluator_config"]

    with st.sidebar:
        st.subheader("Configure OpenAI client")

        env_key = os.getenv("OPENAI_API_KEY", "").strip()
        if env_key:
            api_key = env_key
            st.success("OpenAI key loaded from .env")
        else:
            api_key = st.text_input("OpenAI API Key", type="password", placeholder="sk-...").strip()

        model = st.selectbox(
            "Model",
            options=["gpt-4.1", "gpt-4.1-mini", "gpt-4.1-nano", "gpt-4o", "gpt-4o-mini"],
            index=["gpt-4.1", "gpt-4.1-mini", "gpt-4.1-nano", "gpt-4o", "gpt-4o-mini"].index(cfg.model),
        )

        temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=cfg.temperature, step=0.05)
        top_p = st.slider("Top-p", min_value=0.0, max_value=1.0, value=cfg.top_p, step=0.05)
        selected_prompt_label = st.selectbox(
            "Prompt type",
            options=list(prompt_type_options.keys()),
            index=list(prompt_type_options.values()).index(cfg.prompt_type),
        )
        prompt_type = prompt_type_options[selected_prompt_label]
        max_output_tokens = st.number_input("Max output tokens", min_value=1, max_value=4096, value=cfg.max_output_tokens, step=1)
        store = st.checkbox("Store responses", value=cfg.store)

    st.session_state["interview_evaluator_config"] = InterviewEvaluatorConfig(
        model=model,
        temperature=temperature,
        top_p=top_p,
        max_output_tokens=int(max_output_tokens),
        store=store,
        prompt_type=prompt_type
    )

    return st.session_state["interview_evaluator_config"], (api_key or None)
