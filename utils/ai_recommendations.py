def generate_ai_recommendations(section_scores, missing_skills):

    recommendations = []

    # -----------------------
    # PROJECTS
    # -----------------------

    if section_scores.get("Projects", 0) < 70:
        recommendations.append({
            "section": "Projects",
            "advice": [
                "Add more detailed project descriptions.",
                "Mention technologies used in each project.",
                "Add GitHub or live demo links.",
                "Include measurable outcomes such as accuracy, speed, users, or performance improvement."
            ]
        })

    # -----------------------
    # EXPERIENCE
    # -----------------------

    if section_scores.get("Experience", 0) < 70:
        recommendations.append({
            "section": "Experience",
            "advice": [
                "Add internship, freelance, open-source, or academic project experience.",
                "Mention your responsibilities clearly.",
                "Use strong action verbs like developed, built, optimized, implemented, and analyzed.",
                "Include measurable impact wherever possible."
            ]
        })

    # -----------------------
    # SKILLS
    # -----------------------

    if section_scores.get("Skills", 0) < 70:
        recommendations.append({
            "section": "Skills",
            "advice": [
                "Add more job-relevant technical skills.",
                "Group skills into categories like Languages, Frameworks, Tools, Databases, and Cloud.",
                "Avoid adding skills that you cannot explain confidently.",
                "Include skills that match the job description."
            ]
        })

    # -----------------------
    # CERTIFICATIONS
    # -----------------------

    if section_scores.get("Certifications", 0) < 70:
        recommendations.append({
            "section": "Certifications",
            "advice": [
                "Add relevant certifications from trusted platforms.",
                "Include certifications related to Python, SQL, Machine Learning, Cloud, or Data Analytics.",
                "Mention the certification provider name clearly.",
                "Keep certifications relevant to the job role."
            ]
        })

    # -----------------------
    # EDUCATION
    # -----------------------

    if section_scores.get("Education", 0) < 70:
        recommendations.append({
            "section": "Education",
            "advice": [
                "Add degree, college/university name, and graduation year.",
                "Mention CGPA or percentage if it is strong.",
                "Include relevant coursework if you are a fresher.",
                "Keep education details clean and easy to scan."
            ]
        })

    # -----------------------
    # MISSING SKILLS
    # -----------------------

    if len(missing_skills) > 0:
        top_missing = list(missing_skills)[:5]

        recommendations.append({
            "section": "Missing Skills",
            "advice": [
                f"Focus on improving these missing skills: {', '.join(top_missing)}.",
                "Build small projects using the missing high-priority skills.",
                "Add only genuine skills after gaining hands-on practice.",
                "Update your resume based on the target job description."
            ]
        })

    # -----------------------
    # GENERAL RECOMMENDATION
    # -----------------------

    if not recommendations:
        recommendations.append({
            "section": "Overall Resume",
            "advice": [
                "Your resume looks strong for the selected job description.",
                "Keep project descriptions specific and measurable.",
                "Continue updating your resume with new projects and achievements."
            ]
        })

    return recommendations