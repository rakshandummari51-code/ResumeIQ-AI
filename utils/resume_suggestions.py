def generate_suggestions(
    score,
    missing_skills,
    section_scores
):

    suggestions = []

    # Match Score
    if score < 50:
        suggestions.append(
            "Increase skill match with the job description."
        )

    # Missing Skills
    if len(missing_skills) > 0:
        suggestions.append(
            f"Consider learning: {', '.join(list(missing_skills)[:5])}"
        )

    # Section Analysis
    if section_scores["Projects"] < 70:
        suggestions.append(
            "Add more projects or describe them in greater detail."
        )

    if section_scores["Experience"] < 70:
        suggestions.append(
            "Add internships, freelance work, or practical experience."
        )

    if section_scores["Certifications"] < 70:
        suggestions.append(
            "Add relevant certifications to strengthen your profile."
        )

    if section_scores["Education"] < 70:
        suggestions.append(
            "Provide more education details such as CGPA or percentage."
        )

    return suggestions