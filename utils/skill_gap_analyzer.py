def analyze_skill_gaps(missing_skills):

    high_priority = {
        "python",
        "sql",
        "aws",
        "docker",
        "machine learning",
        "deep learning",
        "javascript",
        "react",
        "fastapi"
    }

    medium_priority = {
        "kubernetes",
        "tensorflow",
        "pytorch",
        "computer vision",
        "natural language processing",
        "power bi",
        "excel"
    }

    results = []

    for skill in missing_skills:

        skill_lower = skill.lower()

        if skill_lower in high_priority:
            priority = "🔥 High"

        elif skill_lower in medium_priority:
            priority = "⚡ Medium"

        else:
            priority = "🟢 Low"

        results.append({
            "skill": skill.title(),
            "priority": priority
        })

    return results


def generate_learning_path(skill_gap_results):

    priority_order = {
        "🔥 High": 1,
        "⚡ Medium": 2,
        "🟢 Low": 3
    }

    sorted_skills = sorted(
        skill_gap_results,
        key=lambda x: priority_order[x["priority"]]
    )

    return [
        item["skill"]
        for item in sorted_skills
    ]