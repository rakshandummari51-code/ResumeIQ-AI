def extract_certifications(text):

    lines = text.split("\n")
    certifications = []

    certification_headings = [
        "certifications",
        "certificates",
        "licenses",
        "licenses & certifications",
        "courses",
        "training",
        "professional development"
    ]

    stop_sections = [
        "projects",
        "project",
        "experience",
        "work experience",
        "internships",
        "education",
        "skills",
        "technical skills",
        "achievements",
        "career objective",
        "professional summary",
        "summary"
    ]

    inside_certifications = False

    for line in lines:

        clean_line = (
            line.replace("", "")
                .replace("", "")
                .replace("•", "")
                .strip()
        )

        if not clean_line:
            continue

        line_lower = clean_line.lower()

        if line_lower in certification_headings:
            inside_certifications = True
            continue

        if inside_certifications:

            if line_lower in stop_sections:
                break

            if clean_line.endswith("."):
                continue

            certifications.append(clean_line)

    return certifications