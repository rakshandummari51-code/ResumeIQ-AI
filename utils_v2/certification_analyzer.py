def analyze_certifications(certifications):

    certification_database = {
        "ai fundamentals": {
            "category": "Artificial Intelligence",
            "impact": "High",
            "score": 8,
            "career_roles": ["AI Engineer", "Machine Learning Engineer"]
        },
        "python": {
            "category": "Programming",
            "impact": "High",
            "score": 8,
            "career_roles": ["Python Developer", "Data Scientist", "AI Engineer"]
        },
        "data visualization": {
            "category": "Data Analytics",
            "impact": "Medium",
            "score": 7,
            "career_roles": ["Data Analyst", "Data Scientist"]
        },
        "data science": {
            "category": "Data Science",
            "impact": "High",
            "score": 8,
            "career_roles": ["Data Scientist", "AI Engineer"]
        },
        "sql": {
            "category": "Database",
            "impact": "Medium",
            "score": 7,
            "career_roles": ["Data Analyst", "Backend Developer"]
        },
        "oracle": {
            "category": "Database",
            "impact": "Medium",
            "score": 7,
            "career_roles": ["Database Developer", "Backend Developer"]
        },
        "communication": {
            "category": "Soft Skills",
            "impact": "Medium",
            "score": 6,
            "career_roles": ["Any Professional Role"]
        },
        "problem solving": {
            "category": "Core Skill",
            "impact": "High",
            "score": 8,
            "career_roles": ["Software Developer", "Data Analyst", "AI Engineer"]
        }
    }

    results = []

    for cert in certifications:

        cert_lower = cert.lower()
        matched = False

        for keyword, details in certification_database.items():

            if keyword in cert_lower:
                results.append({
                    "name": cert,
                    "category": details["category"],
                    "impact": details["impact"],
                    "score": details["score"],
                    "career_roles": details["career_roles"]
                })
                matched = True
                break

        if not matched:
            results.append({
                "name": cert,
                "category": "General",
                "impact": "Low",
                "score": 5,
                "career_roles": ["General Career Development"]
            })

    return results