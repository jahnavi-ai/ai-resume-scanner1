import streamlit as st
from resume_parser import extract_text_from_pdf
from skill_matcher import match_skills

st.title("🧠 AI Resume Scanner")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

if uploaded_file is not None:
    resume_text = extract_text_from_pdf(uploaded_file)
    st.subheader("Extracted Text:")
    st.write(resume_text[:500])  # Show first 500 chars

    score = match_skills(resume_text)
    st.success(f"Your job match score: {score}%")
