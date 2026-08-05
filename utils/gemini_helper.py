import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import errors as genai_errors

load_dotenv()

# Works locally (.env file) AND on Streamlit Community Cloud (st.secrets)
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    try:
        import streamlit as st
        api_key = st.secrets.get("GEMINI_API_KEY")
    except Exception:
        pass

client = genai.Client(api_key=api_key)


def _generate_with_retry(prompt, retries=2, delay=4):
    """
    Calls Gemini and retries on transient 503 (overloaded) errors.
    Raises a clean RuntimeError with a friendly message if it still fails.
    """
    last_error = None

    for attempt in range(retries + 1):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            return response.text
        except genai_errors.ServerError as e:
            last_error = e
            if attempt < retries:
                time.sleep(delay)
                continue
        except genai_errors.ClientError as e:
            raise RuntimeError(
                "Gemini API rejected the request — check that GEMINI_API_KEY "
                "in your .env file is a valid Google AI Studio key."
            ) from e

    raise RuntimeError(
        "Gemini is currently overloaded (503). This is temporary on Google's "
        "side — please try again in a minute."
    ) from last_error


def generate_career_plan(profile):
    prompt = f"""
You are an expert career mentor, data analytics recruiter, and hackathon project evaluator.

Analyze this student profile:

Name: {profile['name']}
Degree: {profile['degree']}
Year: {profile['year']}
Target Role: {profile['target_role']}
Current Skills: {profile['skills']}
Projects: {profile['projects']}
Career Goal: {profile['career_goal']}

Generate a structured career report.

Use this exact format:

## 1. Career Fit Score
Give score out of 10 and explain why.

## 2. Best-Fit Roles
Suggest 3 roles with reason.

## 3. Current Strengths
List the strongest points.

## 4. Missing Technical Skills
List important missing skills for the target role.

## 5. Missing Soft Skills
List important soft skills.

## 6. Resume Improvement Suggestions
Give practical resume changes.

## 7. LinkedIn Improvement Suggestions
Give practical LinkedIn profile suggestions.

## 8. GitHub Improvement Suggestions
Give practical GitHub improvement suggestions.

## 9. 30-Day Learning Roadmap
Give week-wise roadmap.

## 10. Resume-Worthy Project Ideas
Suggest 3 projects with title, problem, dataset idea, tech stack, and output.

## 11. Interview Preparation Questions
Give 10 questions.

## 12. Final Action Plan
Give a clear next-step action plan.

Make the answer practical, specific, and internship-focused.
Do not give generic motivation.
"""

    return _generate_with_retry(prompt)


def generate_jd_match_analysis(profile, job_description):
    prompt = f"""
You are an expert ATS resume evaluator and technical recruiter.

Compare this student profile with the given job description.

Student Profile:
Name: {profile['name']}
Degree: {profile['degree']}
Year: {profile['year']}
Target Role: {profile['target_role']}
Skills: {profile['skills']}
Projects: {profile['projects']}
Career Goal: {profile['career_goal']}

Job Description:
{job_description}

Generate a structured JD match report with:

## 1. JD Match Score
Give score out of 100.

## 2. Matched Skills
List skills from the student profile that match the JD.

## 3. Missing Skills
List important JD skills missing from the profile.

## 4. Missing Keywords for Resume
List keywords that should be added to resume if genuinely known.

## 5. Project Alignment
Explain which projects match the JD.

## 6. Resume Improvement Suggestions
Give specific bullet points to improve resume for this JD.

## 7. Interview Focus Areas
List topics the student should prepare.

## 8. Final Recommendation
Say whether the student should apply now, apply after improvement, or not apply.

Keep the answer practical, honest, and internship-focused.
"""

    return _generate_with_retry(prompt)