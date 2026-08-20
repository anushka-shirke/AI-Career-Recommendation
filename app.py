import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Career Recommender", layout="wide")

# ---------------- GLOBAL CSS ----------------
st.markdown("""
<style>
/* Background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

/* Section Titles */
.section-title {
    font-size: 28px;
    font-weight: 600;
    margin-bottom: 15px;
}

/* Card */
.card {
    background: #1e293b;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 15px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    color: white;
}

/* Best Card */
.best-card {
    background: linear-gradient(135deg, #16a34a, #22c55e);
    color: white;
    padding: 20px;
    border-radius: 12px;
    font-weight: 500;
    margin-bottom: 20px;
}

/* Inputs */
input, textarea {
    background-color: #0f172a !important;
    color: white !important;
}

/* Labels */
label {
    color: white !important;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

# ---------------- STUDENT PROFILE ----------------
st.markdown('<div class="section-title">👤 Student Profile</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    aptitude = st.number_input("Aptitude Score", 0, 100, 85)
    interest = st.selectbox("Interest", ["Data Science", "AI", "Web Development"])

with col2:
    academics = st.number_input("Academic Performance", 0, 100, 75)
    personality = st.selectbox("Personality Type", ["Realistic", "Investigative", "Artistic"])

skills = st.text_area("Skills", "Python, AWS, SQL, Linux")
goal = st.selectbox("Career Goal", ["Data Scientist", "AI Engineer", "Software Engineer"])

# ---------------- BUTTON ----------------
if st.button("Get Recommendations 🚀"):

    # ---------------- RESULTS ----------------
    st.markdown('<div class="section-title">🏆 Your Top Career Recommendations</div>', unsafe_allow_html=True)

    # Best Match
    st.markdown("""
    <div class="best-card">
        <b>Best Match:</b> Data Scientist — Final Score: 48.41%
    </div>
    """, unsafe_allow_html=True)

    # ---------------- CARD FUNCTION ----------------
    def show_card(rank, career, score, confidence):
        st.markdown(f"""
        <div class="card">
            <h4>🏅 Rank #{rank}</h4>
            <h2>{career}</h2>
            <p><b>Final Score:</b> {score}%</p>
            <p><b>Model Confidence:</b> {confidence}%</p>
        </div>
        """, unsafe_allow_html=True)

    # ---------------- DISPLAY TOP 5 ----------------
    show_card(1, "Data Scientist", 48.41, 8.52)
    show_card(2, "ML/AI Engineer", 40.59, 7.80)
    show_card(3, "Data Analyst", 35.20, 7.10)
    show_card(4, "Cloud Engineer", 30.15, 6.50)
    show_card(5, "Software Developer", 28.75, 6.20)

    # ---------------- PROGRESS SECTION ----------------
    st.markdown('<div class="section-title">📊 Capability Match</div>', unsafe_allow_html=True)

    st.write("Data Scientist")
    st.progress(48)

    st.write("ML/AI Engineer")
    st.progress(40)

    st.write("Data Analyst")
    st.progress(35)

    st.write("Cloud Engineer")
    st.progress(30)

    st.write("Software Developer")
    st.progress(28)
