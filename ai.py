# MOCK AI
def analyze_resume(resume_text, user_goal):

    text = resume_text.lower()

    skills = []

    if "python" in text:
        skills.append("Python")
    if "flask" in text:
        skills.append("Flask")
    if "java" in text:
        skills.append("Java")
    if "sql" in text:
        skills.append("SQL")

    if not skills:
        skills = ["Basic Programming"]

    return {
        "skills": skills,
        "missing_skills": [
            "Data Structures & Algorithms",
            "System Design"
        ],
        "roadmap": [
            f"Focus on {user_goal}",
            "Build projects",
            "Practice DSA",
            "Learn APIs"
        ],
        "interview_questions": [
            "What is REST API?",
            "Explain GET vs POST",
            "What is OOP?",
            "Tell about your project"
        ]
    }