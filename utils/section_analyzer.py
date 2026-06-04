def analyze_sections(resume_text):

    text = resume_text.lower()

    sections = {
        "Education": False,
        "Projects": False,
        "Skills": False,
        "Certifications": False,
        "Experience": False
    }

    # Education
    if any(word in text for word in [
        "education",
        "b.tech",
        "bachelor",
        "degree",
        "college",
        "university"
    ]):
        sections["Education"] = True

    # Projects
    if any(word in text for word in [
        "project",
        "projects",
        "developed",
        "built"
    ]):
        sections["Projects"] = True

    # Skills
    if any(word in text for word in [
        "skills",
        "python",
        "java",
        "sql",
        "javascript"
    ]):
        sections["Skills"] = True

    # Certifications
    if any(word in text for word in [
        "certificate",
        "certification",
        "certifications"
    ]):
        sections["Certifications"] = True

    # Experience
    if any(word in text for word in [
        "experience",
        "internship",
        "worked",
        "employment"
    ]):
        sections["Experience"] = True

    return sections