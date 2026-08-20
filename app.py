import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Career Recommendation Engine",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #f7f9fc;
    }

    /* Main container */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    /* Hero */
    .hero {
        padding: 32px 38px;
        border-radius: 20px;
        background: linear-gradient(
            135deg,
            #172554 0%,
            #1d4ed8 55%,
            #2563eb 100%
        );
        color: white;
        margin-bottom: 30px;
        box-shadow: 0 8px 25px rgba(37, 99, 235, 0.18);
    }

    .hero h1 {
        font-size: 38px;
        font-weight: 750;
        margin: 0 0 8px 0;
        color: white;
    }

    .hero p {
        font-size: 17px;
        margin: 0;
        color: #e0e7ff;
        line-height: 1.6;
    }

    /* Section title */
    .section-title {
        font-size: 26px;
        font-weight: 750;
        color: #111827;
        margin-top: 10px;
        margin-bottom: 12px;
    }

    /* Profile description */
    .profile-description {
        color: #6b7280;
        font-size: 15px;
        margin-bottom: 22px;
    }

    /* Info box */
    .info-box {
        padding: 15px 18px;
        border-radius: 12px;
        background: #eff6ff;
        border-left: 5px solid #2563eb;
        margin: 10px 0 25px 0;
        color: #1e3a8a;
    }

    /* Input labels */
    label {
        color: #374151 !important;
        font-weight: 600 !important;
    }

    /* Number input */
    div[data-testid="stNumberInput"] input {
        color: #111827 !important;
        background-color: #ffffff !important;
        caret-color: #111827 !important;
    }

    /* Number input buttons */
    div[data-testid="stNumberInput"] button {
        color: #111827 !important;
        background-color: #f3f4f6 !important;
    }

    /* Select boxes */
    div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #111827 !important;
    }

    /* Select box text */
    div[data-baseweb="select"] input {
        color: #111827 !important;
    }

    /* Text area */
    textarea {
        color: #111827 !important;
        background-color: #ffffff !important;
        caret-color: #111827 !important;
    }

    /* General input text */
    input {
        color: #111827 !important;
    }

    /* Button */
    .stButton > button {
        border-radius: 10px;
        font-weight: 700;
        height: 48px;
        border: none;
    }

    /* Result card */
    .result-card {
        padding: 22px 24px;
        border-radius: 16px;
        background: white;
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 14px rgba(0,0,0,0.06);
        margin-top: 18px;
        margin-bottom: 10px;
    }

    .rank {
        font-size: 13px;
        font-weight: 700;
        color: #2563eb;
        letter-spacing: 0.5px;
    }

    .career {
        font-size: 23px;
        font-weight: 750;
        color: #111827;
        margin: 5px 0;
    }

    .score {
        font-size: 17px;
        font-weight: 650;
        color: #16a34a;
    }

    /* Metrics */
    div[data-testid="stMetricValue"] {
        font-size: 25px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #6b7280;
        font-size: 13px;
        padding: 15px;
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
except Exception:
    model_loaded = False
    final_model = None


# ============================================================
# CAREER REQUIREMENT MAPPING
# ============================================================

career_requirements = {

    "Data Scientist": {
        "skills": ["Python", "SQL", "Statistics", "Machine Learning"],
        "interests": [
            "Data Science",
            "AI & Machine Learning",
            "Research"
        ],
        "strengths": [
            "Analytical",
            "Logical",
            "Academic"
        ]
    },

    "ML/AI Engineer": {
        "skills": [
            "Python",
            "Machine Learning",
            "Deep Learning"
        ],
        "interests": [
            "AI & Machine Learning",
            "Data Science"
        ],
        "strengths": [
            "Technical",
            "Logical",
            "Mathematical"
        ]
    },

    "Software Engineer": {
        "skills": [
            "Programming",
            "Python",
            "Java",
            "SQL",
            "Problem Solving"
        ],
        "interests": [
            "Software Development",
            "Technology"
        ],
        "strengths": [
            "Technical",
            "Logical"
        ]
    },

    "Business Analyst": {
        "skills": [
            "Excel",
            "SQL",
            "Power BI",
            "Data Analysis",
            "Communication"
        ],
        "interests": [
            "Business Management",
            "Data Science"
        ],
        "strengths": [
            "Analytical",
            "Communication",
            "Business"
        ]
    },

    "Cyber Security Analyst": {
        "skills": [
            "Cyber Security",
            "Networking",
            "Linux",
            "Python"
        ],
        "interests": [
            "Cyber Security",
            "Technology"
        ],
        "strengths": [
            "Technical",
            "Logical"
        ]
    },

    "Cloud Engineer": {
        "skills": [
            "AWS",
            "Azure",
            "Cloud Computing",
            "Linux",
            "Networking"
        ],
        "interests": [
            "Cloud Computing",
            "Technology"
        ],
        "strengths": [
            "Technical",
            "Logical"
        ]
    },

    "Marketing Executive": {
        "skills": [
            "Marketing",
            "Communication",
            "Digital Marketing",
            "Social Media"
        ],
        "interests": [
            "Business Management",
            "Entrepreneurship"
        ],
        "strengths": [
            "Communication",
            "Social",
            "Business"
        ]
    },

    "Sales Executive": {
        "skills": [
            "Sales",
            "Communication",
            "Negotiation",
            "Networking"
        ],
        "interests": [
            "Business Management",
            "Entrepreneurship"
        ],
        "strengths": [
            "Communication",
            "Social",
            "Business"
        ]
    },

    "Entrepreneur": {
        "skills": [
            "Business Strategy",
            "Leadership",
            "Communication",
            "Networking"
        ],
        "interests": [
            "Entrepreneurship",
            "Business Management"
        ],
        "strengths": [
            "Business",
            "Communication",
            "Leadership"
        ]
    },

    "Financial Analyst": {
        "skills": [
            "Excel",
            "Financial Analysis",
            "Accounting",
            "SQL"
        ],
        "interests": [
            "Business Management",
            "Data Science"
        ],
        "strengths": [
            "Analytical",
            "Academic"
        ]
    }
}


# ============================================================
# GOAL → CAREER MAPPING
# ============================================================

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
# SKILL SCORING
# ============================================================

def calculate_skill_scores(skills):

    skills_text = skills.lower()

    technical_keywords = [
        "python",
        "sql",
        "machine learning",
        "deep learning",
        "data science",
        "programming",
        "java",
        "c++",
        "cloud",
        "aws",
        "azure",
        "devops",
        "linux",
        "cyber security",
        "cybersecurity",
        "web development"
    ]

    communication_keywords = [
        "communication",
        "presentation",
        "public speaking",
        "negotiation",
        "sales",
        "marketing",
        "leadership",
        "teamwork",
        "management",
        "business"
    ]

    technical_count = sum(
        keyword in skills_text
        for keyword in technical_keywords
    )

    communication_count = sum(
        keyword in skills_text
        for keyword in communication_keywords
    )

    programming_skill = min(
        5,
        max(1, technical_count + 2)
    )

    communication_skill = min(
        5,
        max(1, communication_count + 2)
    )

    technical_strength = (
        programming_skill / 5
    ) * 100

    communication_strength = (
        communication_skill / 5
    ) * 100

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


# ============================================================
# BUILD USER FEATURES
# ============================================================

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


# ============================================================
# MODEL PREDICTION
# ============================================================

def final_recommend_career(student_profile):

    student_df = pd.DataFrame([student_profile])

    probabilities = final_model.predict_proba(
        student_df
    )[0]

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


# ============================================================
# GOAL ALIGNMENT
# ============================================================

def get_goal_alignment(career_goal, career):

    relevant_careers = goal_career_mapping.get(
        career_goal,
        []
    )

    if career in relevant_careers:

        position = relevant_careers.index(career)

        alignment_scores = [
            100,
            90,
            80,
            70,
            60,
            50
        ]

        if position < len(alignment_scores):
            return alignment_scores[position]

        return 50

    return 0


# ============================================================
# CAREER FIT ANALYSIS
# ============================================================

def analyze_career_fit(student_profile, career):

    requirements = career_requirements.get(career)

    if requirements is None:

        return {
            "Why_Recommended":
                "Career requirement mapping not available.",
            "Skills_to_Improve": []
        }

    student_skills = str(
        student_profile.get(
            "Skills",
            ""
        )
    ).lower()

    student_interest = str(
        student_profile.get(
            "Interest",
            ""
        )
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
            "Your current skills match: "
            + ", ".join(matched_skills)
        )

    if interest_match:

        reasons.append(
            "Your interest is aligned with this career."
        )

    academic = float(
        student_profile.get(
            "Academic_Performance",
            0
        )
    )

    aptitude = float(
        student_profile.get(
            "Aptitude_Score",
            0
        )
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
            "The model identified this career "
            "as a suitable option."
        )

    return {
        "Why_Recommended": " ".join(reasons),
        "Skills_to_Improve": missing_skills
    }


# ============================================================
# FINAL SCORE CALCULATION
# ============================================================

def calculate_final_scores(
    student_profile,
    recommendations
):

    results = []

    for _, row in recommendations.iterrows():

        career = row["Career"]
        model_confidence = row["Confidence"]

        goal_alignment = get_goal_alignment(
            student_profile["Career_Goal"],
            career
        )

        matched = len([
            skill
            for skill in career_requirements.get(
                career,
                {}
            ).get(
                "skills",
                []
            )
            if skill.lower()
            in str(
                student_profile["Skills"]
            ).lower()
        ])

        total_required = len(
            career_requirements.get(
                career,
                {}
            ).get(
                "skills",
                []
            )
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

            "Model_Confidence":
                round(
                    model_confidence,
                    2
                ),

            "Capability_Match":
                round(
                    capability_match,
                    2
                ),

            "Goal_Alignment":
                round(
                    goal_alignment,
                    2
                ),

            "Final_Score":
                round(
                    final_score,
                    2
                )
        })

    result_df = pd.DataFrame(results)

    result_df = result_df.sort_values(
        by="Final_Score",
        ascending=False
    ).reset_index(drop=True)

    result_df.insert(
        0,
        "Rank",
        range(
            1,
            len(result_df) + 1
        )
    )

    return result_df


# ============================================================
# HERO HEADER
# ============================================================

st.markdown("""
<div class="hero">

    <h1>🎯 AI Career Recommendation Engine</h1>

    <p>
        Discover the career paths that best match your
        aptitude, interests, personality, academic performance
        and skills.
    </p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# MODEL CHECK
# ============================================================

if not model_loaded:

    st.error(
        "career_model.pkl was not found. "
        "Place the trained model file in the same "
        "folder as app.py."
    )

    st.stop()


# ============================================================
# STUDENT PROFILE
# ============================================================

st.markdown(
    '<div class="section-title">👤 Student Profile</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="profile-description">

Enter your profile below to discover the career paths
that best match your abilities and interests.

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROFILE INPUTS
# ============================================================

with st.container(border=True):

    # --------------------------------------------------------
    # Aptitude Score + Academic Performance
    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        aptitude = st.number_input(
            "Aptitude Score",
            min_value=0,
            max_value=100,
            value=70,
            step=1,
            help="Enter your aptitude assessment score."
        )

    with col2:

        academic_performance = st.number_input(
            "Academic Performance",
            min_value=0,
            max_value=100,
            value=75,
            step=1,
            help="Enter your overall academic performance."
        )


    # --------------------------------------------------------
    # Interest + Personality
    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        interest = st.selectbox(
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

    with col2:

        personality = st.selectbox(
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


    # --------------------------------------------------------
    # Skills
    # --------------------------------------------------------

    skills = st.text_area(
        "Skills",
        placeholder=(
            "Example: Python, SQL, Machine Learning, Power BI"
        ),
        height=100
    )


    # --------------------------------------------------------
    # Career Goal
    # --------------------------------------------------------

    career_goal = st.selectbox(
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


    # --------------------------------------------------------
    # Recommend Button
    # --------------------------------------------------------

    st.markdown(
        "<br>",
        unsafe_allow_html=True
    )

    button_col1, button_col2, button_col3 = st.columns(
        [1, 1, 1]
    )

    with button_col2:

        generate = st.button(
            "🚀 Recommend Careers",
            use_container_width=True,
            type="primary"
        )


# ============================================================
# INFORMATION BEFORE RECOMMENDATION
# ============================================================

if not skills.strip():

    st.markdown("""
    <div class="info-box">

        <b>How it works:</b><br>

        Enter your skills and profile information above,
        then click <b>Recommend Careers</b>.

        The trained Random Forest model will generate
        your Top 5 career recommendations.

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# GENERATE RECOMMENDATIONS
# ============================================================

if generate:

    if not skills.strip():

        st.warning(
            "Please enter at least a few skills "
            "before generating recommendations."
        )

    else:

        student_profile = build_user_features(
            aptitude=aptitude,
            interest=interest,
            personality=personality,
            academic_performance=academic_performance,
            skills=skills,
            career_goal=career_goal
        )

        recommendations = final_recommend_career(
            student_profile
        )

        final_results = calculate_final_scores(
            student_profile,
            recommendations
        )

        st.session_state[
            "student_profile"
        ] = student_profile

        st.session_state[
            "final_results"
        ] = final_results


# ============================================================
# DISPLAY RESULTS
# ============================================================

if "final_results" in st.session_state:

    final_results = st.session_state[
        "final_results"
    ]

    student_profile = st.session_state[
        "student_profile"
    ]


    # --------------------------------------------------------
    # Results Heading
    # --------------------------------------------------------

    st.markdown("---")

    st.markdown(
        '<div class="section-title">'
        '🏆 Your Top 5 Career Recommendations'
        '</div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # Best Career
    # --------------------------------------------------------

    best = final_results.iloc[0]

    st.success(
        f"Best Match: **{best['Career']}** — "
        f"Final Score: **{best['Final_Score']:.2f}%**"
    )


    # --------------------------------------------------------
    # Metrics
    # --------------------------------------------------------

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


    # --------------------------------------------------------
    # Recommendation Cards
    # --------------------------------------------------------

    for _, row in final_results.iterrows():

        analysis = analyze_career_fit(
            student_profile,
            row["Career"]
        )

        st.markdown(
            f"""
            <div class="result-card">

                <div class="rank">
                    RANK #{int(row['Rank'])}
                </div>

                <div class="career">
                    {row['Career']}
                </div>

                <div class="score">
                    Final Score:
                    {row['Final_Score']:.2f}%
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
            f"**💡 Why recommended:** "
            f"{analysis['Why_Recommended']}"
        )


        if analysis["Skills_to_Improve"]:

            st.write(
                "**🚀 Skills to improve:** "
                +
                ", ".join(
                    analysis["Skills_to_Improve"]
                )
            )

        else:

            st.write(
                "**🚀 Skills to improve:** "
                "No major skill gap identified."
            )


        st.markdown("---")


    # ========================================================
    # RECOMMENDATION COMPARISON
    # ========================================================

    st.markdown(
        '<div class="section-title">'
        '📊 Recommendation Comparison'
        '</div>',
        unsafe_allow_html=True
    )

    chart_df = (
        final_results
        .set_index("Career")[["Final_Score"]]
    )

    st.bar_chart(chart_df)


    # ========================================================
    # DETAILED TABLE
    # ========================================================

    st.markdown(
        '<div class="section-title">'
        '📋 Detailed Recommendation Scores'
        '</div>',
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


    # ========================================================
    # DOWNLOAD RESULTS
    # ========================================================

    csv = (
        display_df
        .to_csv(index=False)
        .encode("utf-8")
    )

    st.download_button(
        "⬇️ Download Recommendations",
        data=csv,
        file_name="career_recommendations.csv",
        mime="text/csv"
    )


    # ========================================================
    # RESET
    # ========================================================

    if st.button("🔄 Start New Assessment"):

        st.session_state.clear()
        st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.markdown("""
<div class="footer">

AI Career Recommendation Engine |
Machine Learning + Rule-Based Career Fit Analysis

</div>
""", unsafe_allow_html=True)
