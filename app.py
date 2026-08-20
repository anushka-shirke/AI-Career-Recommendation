import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Career Navigator",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

/* =========================
   GLOBAL
========================= */

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(79,70,229,0.18), transparent 28%),
        radial-gradient(circle at 90% 20%, rgba(6,182,212,0.12), transparent 25%),
        #0B1220;
    color: #F8FAFC;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* =========================
   HEADER
========================= */

.hero {
    background: linear-gradient(
        135deg,
        rgba(79,70,229,0.25),
        rgba(6,182,212,0.12)
    );

    border: 1px solid rgba(129,140,248,0.25);
    border-radius: 28px;

    padding: 35px 40px;

    margin-bottom: 25px;

    box-shadow:
        0 20px 60px rgba(0,0,0,0.25);
}

.hero-title {
    font-size: 42px;
    font-weight: 800;
    margin: 0;
    color: #F8FAFC;
}

.hero-subtitle {
    font-size: 17px;
    color: #94A3B8;
    margin-top: 8px;
}

/* =========================
   MASCOT
========================= */

.mascot {
    background: linear-gradient(
        145deg,
        #4F46E5,
        #06B6D4
    );

    width: 105px;
    height: 105px;

    border-radius: 50%;

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 54px;

    box-shadow:
        0 0 35px rgba(79,70,229,0.45);

    margin: auto;
}

.mascot-small {
    font-size: 35px;
}

/* =========================
   SECTION HEADERS
========================= */

.section-title {
    font-size: 25px;
    font-weight: 750;
    color: #F8FAFC;

    margin-top: 30px;
    margin-bottom: 15px;
}

.section-description {
    color: #94A3B8;
    font-size: 14px;
    margin-bottom: 18px;
}

/* =========================
   CARDS
========================= */

.card {
    background: rgba(17,24,39,0.88);

    border: 1px solid rgba(148,163,184,0.12);

    border-radius: 20px;

    padding: 22px;

    margin-bottom: 15px;

    box-shadow:
        0 10px 35px rgba(0,0,0,0.18);
}

.card:hover {
    border-color: rgba(99,102,241,0.45);
}

/* =========================
   INPUT BOX
========================= */

.input-card {
    background: #111827;

    border: 1px solid rgba(99,102,241,0.15);

    border-radius: 20px;

    padding: 22px;

    min-height: 180px;
}

/* =========================
   CAREER CARDS
========================= */

.career-card {
    background: linear-gradient(
        145deg,
        #111827,
        #0F172A
    );

    border: 1px solid rgba(99,102,241,0.20);

    border-radius: 22px;

    padding: 25px;

    margin-bottom: 15px;

    box-shadow:
        0 12px 40px rgba(0,0,0,0.20);
}

.rank {
    font-size: 14px;
    font-weight: 700;
    color: #06B6D4;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.career-name {
    font-size: 25px;
    font-weight: 750;
    color: #F8FAFC;
    margin-top: 5px;
}

.score {
    font-size: 32px;
    font-weight: 800;
    color: #818CF8;
}

/* =========================
   BEST MATCH
========================= */

.best-match {
    background:
        linear-gradient(
            135deg,
            rgba(79,70,229,0.28),
            rgba(6,182,212,0.15)
        );

    border: 1px solid rgba(129,140,248,0.35);

    border-radius: 25px;

    padding: 30px;

    margin-top: 25px;

    box-shadow:
        0 15px 50px rgba(79,70,229,0.18);
}

.best-title {
    color: #94A3B8;
    font-size: 14px;
    text-transform: uppercase;
    letter-spacing: 2px;
}

.best-career {
    font-size: 36px;
    font-weight: 850;
    color: #F8FAFC;
}

/* =========================
   INSIGHT CARDS
========================= */

.insight {
    background: #111827;

    border-left: 4px solid #4F46E5;

    border-radius: 14px;

    padding: 17px 20px;

    margin-bottom: 12px;

    color: #E2E8F0;
}

/* =========================
   IMPROVEMENT
========================= */

.improvement {
    background: rgba(245,158,11,0.07);

    border: 1px solid rgba(245,158,11,0.18);

    border-radius: 15px;

    padding: 17px 20px;

    margin-bottom: 12px;
}

/* =========================
   BUTTON
========================= */

.stButton > button {
    width: 100%;

    background: linear-gradient(
        90deg,
        #4F46E5,
        #06B6D4
    );

    color: white;

    border: none;

    border-radius: 14px;

    padding: 14px;

    font-size: 17px;

    font-weight: 750;

    box-shadow:
        0 8px 25px rgba(79,70,229,0.25);

    transition: 0.2s;
}

.stButton > button:hover {
    transform: translateY(-2px);

    box-shadow:
        0 12px 30px rgba(6,182,212,0.25);
}

/* =========================
   METRIC
========================= */

[data-testid="stMetric"] {
    background: #111827;

    border: 1px solid rgba(148,163,184,0.10);

    border-radius: 15px;

    padding: 15px;
}

/* =========================
   SLIDERS / INPUTS
========================= */

label {
    color: #CBD5E1 !important;
    font-weight: 600 !important;
}

div[data-baseweb="select"] > div,
.stTextInput input {
    background-color: #111827 !important;
    border-color: #334155 !important;
    color: #F8FAFC !important;
}

/* =========================
   FOOTER
========================= */

.footer {
    text-align: center;

    color: #64748B;

    font-size: 13px;

    padding: 35px 0 10px;
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
    model = load_model()

except Exception as e:

    st.error("Unable to load career_model.pkl")

    st.exception(e)

    st.stop()


# ============================================================
# HERO SECTION
# ============================================================

st.markdown("""
<div class="hero">

<div style="display:flex; align-items:center; gap:30px;">

<div style="flex:1;">

<div class="hero-title">
🎯 AI Career Navigator
</div>

<div class="hero-subtitle">
Discover careers that match your potential, personality,
skills, interests and goals.
</div>

</div>

<div class="mascot">
🤖
</div>

</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# INTRO
# ============================================================

st.markdown("""
<div class="card">

<b>Meet your AI Career Guide 🤖</b>

<br><br>

Answer a few questions about yourself and the AI model
will analyze your profile to generate personalized career
recommendations.

<br><br>

<span style="color:#94A3B8;">
The system evaluates your abilities, interests,
personality, academic performance, skills and career goal.
</span>

</div>
""", unsafe_allow_html=True)


# ============================================================
# STUDENT PROFILE
# ============================================================

st.markdown(
    '<div class="section-title">👤 Tell us about yourself</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">These inputs represent the core profile used for career matching.</div>',
    unsafe_allow_html=True
)


col1, col2 = st.columns(2)


# ============================================================
# LEFT INPUTS
# ============================================================

with col1:

    aptitude = st.slider(
        "🧠 Aptitude Score",
        0.0,
        100.0,
        72.5,
        0.1
    )

    interest = st.selectbox(
        "❤️ Interest Area",
        [
            "Business",
            "Technology",
            "Science",
            "Arts",
            "Social"
        ]
    )

    personality = st.selectbox(
        "🧩 Personality Type",
        [
            "Realistic",
            "Investigative",
            "Artistic",
            "Social",
            "Enterprising",
            "Conventional"
        ]
    )


# ============================================================
# RIGHT INPUTS
# ============================================================

with col2:

    academic_performance = st.slider(
        "📚 Academic Performance",
        0.0,
        100.0,
        80.0,
        0.1
    )

    skills = st.text_input(
        "💻 Skills",
        placeholder="Python, SQL, Excel, Business Strategy..."
    )

    career_goal = st.selectbox(
        "🎯 Career Goal",
        [
            "Data Science",
            "AI & Machine Learning",
            "Software Development",
            "Cyber Security",
            "Cloud Computing",
            "Business Management",
            "Research",
            "Entrepreneurship",
            "Government Job",
            "Higher Studies"
        ]
    )


# ============================================================
# PROFILE SUMMARY
# ============================================================

st.markdown(
    '<div class="section-title">📋 Profile Snapshot</div>',
    unsafe_allow_html=True
)

p1, p2, p3, p4 = st.columns(4)

with p1:
    st.metric("Aptitude", f"{aptitude:.1f}")

with p2:
    st.metric("Academic", f"{academic_performance:.1f}%")

with p3:
    st.metric("Interest", interest)

with p4:
    st.metric("Goal", career_goal)


# ============================================================
# CREATE MODEL INPUT
# ============================================================

def create_input():

    programming_skill = 2

    communication_skill = 3

    skills_lower = skills.lower()

    # Programming estimation
    if any(
        word in skills_lower
        for word in [
            "python",
            "java",
            "c++",
            "sql",
            "coding",
            "programming",
            "machine learning"
        ]
    ):

        programming_skill = 4


    # Communication estimation
    if any(
        word in skills_lower
        for word in [
            "communication",
            "presentation",
            "sales",
            "marketing",
            "leadership"
        ]
    ):

        communication_skill = 4


    technical_strength = programming_skill * 20

    communication_strength = communication_skill * 20


    career_readiness = (

        aptitude * 0.35

        + academic_performance * 0.35

        + communication_strength * 0.15

        + technical_strength * 0.15

    )


    data = {

        "Age": 21,

        "Gender": "Not Specified",

        "Education_Level": "Bachelor's",

        "Specialization": "General",

        "Career_Goal": career_goal,

        "Math_Score": academic_performance,

        "Science_Score": academic_performance,

        "Programming_Skill": programming_skill,

        "Communication_Skill": communication_skill,

        "Logical_Ability": aptitude / 10,

        "R_score": 5,

        "I_score": 5,

        "A_score": 5,

        "S_score": 5,

        "E_score": 5,

        "C_score": 5,

        "Openness": 0.70,

        "Conscientiousness": 0.70,

        "Extraversion": 0.70,

        "Agreeableness": 0.70,

        "Neuroticism": 0.30,

        "High_School_Percentage": academic_performance,

        "CGPA": min(10, academic_performance / 10),

        "Internships_Completed": 0,

        "Projects_Completed": 0,

        "Certifications_Count": 0,

        "Certification_Name": "No Certification",

        "Skills": skills,

        "Soft_Skills_Score": 7,

        "Networking_Score": 5,

        "Attendance_Percentage": 85,

        "Backlog": "No",

        "Aptitude_Score": aptitude,

        "Academic_Performance": academic_performance,

        "Interest": interest,

        "Personality_Type": personality,

        "Academic_Strength": academic_performance,

        "Technical_Skill_Strength": technical_strength,

        "Communication_Strength": communication_strength,

        "Career_Readiness_Score": career_readiness,

        "Overall_Aptitude": aptitude

    }

    return pd.DataFrame([data])


# ============================================================
# CAREER GOAL ALIGNMENT
# ============================================================

def calculate_goal_alignment(career):

    goal = career_goal.lower()

    career_lower = career.lower()


    mapping = {

        "business management": [

            "business analyst",
            "entrepreneur",
            "sales executive",
            "marketing executive",
            "financial analyst",
            "hr manager"

        ],

        "data science": [

            "data scientist",
            "ml/ai engineer",
            "research scientist"

        ],

        "ai & machine learning": [

            "ml/ai engineer",
            "data scientist",
            "research scientist",
            "software engineer"

        ],

        "software development": [

            "software engineer",
            "web developer"

        ],

        "cyber security": [

            "cyber security analyst"

        ],

        "cloud computing": [

            "cloud engineer"

        ],

        "research": [

            "research scientist",
            "professor",
            "data scientist"

        ],

        "government job": [

            "government officer"

        ],

        "entrepreneurship": [

            "entrepreneur",
            "business analyst"

        ],

        "higher studies": [

            "professor",
            "research scientist"

        ]

    }


    for goal_name, careers in mapping.items():

        if goal_name in goal:

            if career_lower in careers:

                return 100

            return 40


    return 50


# ============================================================
# REASON GENERATOR
# ============================================================

def get_reasons(career):

    reasons = []

    alignment = calculate_goal_alignment(career)

    career_lower = career.lower()


    if alignment >= 80:

        reasons.append(
            f"Your career goal of '{career_goal}' strongly aligns with this role."
        )


    if interest.lower() in career_lower:

        reasons.append(
            f"Your interest in {interest} supports this career direction."
        )


    business_roles = [

        "business analyst",
        "entrepreneur",
        "sales executive",
        "marketing executive",
        "financial analyst",
        "hr manager"

    ]


    if (
        personality in
        [
            "Realistic",
            "Enterprising",
            "Conventional"
        ]
        and career_lower in business_roles
    ):

        reasons.append(
            f"Your {personality} personality is compatible with this career."
        )


    if skills.strip():

        reasons.append(
            f"Your current skills ({skills}) contribute to the match."
        )


    if academic_performance >= 85:

        reasons.append(
            "Your strong academic performance supports the recommendation."
        )


    if aptitude >= 75:

        reasons.append(
            "Your aptitude score indicates strong learning potential."
        )


    if not reasons:

        reasons.append(
            "The recommendation is based on patterns learned from the trained ML model."
        )


    return reasons


# ============================================================
# IMPROVEMENT GENERATOR
# ============================================================

def improvement_plan(career):

    career_lower = career.lower()


    if "data scientist" in career_lower:

        return [

            "Strengthen Python and SQL.",

            "Improve statistics and data analysis.",

            "Build machine learning projects."

        ]


    elif "ml/ai" in career_lower:

        return [

            "Improve Python programming.",

            "Learn machine learning and deep learning.",

            "Build practical AI projects."

        ]


    elif "software engineer" in career_lower:

        return [

            "Improve programming fundamentals.",

            "Practice Data Structures and Algorithms.",

            "Build real-world software projects."

        ]


    elif "cyber security" in career_lower:

        return [

            "Learn networking and Linux.",

            "Practice cybersecurity labs.",

            "Build security-related projects."

        ]


    elif "cloud engineer" in career_lower:

        return [

            "Learn AWS or Azure.",

            "Improve Linux and networking.",

            "Build cloud deployment projects."

        ]


    elif career_lower in [

        "business analyst",
        "entrepreneur",
        "sales executive",
        "marketing executive",
        "financial analyst",
        "hr manager"

    ]:

        return [

            "Improve Excel and business analysis skills.",

            "Strengthen communication and presentation.",

            "Gain practical business experience."

        ]


    return [

        "Build practical projects related to the career.",

        "Improve domain knowledge.",

        "Gain internship or certification experience."

    ]


# ============================================================
# RECOMMEND BUTTON
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)


if st.button(
    "🚀 ANALYZE MY CAREER",
    use_container_width=True
):


    if not skills.strip():

        st.warning(
            "⚠️ Please enter at least one skill before analyzing your profile."
        )

        st.stop()


    try:

        # ================================================
        # MODEL INPUT
        # ================================================

        student_data = create_input()


        # ================================================
        # PREDICTION
        # ================================================

        probabilities = model.predict_proba(
            student_data
        )[0]


        careers = model.classes_


        results = pd.DataFrame({

            "Career": careers,

            "Confidence": probabilities * 100

        })


        # ================================================
        # GOAL ALIGNMENT
        # ================================================

        results["Goal Alignment"] = results[
            "Career"
        ].apply(
            calculate_goal_alignment
        )


        # ================================================
        # FINAL SCORE
        # ================================================

        results["Final Score"] = (

            results["Confidence"] * 0.60

            + results["Goal Alignment"] * 0.40

        )


        results = results.sort_values(

            "Final Score",

            ascending=False

        ).reset_index(drop=True)


        top5 = results.head(5)


        # ================================================
        # RESULTS HEADER
        # ================================================

        st.markdown(
            '<div class="section-title">🏆 Your Career Matches</div>',
            unsafe_allow_html=True
        )


        st.markdown(
            '<div class="section-description">Our AI has analyzed your profile and ranked the strongest career matches.</div>',
            unsafe_allow_html=True
        )


        # ================================================
        # CAREER CARDS
        # ================================================

        for i, row in top5.iterrows():

            rank = i + 1

            career = row["Career"]

            final_score = row["Final Score"]

            confidence = row["Confidence"]

            goal_alignment = row["Goal Alignment"]


            st.markdown(
                f"""
                <div class="career-card">

                <div class="rank">
                #{rank} CAREER MATCH
                </div>

                <div class="career-name">
                {career}
                </div>

                <br>

                <div style="display:flex; gap:40px;">

                <div>
                <div style="color:#94A3B8;">
                Final Match
                </div>

                <div class="score">
                {final_score:.1f}%
                </div>
                </div>

                <div>
                <div style="color:#94A3B8;">
                Model Confidence
                </div>

                <div style="font-size:25px;font-weight:700;">
                {confidence:.1f}%
                </div>
                </div>

                <div>
                <div style="color:#94A3B8;">
                Goal Alignment
                </div>

                <div style="font-size:25px;font-weight:700;color:#06B6D4;">
                {goal_alignment:.0f}%
                </div>
                </div>

                </div>

                </div>
                """,
                unsafe_allow_html=True
            )


        # ================================================
        # BEST MATCH
        # ================================================

        best_career = top5.iloc[0]["Career"]

        best_score = top5.iloc[0]["Final Score"]


        st.markdown(
            f"""
            <div class="best-match">

            <div class="best-title">
            ⭐ BEST CAREER MATCH
            </div>

            <div class="best-career">
            {best_career}
            </div>

            <div style="color:#94A3B8;margin-top:8px;">
            Overall Match Score
            </div>

            <div style="font-size:28px;font-weight:800;color:#06B6D4;">
            {best_score:.1f}%
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


        # ================================================
        # WHY RECOMMENDED
        # ================================================

        st.markdown(
            '<div class="section-title">💡 Why is this career recommended?</div>',
            unsafe_allow_html=True
        )


        reasons = get_reasons(best_career)


        for reason in reasons:

            st.markdown(

                f"""
                <div class="insight">
                ✓ &nbsp; {reason}
                </div>
                """,

                unsafe_allow_html=True

            )


        # ================================================
        # IMPROVEMENT
        # ================================================

        st.markdown(
            '<div class="section-title">📈 What should you improve?</div>',
            unsafe_allow_html=True
        )


        st.markdown(
            f"""
            <div class="section-description">
            To become stronger for <b>{best_career}</b>,
            focus on these areas:
            </div>
            """,
            unsafe_allow_html=True
        )


        suggestions = improvement_plan(best_career)


        for suggestion in suggestions:

            st.markdown(

                f"""
                <div class="improvement">
                🔸 &nbsp; {suggestion}
                </div>
                """,

                unsafe_allow_html=True

            )


        # ================================================
        # PROFILE ANALYSIS
        # ================================================

        st.markdown(
            '<div class="section-title">📊 Profile Analysis</div>',
            unsafe_allow_html=True
        )


        a1, a2, a3 = st.columns(3)


        with a1:

            st.metric(
                "Aptitude",
                f"{aptitude:.1f}/100"
            )


        with a2:

            st.metric(
                "Academic Performance",
                f"{academic_performance:.1f}%"
            )


        with a3:

            st.metric(
                "Career Goal",
                career_goal
            )


        # ================================================
        # DATA TABLE
        # ================================================

        st.markdown(
            '<div class="section-title">📋 Recommendation Breakdown</div>',
            unsafe_allow_html=True
        )


        display_results = top5[
            [
                "Career",
                "Confidence",
                "Goal Alignment",
                "Final Score"
            ]
        ].copy()


        display_results[
            "Confidence"
        ] = display_results[
            "Confidence"
        ].round(2)


        display_results[
            "Goal Alignment"
        ] = display_results[
            "Goal Alignment"
        ].round(2)


        display_results[
            "Final Score"
        ] = display_results[
            "Final Score"
        ].round(2)


        st.dataframe(

            display_results,

            use_container_width=True,

            hide_index=True

        )


    except Exception as e:

        st.error(
            "❌ Something went wrong while generating recommendations."
        )

        st.exception(e)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

    🤖 <b>AI Career Navigator</b>

    <br>

    Machine Learning powered career recommendation system

    <br><br>

    Built using Python • Scikit-learn • Streamlit

    </div>
    """,
    unsafe_allow_html=True
)