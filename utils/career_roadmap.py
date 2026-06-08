def generate_career_roadmap(top_role):

    roadmaps = {
        "Backend Developer": {
            "skills": [
                "Docker",
                "AWS",
             "System Design",
            "REST API Development",
            "Database Optimization"
            ],
            "projects": [
                "E-commerce Backend API",
                "URL Shortener Service",
                "Authentication System",
                "Chat Application Backend"
            ]
        },

        "AI Engineer": {
            "skills": [
                "Machine Learning",
                "Deep Learning",
                "TensorFlow",
                "PyTorch",
                "MLOps"
            ],
            "projects": [
                "Resume Screening AI",
                "Object Detection System",
                "AI Chatbot",
                "Image Classification App"
            ]
        },
        "Machine Learning Engineer": {
            "skills": [
                "Machine Learning",
                "Scikit-Learn",
                "Model Deployment",
                "Feature Engineering",
                "MLOps"
            ],
            "projects": [
                "Credit Card Fraud Detection",
                "Movie Recommendation System",
                "Customer Churn Prediction",
                "ML Model Deployment API"
            ]
        },

        "Data Scientist": {
            "skills": [
                "Statistics",
                "Pandas",
                "NumPy",
                "Data Visualization",
                "Machine Learning"
            ],
            "projects": [
                "Sales Forecasting Dashboard",
                "Customer Segmentation",
                "Exploratory Data Analysis Project",
                "Predictive Analytics System"
            ]
        },

        "Data Analyst": {
            "skills": [
                "Power BI",
                "Tableau",
                "Excel",
                "SQL",
                "Data Visualization"
            ],
            "projects": [
                "Sales Dashboard",
                "HR Analytics Dashboard",
                "Financial Analysis Report",
                "Customer Insights Dashboard"
            ]
        }
    }

    return roadmaps.get(
        top_role,
        {
            "skills": [
                "Communication",
                "Problem Solving",
                "Project Building",
                "GitHub Portfolio"
            ],
            "projects": [
                "Portfolio Website",
                "Domain-Specific Project",
                "Research-Based Project"
            ]
        }
    )