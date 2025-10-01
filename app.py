import streamlit as st
from docx import Document
from io import BytesIO

st.title("Project Management Plan Editor")

# Section 2.1: Project Description
project_description = st.text_area("Section 2.1: Project Description", height=200)

# Placeholder AI suggestions based on project description
def generate_suggestions(description):
    return {
        "Objectives": f"Based on the project description, the objectives may include achieving key milestones and delivering value to stakeholders.",
        "Scope": f"The scope of the project includes all activities necessary to fulfill the project goals as described.",
        "Governance": f"Governance will be managed through regular meetings and oversight by the project steering committee.",
        "Risk Management": f"Potential risks include resource constraints and timeline delays, which will be mitigated through proactive planning."
    }

suggestions = {}
if project_description:
    if st.button("Generate AI Suggestions"):
        suggestions = generate_suggestions(project_description)

# Accept / Refine / Reject controls
final_sections = {}
for section, suggestion in suggestions.items():
    st.subheader(section)
    st.write("Suggested Content:")
    st.info(suggestion)
    action = st.radio(f"What would you like to do with the {section} section?", ["Accept", "Refine", "Reject"], key=section)
    if action == "Accept":
        final_sections[section] = suggestion
    elif action == "Refine":
        refined_text = st.text_area(f"Refine {section} content:", suggestion, key=f"refine_{section}")
        final_sections[section] = refined_text
    else:
        final_sections[section] = ""

# Export to Word
if final_sections and st.button("Export Final Document"):
    doc = Document()
    doc.add_heading("Project Management Plan", 0)
    doc.add_heading("Section 2.1: Project Description", level=1)
    doc.add_paragraph(project_description)
    for section, content in final_sections.items():
        doc.add_heading(section, level=1)
        doc.add_paragraph(content)
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    st.download_button(label="Download Project Management Plan", data=buffer, file_name="Project_Management_Plan.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
