def extract_education(text):

    lines = text.split("\n")
    education = []

    inside_education = False

    education_headings = [
        "education",
        "academic background",
        "qualification",
        "qualifications"
    ]

    stop_sections = [
        "skills",
        "technical skills",
        "projects",
        "experience",
        "internships",
        "certifications",
        "certificates",
        "achievements",
        "hobbies",
        "summary"
    ]

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

        if any(heading == line_lower for heading in education_headings):
            inside_education = True
            continue

        if inside_education:

            if any(section == line_lower for section in stop_sections):
                break

            if (
                "b.tech" in line_lower
                or "bachelor" in line_lower
                or "computer science" in line_lower
                or "data science" in line_lower
                or "college" in line_lower
                or "university" in line_lower
                or "institute" in line_lower
            ):
                education.append(clean_line)

    return education