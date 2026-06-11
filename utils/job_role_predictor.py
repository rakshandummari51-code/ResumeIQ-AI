def predict_roles(skills):

    role_database = {
        "AI Engineer": [
            "python",
            "machine learning",
            "artificial intelligence",
            "computer vision",
            "opencv",
            "yolov8",
            "object detection",
            "fastapi"
        ],

        "Data Scientist": [
            "python",
            "sql",
            "machine learning",
            "data analysis",
            "data visualization",
            "statistics",
            "pandas",
            "numpy"
        ],

        "Data Analyst": [
            "sql",
            "excel",
            "python",
            "data analysis",
            "data visualization",
            "power bi"
        ],

        "Machine Learning Engineer": [
            "python",
            "machine learning",
            "computer vision",
            "opencv",
            "yolov8",
            "scikit-learn",
            "deep learning"
        ],

        "Backend Developer": [
            "python",
            "java",
            "sql",
            "fastapi",
            "git"
        ]
    }

    skills = set(skill.lower() for skill in skills)

    predictions = {}

    for role, required_skills in role_database.items():

        matched = len(
            skills.intersection(set(required_skills))
        )

        base_score = int(
            (matched / len(required_skills)) * 100
        )
 
        role_weights = {
            "AI Engineer": 1.20,
            "Data Scientist": 1.15,
            "Data Analyst": 1.05,
            "Machine Learning Engineer": 1.10,
            "Backend Developer": 0.80
        }

        score = int(
            base_score * role_weights.get(role, 1)
        )

        score = min(score, 100)

        predictions[role] = score

    return dict(
        sorted(
            predictions.items(),
            key=lambda x: x[1],
            reverse=True
        )
    )