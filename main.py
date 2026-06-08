import streamlit as st
from prompt import prompt_template
from model import get_response
from parser import parse_response

st.title("Resume Extractor")

resume_text = st.text_area("Paste Resume")

if st.button("Extract"):
    prompt = prompt_template.format(
        resume_text=resume_text
    )

    response = get_response(prompt)
    result = parse_response(response)

    st.success("Extraction Completed")

    st.json(result.model_dump())