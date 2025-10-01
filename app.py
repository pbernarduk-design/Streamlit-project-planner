import streamlit as st

st.set_page_config(page_title="Project Management Plan Editor", layout="wide")

st.title("📋 Project Management Plan Editor")

st.markdown("### Section 2.1: Project Description")
project_description = st.text_area("Enter your project description here:", height=200)

if project_description:
    st.markdown("### 🤖 AI Suggestions Based on Project Description")
    st.markdown("#### Project Objectives")
    st.text_area("Suggested Objectives", value=f"Based on your description: {project_description[:50]}... [AI-generated objectives here]", height=100)
    st.markdown("#### Project Scope")
    st.text_area("Suggested Scope", value=f"Scope derived from: {project_description[:50]}... [AI-generated scope here]", height=100)
    st.markdown("#### Project Governance")
    st.text_area("Suggested Governance", value=f"Governance based on: {project_description[:50]}... [AI-generated governance here]", height=100)
    st.markdown("#### Risk Management")
    st.text_area("Suggested Risks", value=f"Risks inferred from: {project_description[:50]}... [AI-generated risks here]", height=100)

    st.markdown("### 📤 Export Final Document")
    st.button("Export as Word Document (Coming Soon)")
