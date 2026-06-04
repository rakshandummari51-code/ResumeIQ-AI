def calculate_ats_score(
    match_score,
    section_scores,
    resume_strength,
    missing_skills
):

    # Section Average
    section_average = (
        sum(section_scores.values())
        / len(section_scores)
    )

    # Missing Skills Penalty
    penalty = min(len(missing_skills) * 2, 20)

    ats_score = (
        (match_score * 0.5)
        + (section_average * 0.3)
        + (resume_strength * 0.2)
        - penalty
    )

    return max(0, min(int(ats_score), 100))