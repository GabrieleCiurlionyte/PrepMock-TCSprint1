import os

from dotenv import load_dotenv
import streamlit as st


## TODO: these should probably be saved in the state
## TODO; there should be documentation of what are the largest values
def render_OpenAPIConfigurationSideBar() -> str | None:
    load_dotenv()
    env_openai_key = os.getenv("OPENAI_API_KEY", "").strip()

    with st.sidebar:
        st.subheader("Configure OpenAPI client")

        st.markdown("OpenAI key")
        if env_openai_key:
            st.success("OpenAI key loaded from .env")
            st.session_state["openai_api_key"] = env_openai_key
        else:
            st.info("OPENAI_API_KEY not found in .env. Please enter it below.")
            st.session_state["openai_api_key"] = st.text_input(
                "OpenAI API Key",
                value=st.session_state.get("openai_api_key", ""),
                type="password",
                placeholder="sk-...",
            ).strip()

        ### TODO: add validation of the OPENAI key

        st.markdown("Model type")

        ## TODO: create a dropdown

        st.slider("Model temperature", 0, 1, 0, 1)

        st.slider("Model's top-p", 0, 1, 0, 1)

        ### Add a comment that it is recommended that only
        # one needs to be redacted

        st.divider()
        st.caption("Built by Gabriele Ciurlionyte")

    return st.session_state.get("openai_api_key") or None
