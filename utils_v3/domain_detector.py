def detect_domain(text):

    text = text.lower()

    domains = {

        "Data Science": [
            "machine learning",
            "data science",
            "data analysis",
            "pandas",
            "numpy",
            "statistics",
            "power bi",
            "tableau"
        ],

        "Software Development": [
            "java",
            "python",
            "javascript",
            "react",
            "html",
            "css",
            "backend",
            "frontend"
        ],

        "Medicine": [
            "mbbs",
            "patient care",
            "clinical",
            "diagnosis",
            "hospital",
            "medical"
        ],

        "Mechanical Engineering": [
            "autocad",
            "solidworks",
            "manufacturing",
            "thermodynamics",
            "cad"
        ],

        "Civil Engineering": [
            "structural",
            "construction",
            "surveying",
            "autocad civil",
            "civil engineering"
        ],

        "Electronics & Communication": [
            "embedded systems",
            "vlsi",
            "electronics",
            "microcontroller",
            "iot"
        ],

        "Business & Management": [
            "marketing",
            "operations",
            "business strategy",
            "management",
            "mba"
        ],

        "Commerce & Finance": [
            "accounting",
            "finance",
            "taxation",
            "auditing",
            "investment"
        ],

        "Law": [
            "legal",
            "litigation",
            "law",
            "advocate",
            "corporate law"
        ]
    }

    scores = {}

    for domain, keywords in domains.items():

        score = 0

        for keyword in keywords:

            if keyword in text:
                score += 1

        scores[domain] = score

    best_domain = max(
        scores,
        key=scores.get
    )

    confidence = int(
        (scores[best_domain] / max(len(domains[best_domain]), 1))
        * 100
    )

    return {
        "domain": best_domain,
        "confidence": confidence
    }