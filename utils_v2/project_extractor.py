def extract_projects_v2(text):

    lines = text.split("\n")
    projects = []

    inside_projects = False

    project_headings = [
        "projects",
        "academic projects",
        "personal projects",
        "major projects",
        "mini projects",
        "project work"
    ]

    stop_sections = [
        "certifications",
        "experience",
        "education",
        "technical skills",
        "skills",
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
        

        # Start project section
        if any(
            heading == line_lower
            for heading in project_headings
        ):
            inside_projects = True
            continue

        if inside_projects:

            # Stop only if line IS a section heading
            if any(
                section == line_lower
                for section in stop_sections
            ):
                break

            # Project title line
            if "|" in clean_line:

                project_name = (
                    clean_line.split("|")[0]
                    .strip()
                )

                projects.append({
                    "name": project_name
                })

    return projects