import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Career Recommender", layout="wide")

# ---------------- SAFE CSS ----------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

/* Section Title */
.section-title {
    font-size: 26px;
    font-weight: 600;
    margin-bottom: 15px;
}

/* Card */
.card {
    background: #1e293b;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 15px;
    color: white;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}

/* Best Card */
.best-card {
    background: linear-gradient(135deg, #16a34a, #22c55e);
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
    color: white;
}

/* ✅ FIX ALL SELECTBOXES */
div[data-baseweb="select"] > div {
    background-color: #1e293b !important;
    color: white !important;
}

div[role="listbox"] {
    background-color: #1e293b !important;
}

div[role="option"] {
    color: white !important;
}

div[role="option"]:hover {
    background-color: #334155 !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- STUDENT PROFILE ----------------
st.markdown('<div class="section-title">👤 Student Profile</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    aptitude = st.number_input("Aptitude Score", 0, 100, 85)

    interest = st.selectbox(
        "Interest",
        [
            "Data Science",
            "AI",
            "Web Development",
            "Cyber Security",
            "Cloud Computing",
            "Software Engineering"
        ]
    )

with col2:
    academics = st.number_input("Academic Performance", 0, 100, 75)

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

skills = st.text_area("Skills", "Python, AWS, SQL, Linux")

goal = st.selectbox(
    "Career Goal",
    [
        "Data Scientist",
        "AI Engineer",
        "Software Engineer",
        "Cloud Engineer",
        "Cybersecurity Analyst"
    ]
)
skill_map = {
    "Data Scientist": [
        "Python", "Machine Learning", "Statistics", "SQL", "Data Visualization"
    ],
    "ML/AI Engineer": [
        "Deep Learning", "TensorFlow/PyTorch", "Python", "Model Deployment", "MLOps"
    ],
    "Data Analyst": [
        "Excel", "SQL", "Power BI/Tableau", "Python", "Data Cleaning"
    ],
    "Cloud Engineer": [
        "AWS/Azure", "Docker", "Kubernetes", "Linux", "Networking"
    ],
    "Software Developer": [
        "Data Structures", "Algorithms", "Java/Python", "Git", "System Design"
    ]
}
# ---------------- BUTTON ----------------
if st.button("Get Recommendations 🚀"):

    results = [
        ("Data Scientist", 48.41, 8.52),
        ("ML/AI Engineer", 40.59, 7.80),
        ("Data Analyst", 35.20, 7.10),
        ("Cloud Engineer", 30.15, 6.50),
        ("Software Developer", 28.75, 6.20),
    ]

    # ✅ FUNCTION MUST BE SAME INDENT LEVEL AS results
    def show_card(rank, career, score, confidence):
        skills = skill_map.get(career, [])

        st.markdown(f"""
        <div class="card">
            <h4>🏅 Rank #{rank}</h4>
            <h2>{career}</h2>
            <p><b>Final Score:</b> {score}%</p>
            <p><b>Model Confidence:</b> {confidence}%</p>
        </div>
        """, unsafe_allow_html=True)

        if skills:
            st.markdown("**🧠 Recommended Skills to Learn:**")
            st.markdown(" ".join([f"`{s}`" for s in skills]))

    # ✅ LOOP ALSO SAME LEVEL
    for i, (career, score, conf) in enumerate(results, start=1):
        show_card(i, career, score, conf)

    # ---------------- PROGRESS ----------------
    st.markdown('<div class="section-title">📊 Capability Match</div>', unsafe_allow_html=True)

    for career, score, _ in results:
        st.write(career)
        st.progress(int(score))


