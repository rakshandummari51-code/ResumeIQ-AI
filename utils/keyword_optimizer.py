def optimize_keywords(resume_skills):

    keyword_map = {
        "ml": "Machine Learning",
        "ai": "Artificial Intelligence",
        "nlp": "Natural Language Processing",
        "cv": "Computer Vision",
        "js": "JavaScript",
        "github": "Git",
        "powerbi": "Power BI",
        "sklearn": "Scikit-Learn"
    }

    suggestions = []

    for skill in resume_skills:

        skill_lower = skill.lower()

        if skill_lower in keyword_map:

            suggestions.append({
                "current": skill,
                "suggested": keyword_map[skill_lower]
            })

    return suggestions