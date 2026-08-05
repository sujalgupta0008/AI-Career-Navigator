import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utils.gemini_helper import generate_career_plan, generate_jd_match_analysis
from utils.scoring import calculate_skill_score
from utils.report_generator import create_text_report

from utils.theme import (
    inject_theme,
    readiness_console,
    render_report_sections,
    score_gauge,
    parse_report_sections,
    extract_first_number,
)

st.set_page_config(
    page_title="AI Career Navigator",
    page_icon="🎯",
    layout="wide"
)

inject_theme()

st.markdown(
    """
    <div style="margin-bottom:6px;">
        <span style="font-family:'IBM Plex Mono';font-size:11px;letter-spacing:0.08em;
            color:var(--mint);text-transform:uppercase;border:1px solid rgba(61,220,151,0.3);
            background:rgba(61,220,151,0.06);padding:5px 12px;border-radius:99px;">
            ● Powered by Gemini AI
        </span>
    </div>
    <h1 style="font-family:'Space Grotesk';font-size:38px;margin:12px 0 4px;">
        🎯 AI Career Navigator
    </h1>
    <p style="color:var(--text-muted);font-size:15px;max-width:600px;margin-bottom:28px;">
        AI-powered career guidance platform for students and early-career professionals.
    </p>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.header("Student Profile")

    sample = st.button("Use Sample Profile")

    if sample:
        st.session_state["name"] = "Sujal Gupta"
        st.session_state["degree"] = "B.Sc CSDA IIT Patna + B.Tech CSE AKTU"
        st.session_state["year"] = "3rd Year"
        st.session_state["target_role"] = "Data Analyst"
        st.session_state["skills"] = (
            "Python, SQL, Excel, Power BI, DAX, Power Query, "
            "Pandas, NumPy, Matplotlib, Scikit-learn, Streamlit, "
            "Statistics, Probability, Hypothesis Testing, "
            "Exploratory Data Analysis (EDA), Data Cleaning, "
            "Data Visualization, Data Modeling, Dashboard Development, "
            "Business Intelligence, Machine Learning, "
            "Supervised Learning, Unsupervised Learning, "
            "Regression, Classification, Clustering, "
            "Feature Engineering, Model Evaluation, "
            "Jupyter Notebook, Google Colab, Git, GitHub, "
            "VS Code, ETL, Data Warehousing"
        )
        st.session_state["projects"] = (
            "Flight Price Prediction, "
            "Sales Analytics Dashboard, "
            "SmartLend Loan Eligibility Analysis, "
            "LinkedIn Job Posting Analysis, "
            "Fraud Detection System, "
            "Insurance Claim Analysis, "
            "AI Career Navigator"
        )
        st.session_state["career_goal"] = (
            "I want to become a Data Analyst and secure a top Data Analytics internship."
        )
        st.session_state["job_description"] = (
            "We are looking for a Data Analyst Intern with knowledge of SQL, Python, Excel, "
            "Power BI, data cleaning, dashboard creation, statistics, and business insights. "
            "The candidate should be able to analyze datasets, prepare reports, and communicate "
            "findings clearly."
        )

    name = st.text_input("Name", value=st.session_state.get("name", ""))
    degree = st.text_input("Degree / Course", value=st.session_state.get("degree", ""))

    year_options = ["1st Year", "2nd Year", "3rd Year", "4th Year", "Graduate"]
    default_year = st.session_state.get("year", "3rd Year")

    if default_year not in year_options:
        default_year = "3rd Year"

    year = st.selectbox(
        "Current Year",
        year_options,
        index=year_options.index(default_year)
    )

    role_options = [
        "Data Analyst",
        "Data Scientist",
        "Business Analyst",
        "GenAI Engineer",
        "Software Developer"
    ]

    default_role = st.session_state.get("target_role", "Data Analyst")

    if default_role not in role_options:
        default_role = "Data Analyst"

    target_role = st.selectbox(
        "Target Role",
        role_options,
        index=role_options.index(default_role)
    )


st.subheader("Profile Details")

skills = st.text_area(
    "Enter your skills",
    value=st.session_state.get("skills", ""),
    placeholder="Example: Python, SQL, Excel, Power BI, Pandas, Statistics",
    height=120
)

projects = st.text_area(
    "Enter your projects",
    value=st.session_state.get("projects", ""),
    placeholder="Example: Fraud Detection, SmartLend, Sales Dashboard",
    height=120
)

career_goal = st.text_area(
    "Career Goal",
    value=st.session_state.get("career_goal", ""),
    placeholder="Example: I want to become a Data Analyst and get an internship.",
    height=100
)

job_description = st.text_area(
    "Paste Job / Internship Description",
    value=st.session_state.get("job_description", ""),
    placeholder="Paste internship or job description here to check your match score.",
    height=150
)


analyze_btn = st.button("🚀 Generate Career Plan")


if analyze_btn:
    if not name or not degree or not skills or not projects or not career_goal:
        st.error("Please fill all required fields before generating the career plan.")
    else:
        profile = {
            "name": name,
            "degree": degree,
            "year": year,
            "target_role": target_role,
            "skills": skills,
            "projects": projects,
            "career_goal": career_goal
        }

        skill_score, matched_skills, missing_skills = calculate_skill_score(
            skills,
            target_role
        )

        with st.spinner("Gemini is analyzing your career profile..."):
            try:
                ai_report = generate_career_plan(profile)
            except RuntimeError as e:
                st.error(str(e))
                st.stop()

        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
            [
                "📊 Score",
                "🧠 AI Report",
                "🛠 Skill Gap",
                "🎯 JD Match",
                "✅ Roadmap Tracker",
                "📥 Download Report"
            ]
        )

        with tab1:
            st.subheader("Career Readiness Dashboard")

            col1, col2 = st.columns([1, 1.3])

            with col1:
                skill_breakdown = {}
                for i, s in enumerate(matched_skills[:4]):
                    skill_breakdown[s] = max(skill_score - i * 6, 35)

                if not skill_breakdown:
                    skill_breakdown = {"Overall": skill_score}

                readiness_console(
                    score=skill_score,
                    role=target_role,
                    skills=skill_breakdown
                )

            with col2:
                m1, m2 = st.columns(2)
                with m1:
                    st.metric("Matched Skills", len(matched_skills))
                with m2:
                    st.metric("Missing Skills", len(missing_skills))

                plt.rcParams.update({
                    "figure.facecolor": "#121826",
                    "axes.facecolor": "#121826",
                    "axes.edgecolor": "#8B93A7",
                    "axes.labelcolor": "#E8ECF4",
                    "text.color": "#E8ECF4",
                    "xtick.color": "#8B93A7",
                    "ytick.color": "#8B93A7",
                    "font.family": "sans-serif",
                })

                fig, ax = plt.subplots(figsize=(6, 3))
                ax.bar(["Skill Readiness"], [skill_score], color="#3DDC97", width=0.4)
                ax.set_ylim(0, 100)
                ax.set_ylabel("Score")
                ax.set_title("Skill Readiness Score", color="#E8ECF4")
                ax.spines[["top", "right"]].set_visible(False)
                for spine in ["left", "bottom"]:
                    ax.spines[spine].set_color("#2A3348")

                st.pyplot(fig)

        with tab2:
            st.subheader("Personalized AI Career Report")
            render_report_sections(ai_report)

        with tab3:
            st.subheader("Skill Gap Analysis")

            max_len = max(len(matched_skills), len(missing_skills), 1)

            matched_list = matched_skills + [""] * (max_len - len(matched_skills))
            missing_list = missing_skills + [""] * (max_len - len(missing_skills))

            df = pd.DataFrame({
                "Matched Skills": matched_list,
                "Missing Skills": missing_list
            })

            st.dataframe(df, use_container_width=True)

        with tab4:
            st.subheader("Job Description Match Analyzer")

            if job_description:
                with st.spinner("Gemini is analyzing your JD match..."):
                    try:
                        jd_report = generate_jd_match_analysis(profile, job_description)
                    except RuntimeError as e:
                        st.error(str(e))
                        st.stop()

                jd_sections = parse_report_sections(jd_report)

                match_score_text = jd_sections[0][2] if jd_sections else jd_report
                match_score = extract_first_number(match_score_text, default="—")

                score_gauge("JD Match Score", match_score, max_score=100, sublabel=target_role)
                render_report_sections(jd_report)

            else:
                st.info("Paste a job or internship description above to get JD match analysis.")

        with tab5:
            st.subheader("30-Day Career Roadmap Tracker")

            st.write("Track your preparation progress for the next 30 days.")

            roadmap_tasks = {
                "Week 1: Foundation": [
                    "Revise Python basics",
                    "Practice SQL SELECT, WHERE, GROUP BY",
                    "Revise Excel formulas and pivot tables",
                    "Understand data cleaning concepts"
                ],
                "Week 2: Analytics Tools": [
                    "Build one Power BI dashboard",
                    "Practice Pandas data analysis",
                    "Create 5 charts using Matplotlib",
                    "Write insights from one dataset"
                ],
                "Week 3: Project Building": [
                    "Improve one existing project",
                    "Add business problem statement",
                    "Add dashboard screenshots",
                    "Upload clean project to GitHub"
                ],
                "Week 4: Resume and Interview": [
                    "Update resume with quantified bullet points",
                    "Improve LinkedIn headline and About section",
                    "Prepare 20 SQL interview questions",
                    "Prepare final project explanation"
                ]
            }

            completed_count = 0
            total_count = 0

            accents = ["var(--mint)", "var(--violet)", "var(--amber)", "var(--mint)"]

            for w_idx, (week, tasks) in enumerate(roadmap_tasks.items()):
                with st.container(border=True):
                    week_completed = 0

                    st.markdown(
                        f"""<span style="font-family:'Space Grotesk';font-weight:600;font-size:15.5px;
                            color:{accents[w_idx % len(accents)]};">{week}</span>""",
                        unsafe_allow_html=True,
                    )
                    st.write("")

                    for t_idx, task in enumerate(tasks):
                        total_count += 1
                        checked = st.checkbox(task, key=f"{week}_{t_idx}")

                        if checked:
                            completed_count += 1
                            week_completed += 1

                    week_progress = week_completed / len(tasks) if tasks else 0
                    st.progress(week_progress)
                    st.caption(f"{week_completed}/{len(tasks)} done this week")

            overall_progress = completed_count / total_count if total_count > 0 else 0

            st.markdown("#### Overall Progress")
            st.progress(overall_progress)
            st.write(f"**{completed_count}/{total_count}** tasks completed across the 30-day plan")

        with tab6:
            st.subheader("Download Career Report")

            report_text = create_text_report(
                name,
                target_role,
                ai_report,
                skill_score,
                matched_skills,
                missing_skills
            )

            if job_description:
                report_text += "\n\n--------------------------------------------------\n"
                report_text += "\nJob Description Used:\n"
                report_text += job_description

            st.download_button(
                label="Download Report as TXT",
                data=report_text,
                file_name=f"{name}_career_report.txt",
                mime="text/plain"
            )