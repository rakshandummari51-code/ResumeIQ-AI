from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch


def generate_pdf_report(
    match_score,
    ats_score,
    resume_strength,
    matching_skills,
    missing_skills,
    role_predictions,
    skill_gap_results,
    learning_path,
    ai_recommendations,
    career_roadmap,
    rewrite_suggestions
):

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("ResumeIQ AI Report", styles["Title"]))
    story.append(Spacer(1, 0.25 * inch))

    story.append(Paragraph("Scores", styles["Heading2"]))
    story.append(Paragraph(f"Match Score: {match_score}%", styles["Normal"]))
    story.append(Paragraph(f"ATS Score: {ats_score}%", styles["Normal"]))
    story.append(Paragraph(f"Resume Strength: {resume_strength}%", styles["Normal"]))
    story.append(Spacer(1, 0.2 * inch))

    story.append(Paragraph("Matching Skills", styles["Heading2"]))
    if matching_skills:
        for skill in matching_skills:
            story.append(Paragraph(f"- {str(skill).title()}", styles["Normal"]))
    else:
        story.append(Paragraph("No matching skills found.", styles["Normal"]))

    story.append(Spacer(1, 0.2 * inch))

    story.append(Paragraph("Missing Skills", styles["Heading2"]))
    if missing_skills:
        for skill in missing_skills:
            story.append(Paragraph(f"- {str(skill).title()}", styles["Normal"]))
    else:
        story.append(Paragraph("No missing skills found.", styles["Normal"]))

    story.append(Spacer(1, 0.2 * inch))

    story.append(Paragraph("Predicted Career Paths", styles["Heading2"]))
    for role, role_score in list(role_predictions.items())[:5]:
        story.append(Paragraph(f"- {role}: {role_score}%", styles["Normal"]))

    story.append(Spacer(1, 0.2 * inch))

    story.append(Paragraph("Skill Gap Analysis", styles["Heading2"]))
    if skill_gap_results:
        for item in skill_gap_results:
            story.append(
                Paragraph(
                    f"- {item['skill']}: {item['priority']}",
                    styles["Normal"]
                )
            )
    else:
        story.append(Paragraph("No major skill gaps detected.", styles["Normal"]))

    story.append(Spacer(1, 0.2 * inch))

    story.append(Paragraph("Recommended Learning Path", styles["Heading2"]))
    if learning_path:
        for i, skill in enumerate(learning_path[:5], start=1):
            story.append(Paragraph(f"{i}. {skill}", styles["Normal"]))
    else:
        story.append(Paragraph("No learning path required.", styles["Normal"]))

    story.append(Spacer(1, 0.2 * inch))

    story.append(Paragraph("AI Resume Recommendations", styles["Heading2"]))
    if ai_recommendations:
        for recommendation in ai_recommendations:
            story.append(Paragraph(recommendation["section"], styles["Heading3"]))

            for advice in recommendation["advice"]:
                story.append(Paragraph(f"- {advice}", styles["Normal"]))
    else:
        story.append(Paragraph("No major recommendations detected.", styles["Normal"]))

    story.append(Spacer(1, 0.2 * inch))

    story.append(Paragraph("Career Roadmap", styles["Heading2"]))

    story.append(Paragraph("Skills To Learn", styles["Heading3"]))
    for skill in career_roadmap["skills"]:
        story.append(Paragraph(f"- {skill}", styles["Normal"]))

    story.append(Paragraph("Projects To Build", styles["Heading3"]))
    for project in career_roadmap["projects"]:
        story.append(Paragraph(f"- {project}", styles["Normal"]))

    story.append(Spacer(1, 0.2 * inch))

    story.append(Paragraph("Resume Rewrite Suggestions", styles["Heading2"]))

    if rewrite_suggestions:
        for item in rewrite_suggestions:
            story.append(Paragraph(f"Weak: {item['weak']}", styles["Normal"]))
            story.append(Paragraph(f"Better: {item['better']}", styles["Normal"]))
            story.append(Spacer(1, 0.1 * inch))
    else:
        story.append(Paragraph("No rewrite suggestions found.", styles["Normal"]))

    doc.build(story)

    buffer.seek(0)
    return buffer