def generate_rewrite_suggestions(resume_text):

    text = resume_text.lower()

    suggestions = []

    if "project" in text or "projects" in text:
        suggestions.append({
            "weak": "Worked on a project.",
            "better": "Developed a complete project with clear problem statement, technologies used, implementation details, and measurable outcomes."
        })

    if "attendance" in text:
        suggestions.append({
            "weak": "Built a smart attendance system.",
            "better": "Developed an AI-based Smart Attendance System using Python, OpenCV, FastAPI, and face recognition to automate real-time attendance tracking."
        })

    if "yolov8" in text or "object detection" in text:
        suggestions.append({
            "weak": "Built an object detection project.",
            "better": "Built a real-time object detection system using YOLOv8 with data preprocessing, annotation, model training, and performance optimization."
        })

    if "python" in text:
        suggestions.append({
            "weak": "Skilled in Python.",
            "better": "Proficient in Python for backend development, automation, data processing, and AI-based application development."
        })

    if "sql" in text:
        suggestions.append({
            "weak": "Know SQL.",
            "better": "Experienced in SQL for database management, querying, and structured data handling."
        })

    if not suggestions:
        suggestions.append({
            "weak": "Resume content is too general.",
            "better": "Use action verbs, mention technologies clearly, and add measurable project outcomes to make your resume stronger."
        })

    return suggestions