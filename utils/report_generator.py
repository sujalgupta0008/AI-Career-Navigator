from datetime import datetime


def create_text_report(name, target_role, ai_report, skill_score, matched_skills, missing_skills):
    report = f"""
AI Career Navigator Report
Generated On: {datetime.now().strftime("%d %B %Y, %I:%M %p")}

Student Name: {name}
Target Role: {target_role}

Skill Readiness Score: {skill_score}/100

Matched Skills:
{", ".join(matched_skills) if matched_skills else "No matched skills found"}

Missing Skills:
{", ".join(missing_skills) if missing_skills else "No missing skills found"}

--------------------------------------------------

AI Career Analysis:

{ai_report}
"""
    return report 