def extract_skills(text):

    skills_db = [

        # Programming Languages
        "python",
        "java",
        "c++",
        "javascript",
        "typescript",
        "php",
        "go",
        "rust",

        # Web Development
        "html",
        "css",
        "react",
        "angular",
        "vue",
        "node.js",
        "express",
        "django",
        "flask",
        "fastapi",

        # Databases
        "sql",
        "mysql",
        "postgresql",
        "mongodb",
        "sqlite",

        # Data Science
        "pandas",
        "numpy",
        "scikit-learn",
        "machine learning",
        "deep learning",
        "statistics",
        "data analysis",
        "data visualization",
        "nlp",

        # AI & Computer Vision
        "tensorflow",
        "pytorch",
        "keras",
        "opencv",
        "computer vision",
        "yolov8",
        "object detection",
        "face recognition",

        # Business Intelligence
        "power bi",
        "tableau",
        "excel",

        # Cloud
        "aws",
        "azure",
        "gcp",

        # DevOps
        "docker",
        "kubernetes",
        "jenkins",
        "github actions",

        # Version Control
        "git",
        "github",

        # Mobile Development
        "android",
        "flutter",
        "react native",

        # Cybersecurity
        "network security",
        "penetration testing",
        "ethical hacking",
        "cyber security",

        # Software Engineering
        "data structures",
        "algorithms",
        "oop",
        "object oriented programming",
        "system design",

        # Tools
        "linux",
        "postman",
        "jira"
    ]

    text = text.lower()

    found_skills = []

    for skill in skills_db:
        if skill.lower() in text:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))