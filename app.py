import streamlit as st
import plotly.graph_objects as go
from utils.pdf_parser import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.section_analyzer import analyze_sections
from utils.resume_suggestions import generate_suggestions
from utils.ats_scorer import calculate_ats_score
from utils.job_role_predictor import predict_roles
from utils.skill_gap_analyzer import (
    analyze_skill_gaps,
    generate_learning_path
)
from utils.keyword_optimizer import optimize_keywords
from utils.ai_recommendations import generate_ai_recommendations
from utils.career_roadmap import generate_career_roadmap
from utils.resume_rewriter import generate_rewrite_suggestions
from utils.pdf_report import generate_pdf_report

def format_skill(skill):

    custom = {
        "sql": "SQL",
        "aws": "AWS",
        "fastapi": "FastAPI",
        "power bi": "Power BI",
        "github": "GitHub",
        "opencv": "OpenCV",
        "yolov8": "YOLOv8"
    }

    return custom.get(
        skill.lower(),
        skill.title()
    )

# -----------------------
# PAGE CONFIG
# -----------------------

st.set_page_config(
    page_title="ResumeIQ AI",
    page_icon="🚀",
    layout="wide"
)

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
    width="stretch"
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
    
    rewrite_suggestions = generate_rewrite_suggestions(resume_text)

    sections = analyze_sections(resume_text)

    st.subheader("📊 Resume Section Quality")

    for section, section_score in sections.items():

        st.write(f"{section} — {section_score}/100")

        st.progress(int(section_score))

    # Extract Skills
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    resume_skills = resume_skills if resume_skills else []
    job_skills = job_skills if job_skills else []
    
    keyword_suggestions = optimize_keywords(
    resume_text.split()
    )
    

    # Predict Job Roles
    role_predictions = predict_roles(resume_skills)
    
    top_role = list(role_predictions.keys())[0]

    career_roadmap = generate_career_roadmap(top_role)
    
    # Matching Skills
    # Matching Skills
    matching = set(resume_skills).intersection(set(job_skills))
    missing = set(job_skills) - set(resume_skills)
    
    ai_recommendations = generate_ai_recommendations(
    sections,
    missing
    )

    # Skill Gap Analysis
    skill_gap_results = analyze_skill_gaps(
        missing
    )

    # Learning Path
    learning_path = generate_learning_path(
        skill_gap_results
    )

    # Match Score
    if len(job_skills) > 0:
        score = int((len(matching) / len(job_skills)) * 100)
    else:
        score = 0
        # Resume Strength
    resume_strength = min(len(resume_skills) * 5, 100)
    # ATS Score
    ats_score = calculate_ats_score(
    match_score=score,
    section_scores=sections,
    resume_strength=resume_strength,
    missing_skills=missing
    )
    section_average = (
    sum(sections.values())
    / len(sections)
    )

    penalty = min(len(missing) * 2, 20)
    # Resume Strength
    suggestions = generate_suggestions(
    score,
    missing,
    sections
    )

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
    
    st.subheader("🎯 ATS Score Gauge")

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=ats_score,
        title={"text": "ATS Score"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "green"},
            "steps": [
                {"range": [0, 40], "color": "#ffcccc"},
                {"range": [40, 70], "color": "#fff4cc"},
                {"range": [70, 100], "color": "#ccffcc"}
            ]
        }
    ))

    fig.update_layout(
    height=350
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    
    
    st.subheader("📈 ATS Score Breakdown")

    st.write(f"✅ Skill Match Contribution: {int(score * 0.5)}")

    st.write(
        f"✅ Section Quality Contribution: "
        f"{int(section_average * 0.3)}"
    )

    st.write(
        f"✅ Resume Strength Contribution: "
        f"{int(resume_strength * 0.2)}"
    )

    st.write(
        f"❌ Missing Skills Penalty: "
        f"-{penalty}"
    )

    st.success(
        f"Final ATS Score: {ats_score}/100"
    )

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

            skills_html = ""

            for skill in resume_skills:
                skills_html += f"""
                <span style="
                    background:#1f2937;
                    color:white;
                    padding:8px 12px;
                    border-radius:15px;
                    margin:4px;
                    display:inline-block;
                ">
                {format_skill(skill)}
                </span>
                """

            st.markdown(skills_html, unsafe_allow_html=True)

        else:
            st.warning("No skills detected.")
    with right:
        st.subheader("Job Skills")

        if job_skills:

            skills_html = ""

            for skill in job_skills:
                skills_html += f"""
                <span style="
                    background:#1f2937;
                    color:white;
                    padding:8px 12px;
                    border-radius:15px;
                    margin:4px;
                    display:inline-block;
                ">
                {format_skill(skill)}
                </span>
                """

            st.markdown(skills_html, unsafe_allow_html=True)

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

            skills_html = ""

            for skill in matching:
                skills_html += f"""
                <span style="
                    background:#1f2937;
                    color:white;
                    padding:8px 12px;
                    border-radius:15px;
                    margin:4px;
                    display:inline-block;
                ">
                {format_skill(skill)}
                </span>
                """

            st.markdown(skills_html, unsafe_allow_html=True)

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
            width="stretch"
        )
    # -----------------------
    # DOWNLOAD REPORT
    # -----------------------

    pdf_report = generate_pdf_report(
    match_score=score,
    ats_score=ats_score,
    resume_strength=resume_strength,
    matching_skills=matching,
    missing_skills=missing,
    role_predictions=role_predictions,
    skill_gap_results=skill_gap_results,
    learning_path=learning_path,
    ai_recommendations=ai_recommendations,
    career_roadmap=career_roadmap,
    rewrite_suggestions=rewrite_suggestions
    )

    st.download_button(
        label="📄 Download Professional PDF Report",
        data=pdf_report,
        file_name="ResumeIQ_Report.pdf",
        mime="application/pdf"
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
        
    st.subheader("🔥 Skill Gap Analysis")

    if skill_gap_results:

        for item in skill_gap_results:

            st.write(
            f"{item['skill']} — {item['priority']}"
            )

    else:
        st.success(
        "No major skill gaps detected."
        )
        
    st.subheader("📚 Recommended Learning Path")

    if learning_path:

        for i, skill in enumerate(
            learning_path[:5],
            start=1
        ):
            st.write(
                f"{i}. {skill}"
            )    
    # -----------------------
    # RESUME IMPROVEMENT SUGGESTIONS
    # -----------------------

    st.subheader("📌 Resume Improvement Suggestions")

    if suggestions:
        for suggestion in suggestions:
            st.warning(suggestion)
    else:
        st.success("Your resume looks strong. No major improvements detected.")
        
        
    # -----------------------
    # AI RECOMMENDATIONS
    # -----------------------

    st.subheader("💡 AI Resume Recommendations")

    if ai_recommendations:

        for recommendation in ai_recommendations:

            st.markdown(
                f"### {recommendation['section']}"
            )

            for advice in recommendation["advice"]:

                st.info(advice)

    else:

        st.success(
            "No major recommendations detected."
        )
        
    # -----------------------
    # KEYWORD OPTIMIZER
    # -----------------------

    st.subheader("📝 Resume Keyword Optimizer")

    if keyword_suggestions:

        for item in keyword_suggestions:
            st.info(
                f"{item['current'].title()} → {item['suggested']}"
            )

    else:
        st.success(
            "No keyword optimization suggestions found."
        )    

    # -----------------------
    # RESUME REWRITE SUGGESTIONS
    # -----------------------

    st.subheader("✍️ Resume Rewrite Suggestions")

    if rewrite_suggestions:

        for suggestion in rewrite_suggestions:

            st.warning(f"Weak: {suggestion['weak']}")

            st.success(f"Better: {suggestion['better']}")

    else:
        st.success("No rewrite suggestions found.")
        
        
    # -----------------------
    # JOB ROLE PREDICTIONS
    # -----------------------
    

    st.subheader("🎯 Predicted Career Paths")

    for role, role_score in list(role_predictions.items())[:5]:

        st.markdown(
            f"""
            <div style="
                background:#1f2937;
                padding:15px;
                border-radius:12px;
                margin-bottom:12px;
                border-left:5px solid #22c55e;
            ">
                <h4 style="margin:0;">
                    {role}
                </h4>
                <p style="margin:5px 0 0 0;">
                    Match Score: <b>{role_score}%</b>
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.progress(role_score / 100)
    # -----------------------
    # CAREER ROADMAP
    # -----------------------

    st.subheader(f"🧭 Career Roadmap for {top_role}")

    st.markdown("### Skills To Learn")

    for skill in career_roadmap["skills"]:
        st.info(skill)

    st.markdown("### Projects To Build")

    for project in career_roadmap["projects"]:
        st.success(project)
        