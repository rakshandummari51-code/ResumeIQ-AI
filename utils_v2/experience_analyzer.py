def analyze_experience(experiences):

    results = []

    for exp in experiences:

        exp_lower = exp.lower()

        if "data analytics" in exp_lower:

            results.append({
                "name": exp,
                "type": "Data Analytics Internship",
                "impact": "High",
                "score": 8,
                "career_roles": [
                    "Data Analyst",
                    "Business Analyst"
                ]
            })

        elif "data science" in exp_lower:

            results.append({
                "name": exp,
                "type": "Data Science Internship",
                "impact": "High",
                "score": 9,
                "career_roles": [
                    "Data Scientist",
                    "AI Engineer"
                ]
            })

        else:

            results.append({
                "name": exp,
                "type": "General Internship",
                "impact": "Medium",
                "score": 6,
                "career_roles": [
                    "Software Developer"
                ]
            })

    return results