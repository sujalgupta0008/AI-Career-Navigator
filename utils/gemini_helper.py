"""
Groq AI Helper - Ultra-Fast Free LLM API
Uses FREE models: LLaMA 3.1, Mixtral, Gemma
10x faster than OpenRouter, completely free, no 404 errors!
"""

import os
import time
from dotenv import load_dotenv

load_dotenv()
_api_key = None
_configured = False


def _ensure_groq_config():
    """Ensure Groq API key is configured from env or Streamlit secrets."""
    global _api_key, _configured

    if _configured:
        return

    # Priority 1: Environment variable (.env file)
    _api_key = os.getenv("GROQ_API_KEY")

    # Priority 2: Streamlit secrets
    if not _api_key:
        try:
            import streamlit as st
            if hasattr(st, "secrets") and st.secrets is not None:
                _api_key = st.secrets.get("GROQ_API_KEY")
        except Exception:
            pass

    if not _api_key or _api_key == "your_groq_api_key_here":
        raise RuntimeError(
            "❌ Groq API key not configured!\n\n"
            "Quick Setup (2 minutes):\n"
            "1. Go to: https://console.groq.com\n"
            "2. Sign up (FREE, no credit card needed)\n"
            "3. Click 'API Keys' → 'Create API Key'\n"
            "4. Copy your API key\n"
            "5. Paste in .env file: GROQ_API_KEY=your_key_here\n"
            "6. Restart the app\n\n"
            "🚀 Groq is 10x faster than other APIs and completely FREE!"
        )

    _configured = True


def _generate_with_retry(prompt, retries=2, delay=2, max_tokens=2000):
    """
    Calls Groq API with intelligent retry logic.
    Groq is ULTRA-FAST, so this will complete in seconds.
    
    Args:
        prompt: User prompt to send
        retries: Number of retry attempts (default: 2)
        delay: Wait time between retries in seconds (default: 2)
        max_tokens: Maximum tokens in response (default: 2000)
    
    Returns:
        str: Generated response text
    """
    _ensure_groq_config()
    
    try:
        from groq import Groq
    except ImportError:
        raise RuntimeError(
            "❌ Groq Python SDK not installed!\n\n"
            "Fix: Run this in terminal:\n"
            "pip install groq\n\n"
            "Then restart the app."
        )

    last_error = None

    # ✅ FASTEST FREE MODELS on Groq
    models_to_try = [
        "mixtral-8x7b-32768",           # ⭐ Fast & powerful
        "llama-3.1-70b-versatile",      # ⭐ Most capable
        "llama-3.1-8b-instant",         # ⭐ Ultra-fast fallback
    ]

    client = Groq(api_key=_api_key)

    for attempt in range(retries + 1):
        for model_name in models_to_try:
            try:
                # Call Groq API (SUPER FAST!)
                message = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model=model_name,
                    temperature=0.7,
                    max_tokens=max_tokens,
                    timeout=30  # Groq is so fast, 30s is plenty
                )

                # Extract response
                if message.choices and len(message.choices) > 0:
                    return message.choices[0].message.content

            except Exception as e:
                last_error = e
                error_msg = str(e).lower()
                
                # Only retry on specific errors
                if "rate" in error_msg or "timeout" in error_msg:
                    if attempt < retries:
                        time.sleep(delay)
                        break  # Try next attempt
                
                # For other errors, try next model
                continue

    # All attempts failed
    raise RuntimeError(
        f"❌ Groq API Error!\n\n"
        f"Last error: {last_error}\n\n"
        f"Troubleshooting:\n"
        f"✓ Check your internet connection\n"
        f"✓ Verify API key: https://console.groq.com/account/keys\n"
        f"✓ Check Groq status: https://status.groq.com\n"
        f"✓ Wait 1-2 seconds and try again\n\n"
        f"Groq is usually instant, if it's slow your connection may have issues."
    ) from last_error


def generate_career_plan(profile):
    """
    Generate comprehensive career plan for a student using Groq (ULTRA-FAST!).
    
    Args:
        profile (dict): Student profile with keys:
            - name, degree, year, target_role, skills, projects, career_goal
    
    Returns:
        str: Formatted career analysis report
    """
    prompt = f"""You are an expert career mentor, data analytics recruiter, and hackathon project evaluator.

Analyze this student profile:

Name: {profile['name']}
Degree: {profile['degree']}
Year: {profile['year']}
Target Role: {profile['target_role']}
Current Skills: {profile['skills']}
Projects: {profile['projects']}
Career Goal: {profile['career_goal']}

Generate a structured career report using this EXACT format:

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

Make the answer practical, specific, and internship-focused."""

    return _generate_with_retry(prompt, max_tokens=2000)


def generate_jd_match_analysis(profile, job_description):
    """
    Analyze how well a student profile matches a job description using Groq.
    
    Args:
        profile (dict): Student profile
        job_description (str): Full job description text
    
    Returns:
        str: Formatted JD match analysis report
    """
    prompt = f"""You are an expert ATS resume evaluator and technical recruiter.

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

Generate a structured JD match report using this EXACT format:

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

Keep the answer practical, honest, and internship-focused."""

    return _generate_with_retry(prompt, max_tokens=2500)