import streamlit as st
import json

from parser import extract_text
from llm_engine import analyze_resume
from scorer import calculate_match

# Required skills
required_skills = ["python", "sql", "excel", "tableau", "data analysis"]

st.title("HireSense AI – Resume Screening System")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if uploaded_file:

    st.info("Processing resume...")
    st.write("Debug : file recieved!")
    # Extract text
    text = extract_text(uploaded_file)
    text = text[:2000]

    #  LLM analysis
    result = analyze_resume(text)

    # Parse JSON safely
    try:
        import re
        json_match = re.search(r"\{.*\}", result, re.DOTALL)
        data = json.loads(json_match.group())
    except:
        st.error("Error processing resume")
        st.write(result)
        st.stop()

    #  Calculate score
    final_score = calculate_match(data["skills"], required_skills, text)

    #  Display results
    st.subheader("Analysis Results")

    st.write("### Skills")
    st.write(data["skills"])

    st.write("### Experience Summary")
    st.write(data["experience_summary"])

    st.write("### Final Score")
    st.success(f"{final_score} / 100")

    st.write("### Missing Skills")
    st.write(data["missing_skills"])

    st.write("### Recommendation")
    st.write(data["recommendation"])
