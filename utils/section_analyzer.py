def analyze_sections(resume_text):

    text = resume_text.lower()

    scores = {}

    # Education
    education_score = 0

    if any(word in text for word in [
        "education",
        "degree",
        "college",
        "university",
        "b.tech",
        "bachelor"
    ]):
        education_score += 70

    if "%" in text or "cgpa" in text:
        education_score += 20

    scores["Education"] = min(education_score, 100)

    # Projects
    project_keywords = [
        "project",
        "projects",
        "developed",
        "built",
        "designed",
        "implemented"
    ]

    project_count = sum(text.count(word) for word in project_keywords)

    scores["Projects"] = min(project_count * 15, 100)

    # Skills
    skill_keywords = [
        "python",
        "java",
        "sql",
        "html",
        "css",
        "javascript",
        "git",
        "github",
        "opencv",
        "fastapi",
        "yolov8"
    ]

    skill_count = sum(1 for skill in skill_keywords if skill in text)

    scores["Skills"] = min(skill_count * 10, 100)

    # Certifications
    certification_score = 0

    if any(word in text for word in [
        "certificate",
        "certificates",
        "certification",
        "certifications"
    ]):
        certification_score += 70

    scores["Certifications"] = min(certification_score, 100)

    # Experience
    experience_score = 0

    if any(word in text for word in [
        "experience",
        "internship",
        "worked",
        "employment"
    ]):
        experience_score += 70

    scores["Experience"] = min(experience_score, 100)

    return scores