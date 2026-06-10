def analyze_projects(projects):

    project_database = {
        "resumeiq": {
            "type": "AI Career Intelligence Platform",
            "complexity": "High",
            "impact_score": 9,
            "career_roles": [
                "AI Engineer",
                "Data Scientist",
                "Python Developer"
            ]
        },

        "attendance": {
            "type": "Computer Vision System",
            "complexity": "High",
            "impact_score": 9,
            "career_roles": [
                "AI Engineer",
                "Computer Vision Engineer",
                "Backend Developer"
            ]
        },

        "fraud": {
            "type": "Machine Learning Project",
            "complexity": "Medium",
            "impact_score": 8,
            "career_roles": [
                "Data Scientist",
                "Machine Learning Engineer"
            ]
        },

        "titanic": {
            "type": "Predictive Analytics Project",
            "complexity": "Beginner",
            "impact_score": 6,
            "career_roles": [
                "Data Analyst",
                "Data Scientist"
            ]
        },

        "sales": {
            "type": "Forecasting Project",
            "complexity": "Medium",
            "impact_score": 7,
            "career_roles": [
                "Data Analyst",
                "Business Analyst"
            ]
        },

        "iris": {
            "type": "Classification Project",
            "complexity": "Beginner",
            "impact_score": 6,
            "career_roles": [
                "Data Scientist",
                "Machine Learning Intern"
            ]
        },

        "movie": {
            "type": "Prediction System",
            "complexity": "Medium",
            "impact_score": 7,
            "career_roles": [
                "Data Scientist",
                "Machine Learning Engineer"
            ]
        }
    }

    results = []

    for project in projects:

        if isinstance(project, dict):
            project_name = project.get("name", "")
        else:
            project_name = str(project)

        project_lower = project_name.lower()
        matched = False

        for keyword, details in project_database.items():

            if keyword in project_lower:

                results.append({
                    "name": project_name,
                    "type": details["type"],
                    "complexity": details["complexity"],
                    "impact_score": details["impact_score"],
                    "career_roles": details["career_roles"]
                })

                matched = True
                break

        if not matched:

            results.append({
                "name": project_name,
                "type": "General Software Project",
                "complexity": "Medium",
                "impact_score": 6,
                "career_roles": [
                    "Software Developer"
                ]
            })

    return results