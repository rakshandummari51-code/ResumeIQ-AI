SKILL_ALIASES = {
    "ml": "machine learning",
    "ai": "artificial intelligence",
    "js": "javascript",
    "react.js": "react",
    "node.js": "nodejs",
    "node js": "nodejs",
    "scikit learn": "scikit-learn",
    "sklearn": "scikit-learn",
    "powerbi": "power bi",
    "ms excel": "excel",
    "github": "git",
    "opencv": "computer vision",
    "cv": "computer vision",
    "yolov8": "object detection",
    "yolo": "object detection",
    "tensorflow": "deep learning",
    "pytorch": "deep learning",
    "keras": "deep learning",
    "nlp": "natural language processing"
}


def normalize_skill(skill):
    skill = skill.lower().strip()
    return SKILL_ALIASES.get(skill, skill)


def normalize_skills(skills):
    normalized = []

    for skill in skills:
        normalized.append(normalize_skill(skill))

    return sorted(list(set(normalized)))