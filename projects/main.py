import streamlit as st

from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5-coder:latest",
    temperature=0
)

st.title("🗣️ Translation App | Langchain + Streamlit + Ollama")

if st.session_state == None:
    st.session_state['selected_language'] = "French"

language_options = st.sidebar.selectbox(
    "Select a Language to Translate",
    ("French", "Hindi", "Telugu", "Tamil"),
)

st.session_state['selected_language'] = language_options

st.sidebar.info(f"Selected Option: {st.session_state['selected_language']}")


def generate_response(input_text):
    translation_prompt = f"""
        You're an expert translator. translate the input text provided
        {input_text}. translate into {st.session_state['selected_language']}.
    """
    assitant_prompt = f"""
        you're an ai assistant. respond to my input queries {input_text}
    """
    response = llm.invoke(assitant_prompt)
    st.success(response.content)


with st.form("my_form"):
    text = st.text_area(
        "Enter your prompt:",
        "What you want to translate today !",
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)
