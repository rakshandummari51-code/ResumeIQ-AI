def analyze_education(education_items):

    results = []

    for item in education_items:

        item_lower = item.lower()

        if (
            "data science" in item_lower
            or "computer science" in item_lower
            or "cse" in item_lower
        ):
            results.append({
                "name": item,
                "domain_alignment": "High",
                "industry_relevance": "AI, Data Science, Software Development",
                "score": 9,
                "career_roles": [
                    "AI Engineer",
                    "Data Scientist",
                    "Data Analyst",
                    "Software Developer"
                ]
            })

        elif (
            "engineering" in item_lower
            or "technology" in item_lower
        ):
            results.append({
                "name": item,
                "domain_alignment": "Medium",
                "industry_relevance": "Technology and Engineering",
                "score": 7,
                "career_roles": [
                    "Software Developer",
                    "Technical Analyst"
                ]
            })

        else:
            results.append({
                "name": item,
                "domain_alignment": "General",
                "industry_relevance": "General Career Development",
                "score": 5,
                "career_roles": [
                    "General Professional Role"
                ]
            })

    return results