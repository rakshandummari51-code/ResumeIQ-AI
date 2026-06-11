def generate_recruiter_summary(
    name,
    top_role,
    resume_skills,
    project_analysis,
    experience_analysis,
    certification_analysis,
    education_analysis,
    ats_score_v2
):

    strong_projects = [
        project["name"]
        for project in project_analysis
        if project["impact_score"] >= 8
    ]

    strong_experience = [
        exp["name"]
        for exp in experience_analysis
        if exp["score"] >= 8
    ]

    high_certifications = []

    for cert in certification_analysis:
        cert_name = cert["name"].replace("", "").replace("", "").strip()

        if cert["impact"] == "High" and len(cert_name) < 80:
            high_certifications.append(cert_name)

    education_strength = "relevant academic background"

    if education_analysis:
        best_education = max(
            education_analysis,
            key=lambda edu: edu.get("score", 0)
        )

    education_strength = best_education["industry_relevance"]

    summary = (
        f"{name} demonstrates strong potential for {top_role} and related roles with "
        f"hands-on skills in {', '.join(resume_skills[:6])}. "
    )

    if strong_projects:
        summary += (
            f"The candidate has built impactful projects such as "
            f"{', '.join(strong_projects[:2])}, showing practical execution ability. "
        )

    if strong_experience:
        summary += (
            f"They also have internship experience through "
            f"{', '.join(strong_experience[:2])}, adding real-world exposure. "
        )

    if high_certifications:
        summary += (
            f"Their certifications in "
            f"{', '.join(high_certifications[:3])} strengthen their profile further. "
        )

    summary += (
        f"Their education shows alignment with {education_strength}. "
        f"Overall, the resume shows an ATS V2 score of {ats_score_v2}/100, "
        f"making the candidate suitable for entry-level opportunities in "
        f"{top_role} and related career paths."
    )

    return summary