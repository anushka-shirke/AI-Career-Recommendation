
import streamlit as st
import pandas as pd
import numpy as np
import joblib
st.title("🔥 TEST VERSION 999 🔥")
# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Career Recommendation Engine",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>
    .main {
        background-color: #f7f9fc;
    }

    .hero {
        padding: 28px 30px;
        border-radius: 18px;
        background: linear-gradient(135deg, #172554, #2563eb);
        color: white;
        margin-bottom: 25px;
    }

    .hero h1 {
        font-size: 38px;
        margin-bottom: 8px;
    }

    .hero p {
        font-size: 17px;
        opacity: 0.92;
    }

    .result-card {
        padding: 20px;
        border-radius: 16px;
        background: white;
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 14px rgba(0,0,0,0.06);
        margin-bottom: 14px;
    }

    .rank {
        font-size: 14px;
        font-weight: 700;
        color: #2563eb;
    }

    .career {
        font-size: 23px;
        font-weight: 700;
        color: #111827;
        margin: 4px 0;
    }

    .score {
        font-size: 17px;
        font-weight: 600;
        color: #16a34a;
    }

    .section-title {
        font-size: 25px;
        font-weight: 700;
        color: #111827;
        margin-top: 10px;
        margin-bottom: 12px;
    }

    .info-box {
        padding: 15px 18px;
        border-radius: 12px;
        background: #eff6ff;
        border-left: 5px solid #2563eb;
        margin: 10px 0 20px 0;
    }

    div[data-testid="stMetricValue"] {
        font-size: 28px;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():
    return joblib.load("career_model.pkl")


try:
    final_model = load_model()
    model_loaded = True
except Exception as e:
    model_loaded = False
    final_model = None

# ============================================================
# CAREER REQUIREMENT MAPPING
# ============================================================

career_requirements = {

    "Data Scientist": {
        "skills": ["Python", "SQL", "Statistics", "Machine Learning"],
        "interests": ["Data Science", "AI & Machine Learning", "Research"],
        "strengths": ["Analytical", "Logical", "Academic"]
    },

    "ML/AI Engineer": {
        "skills": ["Python", "Machine Learning", "Deep Learning"],
        "interests": ["AI & Machine Learning", "Data Science"],
        "strengths": ["Technical", "Logical", "Mathematical"]
    },

    "Software Engineer": {
        "skills": ["Programming", "Python", "Java", "SQL", "Problem Solving"],
        "interests": ["Software Development", "Technology"],
        "strengths": ["Technical", "Logical"]
    },

    "Business Analyst": {
        "skills": ["Excel", "SQL", "Power BI", "Data Analysis", "Communication"],
        "interests": ["Business Management", "Data Science"],
        "strengths": ["Analytical", "Communication", "Business"]
    },

    "Cyber Security Analyst": {
        "skills": ["Cyber Security", "Networking", "Linux", "Python"],
        "interests": ["Cyber Security", "Technology"],
        "strengths": ["Technical", "Logical"]
    },

    "Cloud Engineer": {
        "skills": ["AWS", "Azure", "Cloud Computing", "Linux", "Networking"],
        "interests": ["Cloud Computing", "Technology"],
        "strengths": ["Technical", "Logical"]
    },

    "Marketing Executive": {
        "skills": ["Marketing", "Communication", "Digital Marketing", "Social Media"],
        "interests": ["Business Management", "Entrepreneurship"],
        "strengths": ["Communication", "Social", "Business"]
    },

    "Sales Executive": {
        "skills": ["Sales", "Communication", "Negotiation", "Networking"],
        "interests": ["Business Management", "Entrepreneurship"],
        "strengths": ["Communication", "Social", "Business"]
    },

    "Entrepreneur": {
        "skills": ["Business Strategy", "Leadership", "Communication", "Networking"],
        "interests": ["Entrepreneurship", "Business Management"],
        "strengths": ["Business", "Communication", "Leadership"]
    },

    "Financial Analyst": {
        "skills": ["Excel", "Financial Analysis", "Accounting", "SQL"],
        "interests": ["Business Management", "Data Science"],
        "strengths": ["Analytical", "Academic"]
    }
}

goal_career_mapping = {
    "Data Science": [
        "Data Scientist",
        "ML/AI Engineer",
        "Research Scientist",
        "Business Analyst",
        "Financial Analyst"
    ],

    "AI & Machine Learning": [
        "ML/AI Engineer",
        "Data Scientist",
        "Research Scientist",
        "Software Engineer"
    ],

    "Software Development": [
        "Software Engineer",
        "Web Developer",
        "ML/AI Engineer"
    ],

    "Cyber Security": [
        "Cyber Security Analyst"
    ],

    "Cloud Computing": [
        "Cloud Engineer",
        "Software Engineer"
    ],

    "Business Management": [
        "Business Analyst",
        "Entrepreneur",
        "Marketing Executive",
        "Sales Executive",
        "Financial Analyst",
        "HR Manager"
    ],

    "Entrepreneurship": [
        "Entrepreneur",
        "Business Analyst",
        "Marketing Executive",
        "Sales Executive"
    ],

    "Government Job": [
        "Government Officer"
    ],

    "Higher Studies": [
        "Professor",
        "Research Scientist",
        "Doctor"
    ],

    "Research": [
        "Research Scientist",
        "Data Scientist",
        "Professor"
    ]
}

# ============================================================
# FUNCTIONS — SAME LOGIC AS FINAL NOTEBOOK
# ============================================================

def calculate_skill_scores(skills):
    skills_text = skills.lower()

    technical_keywords = [
        "python", "sql", "machine learning", "deep learning",
        "data science", "programming", "java", "c++",
        "cloud", "aws", "azure", "devops", "linux",
        "cyber security", "cybersecurity", "web development"
    ]

    communication_keywords = [
        "communication", "presentation", "public speaking",
        "negotiation", "sales", "marketing", "leadership",
        "teamwork", "management", "business"
    ]

    technical_count = sum(
        keyword in skills_text
        for keyword in technical_keywords
    )

    communication_count = sum(
        keyword in skills_text
        for keyword in communication_keywords
    )

    programming_skill = min(5, max(1, technical_count + 2))
    communication_skill = min(5, max(1, communication_count + 2))

    technical_strength = programming_skill / 5 * 100
    communication_strength = communication_skill / 5 * 100

    soft_skill_score = min(
        10,
        max(1, communication_count * 2 + 6)
    )

    return (
        programming_skill,
        communication_skill,
        soft_skill_score,
        technical_strength,
        communication_strength
    )


def build_user_features(
    aptitude,
    interest,
    personality,
    academic_performance,
    skills,
    career_goal
):
    student = {
        "Aptitude_Score": aptitude,
        "Interest": interest,
        "Personality_Type": personality,
        "Academic_Performance": academic_performance,
        "Skills": skills,
        "Career_Goal": career_goal
    }

    student["Overall_Aptitude"] = aptitude
    student["Academic_Strength"] = academic_performance

    (
        programming_skill,
        communication_skill,
        soft_skill_score,
        technical_strength,
        communication_strength
    ) = calculate_skill_scores(skills)

    student["Programming_Skill"] = programming_skill
    student["Communication_Skill"] = communication_skill
    student["Soft_Skills_Score"] = soft_skill_score

    student["Technical_Skill_Strength"] = technical_strength
    student["Communication_Strength"] = communication_strength

    student["Career_Readiness_Score"] = (
        academic_performance * 0.5 +
        aptitude * 0.5
    )

    return student


def final_recommend_career(student_profile):
    student_df = pd.DataFrame([student_profile])

    probabilities = final_model.predict_proba(student_df)[0]
    careers = final_model.classes_

    recommendations = pd.DataFrame({
        "Career": careers,
        "Confidence": probabilities * 100
    })

    recommendations = recommendations.sort_values(
        by="Confidence",
        ascending=False
    ).reset_index(drop=True)

    return recommendations.head(5)


def get_goal_alignment(career_goal, career):
    relevant_careers = goal_career_mapping.get(career_goal, [])

    if career in relevant_careers:
        position = relevant_careers.index(career)
        alignment_scores = [100, 90, 80, 70, 60, 50]

        if position < len(alignment_scores):
            return alignment_scores[position]

        return 50

    return 0


def analyze_career_fit(student_profile, career):
    requirements = career_requirements.get(career)

    if requirements is None:
        return {
            "Why_Recommended": "Career requirement mapping not available.",
            "Skills_to_Improve": []
        }

    student_skills = str(
        student_profile.get("Skills", "")
    ).lower()

    student_interest = str(
        student_profile.get("Interest", "")
    ).lower()

    matched_skills = []
    missing_skills = []

    for skill in requirements["skills"]:
        if skill.lower() in student_skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    interest_match = any(
        interest.lower() in student_interest
        for interest in requirements["interests"]
    )

    reasons = []

    if matched_skills:
        reasons.append(
            "Your current skills match: " +
            ", ".join(matched_skills)
        )

    if interest_match:
        reasons.append(
            "Your interest is aligned with this career."
        )

    academic = float(
        student_profile.get("Academic_Performance", 0)
    )

    aptitude = float(
        student_profile.get("Aptitude_Score", 0)
    )

    if academic >= 80:
        reasons.append(
            "Your academic performance is strong."
        )

    if aptitude >= 70:
        reasons.append(
            "Your aptitude level supports this career."
        )

    if not reasons:
        reasons.append(
            "The model identified this career as a suitable option."
        )

    return {
        "Why_Recommended": " ".join(reasons),
        "Skills_to_Improve": missing_skills
    }


def calculate_final_scores(student_profile, recommendations):

    results = []

    for _, row in recommendations.iterrows():

        career = row["Career"]
        model_confidence = row["Confidence"]

        goal_alignment = get_goal_alignment(
            student_profile["Career_Goal"],
            career
        )

        matched = len([
            skill for skill in career_requirements.get(
                career, {}
            ).get("skills", [])
            if skill.lower() in str(
                student_profile["Skills"]
            ).lower()
        ])

        total_required = len(
            career_requirements.get(
                career, {}
            ).get("skills", [])
        )

        if total_required > 0:
            capability_match = (
                matched / total_required
            ) * 100
        else:
            capability_match = 50

        final_score = (
            0.40 * model_confidence +
            0.30 * capability_match +
            0.30 * goal_alignment
        )

        results.append({
            "Career": career,
            "Model_Confidence": round(model_confidence, 2),
            "Capability_Match": round(capability_match, 2),
            "Goal_Alignment": round(goal_alignment, 2),
            "Final_Score": round(final_score, 2)
        })

    result_df = pd.DataFrame(results)

    result_df = result_df.sort_values(
        by="Final_Score",
        ascending=False
    ).reset_index(drop=True)

    result_df.insert(
        0,
        "Rank",
        range(1, len(result_df) + 1)
    )

    return result_df

# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="hero">
    <h1>🎯 AI Career Recommendation Engine</h1>
    <p>
        Discover the career paths that best match your aptitude,
        interests, personality, academic performance and skills.
    </p>
</div>
""", unsafe_allow_html=True)

if not model_loaded:
    st.error(
        "career_model.pkl was not found. "
        "Place the trained model file in the same folder as app.py."
    )
    st.stop()

# ============================================================
# SIDEBAR INPUTS
# ============================================================

st.sidebar.header("👤 Student Profile")
st.sidebar.caption("Enter your profile to generate career recommendations.")

aptitude = st.sidebar.slider(
    "Aptitude Score",
    min_value=0,
    max_value=100,
    value=70,
    help="Enter your aptitude assessment score."
)

academic_performance = st.sidebar.slider(
    "Academic Performance",
    min_value=0,
    max_value=100,
    value=75,
    help="Enter your overall academic performance."
)

interest = st.sidebar.selectbox(
    "Interest",
    [
        "Data Science",
        "AI & Machine Learning",
        "Software Development",
        "Cyber Security",
        "Cloud Computing",
        "Business Management",
        "Entrepreneurship",
        "Research",
        "Science",
        "Arts",
        "Social"
    ]
)

personality = st.sidebar.selectbox(
    "Personality Type",
    [
        "Realistic",
        "Investigative",
        "Artistic",
        "Social",
        "Enterprising",
        "Conventional"
    ]
)

skills = st.sidebar.text_area(
    "Skills",
    placeholder="Example: Python, SQL, Machine Learning, Power BI",
    height=110
)

career_goal = st.sidebar.selectbox(
    "Career Goal",
    [
        "Data Science",
        "AI & Machine Learning",
        "Software Development",
        "Cyber Security",
        "Cloud Computing",
        "Business Management",
        "Entrepreneurship",
        "Government Job",
        "Higher Studies",
        "Research"
    ]
)

st.sidebar.markdown("---")
generate = st.sidebar.button(
    "🚀 Recommend Careers",
    use_container_width=True,
    type="primary"
)

# ============================================================
# MAIN CONTENT
# ============================================================

if not skills.strip():
    st.markdown("""
    <div class="info-box">
        <b>How it works:</b><br>
        Enter your student profile from the sidebar and click
        <b>Recommend Careers</b>. The trained Random Forest model
        will return your Top 5 career recommendations.
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Model Type", "Random Forest")

    with col2:
        st.metric("Recommendations", "Top 5")

    with col3:
        st.metric("Model Accuracy", "71.4%")

else:
    if generate:

        student_profile = build_user_features(
            aptitude=aptitude,
            interest=interest,
            personality=personality,
            academic_performance=academic_performance,
            skills=skills,
            career_goal=career_goal
        )

        recommendations = final_recommend_career(student_profile)

        final_results = calculate_final_scores(
            student_profile,
            recommendations
        )

        st.session_state["student_profile"] = student_profile
        st.session_state["final_results"] = final_results

# ============================================================
# DISPLAY RESULTS
# ============================================================

if "final_results" in st.session_state:

    final_results = st.session_state["final_results"]
    student_profile = st.session_state["student_profile"]

    st.markdown(
        '<div class="section-title">🏆 Your Top 5 Career Recommendations</div>',
        unsafe_allow_html=True
    )

    # Best career
    best = final_results.iloc[0]

    st.success(
        f"Best Match: **{best['Career']}** — "
        f"Final Score: **{best['Final_Score']:.2f}%**"
    )

    # Metrics
    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Best Career",
            best["Career"]
        )

    with c2:
        st.metric(
            "Final Score",
            f"{best['Final_Score']:.2f}%"
        )

    with c3:
        st.metric(
            "Model Confidence",
            f"{best['Model_Confidence']:.2f}%"
        )

    st.markdown("---")

    # Recommendation cards
    for _, row in final_results.iterrows():

        analysis = analyze_career_fit(
            student_profile,
            row["Career"]
        )

        st.markdown(
            f"""
            <div class="result-card">
                <div class="rank">RANK #{int(row['Rank'])}</div>
                <div class="career">{row['Career']}</div>
                <div class="score">
                    Final Score: {row['Final_Score']:.2f}%
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Model Confidence",
                f"{row['Model_Confidence']:.2f}%"
            )

        with col2:
            st.metric(
                "Capability Match",
                f"{row['Capability_Match']:.2f}%"
            )

        with col3:
            st.metric(
                "Goal Alignment",
                f"{row['Goal_Alignment']:.0f}%"
            )

        st.write(
            f"**💡 Why recommended:** {analysis['Why_Recommended']}"
        )

        if analysis["Skills_to_Improve"]:
            st.write(
                "**🚀 Skills to improve:** " +
                ", ".join(analysis["Skills_to_Improve"])
            )
        else:
            st.write(
                "**🚀 Skills to improve:** "
                "No major skill gap identified."
            )

        st.markdown("---")

    # Chart
    st.markdown(
        '<div class="section-title">📊 Recommendation Comparison</div>',
        unsafe_allow_html=True
    )

    chart_df = final_results.set_index("Career")[
        ["Final_Score"]
    ]

    st.bar_chart(chart_df)

    # Detailed table
    st.markdown(
        '<div class="section-title">📋 Detailed Recommendation Scores</div>',
        unsafe_allow_html=True
    )

    display_df = final_results.copy()

    display_df.columns = [
        "Rank",
        "Career",
        "Model Confidence (%)",
        "Capability Match (%)",
        "Goal Alignment (%)",
        "Final Score (%)"
    ]

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

    # Download results
    csv = display_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇️ Download Recommendations",
        data=csv,
        file_name="career_recommendations.csv",
        mime="text/csv"
    )

    # Reset
    if st.button("🔄 Start New Assessment"):
        st.session_state.clear()
        st.rerun()

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "AI Career Recommendation Engine | "
    "Machine Learning + Rule-Based Career Fit Analysis"
)
