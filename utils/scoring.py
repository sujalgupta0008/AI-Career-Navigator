def calculate_skill_score(skills, target_role):
    skills_lower = skills.lower()

    role_skills = {
        "Data Analyst": [
            "python", "sql", "excel", "power bi", "statistics",
            "pandas", "numpy", "matplotlib", "dashboard", "data cleaning"
        ],
        "Data Scientist": [
            "python", "sql", "statistics", "machine learning", "pandas",
            "numpy", "scikit-learn", "matplotlib", "feature engineering", "model"
        ],
        "Business Analyst": [
            "excel", "sql", "power bi", "communication", "requirement",
            "dashboard", "business", "presentation", "stakeholder", "analysis"
        ],
        "GenAI Engineer": [
            "python", "api", "llm", "gemini", "prompt engineering",
            "streamlit", "rag", "langchain", "vector database", "github"
        ],
        "Software Developer": [
            "python", "java", "dsa", "oop", "git", "github",
            "database", "api", "web development", "debugging"
        ]
    }

    required = role_skills.get(target_role, [])
    matched = []

    for skill in required:
        if skill in skills_lower:
            matched.append(skill)

    score = int((len(matched) / len(required)) * 100) if required else 0
    missing = [skill for skill in required if skill not in matched]

    return score, matched, missing 