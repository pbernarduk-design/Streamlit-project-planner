
import streamlit as st
from docx import Document
from io import BytesIO
import base64

# Define editable section and AI-suggested sections
editable_section = "2.1 Project Description"
suggested_sections = [
    "2.2 Project Objectives",
    "2.3 Project Scope",
    "2.4 Project Governance",
    "2.5 Risk Management"
]

st.title("📝 Project Management Plan Editor")

# Editable Section 2.1
st.subheader(editable_section)
project_description = st.text_area("Enter your project description here:", height=200)

# Generate AI suggestions based on project description
def generate_ai_suggestion(section_title, description):
    return f"Suggested content for {section_title} based on the project description: {description[:100]}..."

accepted_content = {}

if project_description:
    st.subheader("AI Suggestions")
    for section in suggested_sections:
        st.markdown(f"### {section}")
        suggestion = generate_ai_suggestion(section, project_description)
        with st.expander("View Suggestion"):
            st.write(suggestion)
        action = st.radio(f"What would you like to do with the suggestion for {section}?", 
                          ["Accept", "Refine", "Reject"], key=section)
        if action == "Accept":
            accepted_content[section] = suggestion
        elif action == "Refine":
            refined = st.text_area(f"Refine the suggestion for {section}:", value=suggestion, key=f"refine_{section}")
            accepted_content[section] = refined
        else:
            accepted_content[section] = ""

# Export final document
if st.button("Export Final Document"):
    new_doc = Document()
    new_doc.add_heading("Project Management Plan", level=1)
    new_doc.add_heading(editable_section, level=2)
    new_doc.add_paragraph(project_description)
    for section in suggested_sections:
        new_doc.add_heading(section, level=2)
        new_doc.add_paragraph(accepted_content.get(section, ""))
    buffer = BytesIO()
    new_doc.save(buffer)
    buffer.seek(0)
    b64 = base64.b64encode(buffer.read()).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="Final_Project_Management_Plan.docx">📥 Download Final Document</a>'
    st.markdown(href, unsafe_allow_html=True)
