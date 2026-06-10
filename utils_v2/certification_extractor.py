def extract_certifications(text):

    lines = text.split("\n")
    certifications = []

    inside_certifications = False

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

    for line in lines:

        clean_line = (
            line.replace("", "")
                .replace("", "")
                .strip()
        )

        if not clean_line:
            continue

        line_lower = clean_line.lower()

        # Start Certification Section
        if any(
            heading in line_lower
            for heading in certification_headings
        ):
            inside_certifications = True
            continue

        # Read Certifications
        if inside_certifications:

            # Stop when next section starts
            if any(
                section in line_lower
                for section in stop_sections
            ):
                break

            certifications.append(clean_line)

    return certifications