def extract_experience(text):

    lines = text.split("\n")
    experiences = []

    inside_experience = False

    experience_headings = [
        "experience",
        "work experience",
        "internships",
        "internship",
        "professional experience"
    ]

    stop_sections = [
        "projects",
        "certifications",
        "education",
        "skills",
        "technical skills",
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

        if any(
            heading == line_lower
            for heading in experience_headings
        ):
            inside_experience = True
            continue

        if inside_experience:

            if any(
                section == line_lower
                for section in stop_sections
            ):
                break

            if (
                "intern" in line_lower
                or "virtual" in line_lower
            ):
                experiences.append(clean_line)

    return experiences