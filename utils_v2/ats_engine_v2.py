def calculate_ats_score_v2(
    match_score,
    project_analysis,
    experience_analysis,
    certification_analysis,
    education_analysis,
    section_scores,
    missing_skills
):

    # -----------------------
    # SKILLS SCORE: 30 marks
    # -----------------------
    skills_score = int(match_score * 0.30)

    # -----------------------
    # PROJECT SCORE: 20 marks
    # -----------------------
    if project_analysis:
        avg_project_score = sum(
            project["impact_score"]
            for project in project_analysis
        ) / len(project_analysis)

        project_score = int(avg_project_score * 2)
    else:
        project_score = 0

    # -----------------------
    # EXPERIENCE SCORE: 15 marks
    # -----------------------
    if experience_analysis:
        avg_exp_score = sum(
            exp["score"]
            for exp in experience_analysis
        ) / len(experience_analysis)

        experience_score = int(avg_exp_score * 1.5)
    else:
        experience_score = 0

    # -----------------------
    # CERTIFICATION SCORE: 10 marks
    # -----------------------
    if certification_analysis:
        avg_cert_score = sum(
            cert["score"]
            for cert in certification_analysis
        ) / len(certification_analysis)

        certification_score = int(avg_cert_score)
    else:
        certification_score = 0

    # -----------------------
    # EDUCATION SCORE: 10 marks
    # -----------------------
    if education_analysis:
        education_score = 10
    else:
        education_score = 0

    # -----------------------
    # SECTION QUALITY: 10 marks
    # -----------------------
    if section_scores:
        section_average = (
            sum(section_scores.values())
            / len(section_scores)
        )

        section_score = int(section_average * 0.10)
    else:
        section_score = 0

    # -----------------------
    # MISSING SKILLS PENALTY: max 5
    # -----------------------
    penalty = min(len(missing_skills), 5)

    final_score = (
        skills_score
        + project_score
        + experience_score
        + certification_score
        + education_score
        + section_score
        - penalty
    )

    final_score = max(0, min(final_score, 100))

    breakdown = {
        "Skills Match": skills_score,
        "Projects": project_score,
        "Experience": experience_score,
        "Certifications": certification_score,
        "Education": education_score,
        "Section Quality": section_score,
        "Missing Skills Penalty": -penalty,
        "Final ATS Score V2": final_score
    }

    return final_score, breakdown