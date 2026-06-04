import plotly.express as px
import pandas as pd
import streamlit as st
from utils.pdf_parser import extract_text_from_pdf
from utils.skill_extractor import extract_skills

# -----------------------
# PAGE CONFIG
# -----------------------

st.set_page_config(
    page_title="ResumeIQ AI",
    page_icon="🚀",
    layout="wide"
)
if "analyzed" not in st.session_state:
    st.session_state["analyzed"] = False
# -----------------------
# CUSTOM CSS
# -----------------------

st.markdown("""
<style>

.main {
    background-color: #0e1117;
}

.hero {
    text-align: center;
    padding: 2rem;
    border-radius: 15px;
    background: linear-gradient(
        135deg,
        #4f46e5,
        #7c3aed
    );
    color: white;
}

.metric-card {
    background-color: #1f2937;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
}

.big-score {
    font-size: 40px;
    font-weight: bold;
    color: #22c55e;
}

</style>
""", unsafe_allow_html=True)

# -----------------------
# HERO SECTION
# -----------------------

st.markdown("""
<div class="hero">
    <h1>🚀 ResumeIQ AI</h1>
    <h3>AI Resume Analyzer & Job Match System</h3>
    <p>
    Upload your resume and compare it against any job description.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")

# -----------------------
# INPUT SECTION
# -----------------------

col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader(
        "📄 Upload Resume",
        type=["pdf"]
    )

with col2:
    job_description = st.text_area(
        "💼 Job Description",
        height=200
    )

st.write("")

analyze = st.button(
    "🔍 Analyze Resume",
    use_container_width=True
)

# -----------------------
# ANALYSIS
# -----------------------

if analyze:

    if uploaded_file is None:
        st.error("Please upload a resume PDF.")
        st.stop()

    # Extract Resume Text
    resume_text = extract_text_from_pdf(uploaded_file)

    # Extract Skills
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)
    
    resume_skills = resume_skills if resume_skills else []
    job_skills = job_skills if job_skills else []
    
    # Matching Skills
    matching = set(resume_skills).intersection(set(job_skills))
    missing = set(job_skills) - set(resume_skills)

    # Match Score
    if len(job_skills) > 0:
        score = int((len(matching) / len(job_skills)) * 100)
    else:
        score = 0

    # ATS Score
    ats_score = min(score + 15, 100)

    # Resume Strength
    resume_strength = min(len(resume_skills) * 5, 100)

    st.success("Resume Processed Successfully!")

    # -----------------------
    # METRICS
    # -----------------------

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Match Score</h3>
            <div class="big-score">{score}%</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>ATS Score</h3>
            <div class="big-score">{ats_score}%</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Resume Strength</h3>
            <div class="big-score">{resume_strength}%</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # -----------------------
    # EXTRACTED TEXT
    # -----------------------

    st.subheader("📄 Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=250
    )

    # -----------------------
    # SKILLS SECTION
    # -----------------------

    st.subheader("🧠 Skills Analysis")

    left, right = st.columns(2)

    with left:
        st.subheader("Resume Skills")
        if resume_skills:
            for skill in resume_skills:
                st.success(skill.title())
        else:
            st.warning("No skills detected.")

    with right:
        st.subheader("Job Skills")
        if job_skills:
            for skill in job_skills:
                st.info(skill.title())
        else:
            st.warning("No job skills detected.")

    st.write("")

    # -----------------------
    # MATCHING & MISSING
    # -----------------------

    left, right = st.columns(2)

    with left:
        st.subheader("Matching Skills")
        if matching:
            for skill in matching:
                st.success(skill.title())
        else:
            st.warning("No matching skills found.")

    with right:
        st.subheader("Missing Skills")
        if missing:
            for skill in missing:
                st.error(skill.title())
        else:
            st.success("No missing skills!")

    st.write("")

    # -----------------------
    # PIE CHART
    # -----------------------

    st.subheader("📊 Skill Match Analysis")

    matched_count = len(matching)
    missing_count = len(missing)

    st.write("DEBUG matched:", matched_count)
    st.write("DEBUG missing:", missing_count)

    if matched_count + missing_count == 0:
        st.warning("No skills available to generate chart.")
    else:
        import plotly.graph_objects as go

        fig = go.Figure(
            data=[
                go.Pie(
                    labels=["Matched", "Missing"],
                    values=[matched_count, missing_count],
                    hole=0.4
                )
            ]
        )

        fig.update_layout(
            title="Skill Match Analysis"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
    # -----------------------
    # DOWNLOAD REPORT
    # -----------------------

    report = f"""
ResumeIQ AI Report
==============================

Match Score: {score}%
ATS Score: {ats_score}%
Resume Strength: {resume_strength}%

Matching Skills:
{chr(10).join(matching)}

Missing Skills:
{chr(10).join(missing)}
"""

    st.download_button(
        label="📄 Download Report",
        data=report,
        file_name="ResumeIQ_Report.txt",
        mime="text/plain"
    )

    # -----------------------
    # ATS RECOMMENDATIONS
    # -----------------------

    st.subheader("🎯 ATS Recommendations")

    if missing:
        for skill in list(missing)[:5]:
            st.info(f"Add experience/projects in {skill.title()}.")
    else:
        st.success("Excellent! Your resume matches all required skills.")

    # -----------------------
    # CAREER RECOMMENDATIONS
    # -----------------------

    st.subheader("📈 Career Recommendations")

    st.progress(min(score + 20, 100))
    st.write(f"Data Analyst — {min(score + 20, 100)}%")

    st.progress(min(score + 10, 100))
    st.write(f"Data Scientist — {min(score + 10, 100)}%")

    st.progress(score)
    st.write(f"ML Engineer — {score}%")