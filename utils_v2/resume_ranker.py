def get_resume_rank(ats_score):

    if ats_score >= 80:
        return (
            "🏆 Interview Ready",
            "Your resume demonstrates strong technical skills, relevant experience, impactful projects, and industry-aligned qualifications. You are well-positioned for interviews and competitive job opportunities."
        )

    elif ats_score >= 60:
        return (
            "🥇 Strong Candidate",
            "Your profile is competitive and shows solid skills, projects, and experience. Strengthening a few key areas such as advanced projects, certifications, or domain expertise can further improve your job readiness."
        )

    elif ats_score >= 40:
        return (
            "🥈 Developing Candidate",
            "You have a good foundation, but there are noticeable gaps in skills, projects, experience, or resume quality. Focus on building practical projects, gaining certifications, and improving alignment with your target role."
        )

    else:
        return (
            "🥉 Beginner",
            "Your resume is currently at an early stage. Start by developing core skills, creating hands-on projects, earning relevant certifications, and improving the overall structure of your resume."
        )