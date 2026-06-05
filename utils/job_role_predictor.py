def predict_roles(skills):

    role_database = {
        "AI Engineer": [
            "python",
            "artificial intelligence",
            "machine learning",
            "deep learning",
            "computer vision",
            "object detection",
            "fastapi"
        ],

        "Machine Learning Engineer": [
            "python",
            "machine learning",
            "deep learning",
            "computer vision",
            "object detection",
            "scikit-learn"
        ],

        "Backend Developer": [
            "python",
            "java",
            "sql",
            "fastapi",
            "git"
        ],

        "Data Analyst": [
            "sql",
            "excel",
            "python",
            "data analysis",
            "data visualization",
            "power bi"
        ],

        "Data Scientist": [
            "python",
            "sql",
            "machine learning",
            "data analysis",
            "pandas",
            "numpy",
            "statistics"
        ]
    }

    predictions = {}

    skills = set(skill.lower() for skill in skills)

    for role, required_skills in role_database.items():
        matched = len(skills.intersection(set(required_skills)))
        score = int((matched / len(required_skills)) * 100)
        predictions[role] = score

    return dict(
        sorted(
            predictions.items(),
            key=lambda x: x[1],
            reverse=True
        )
    )