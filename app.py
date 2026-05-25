import joblib
import pandas as pd
import streamlit as st
# model = joblib.load("model/career_model.pkl")
# feature_columns = joblib.load("model/feature_columns.pkl")
from questions.python_questions import questions as python_questions
from questions.ml_questions import questions as ml_questions
from questions.web_questions import questions as web_questions
from questions.cyber_questions import questions as cyber_questions
# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Smart Career Recommender",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------------
# MODERN UI CSS
# -----------------------------------

st.markdown("""
<style>

/* MAIN APP */
.stApp {
    background:
    radial-gradient(circle at top left, rgba(0,255,170,0.15), transparent 25%),
    radial-gradient(circle at bottom right, rgba(0,150,255,0.15), transparent 25%),
    linear-gradient(135deg, #020617, #071226, #0f172a, #111827);
    color: white;
    overflow-x: hidden;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617, #071226, #0f172a);
    border-right: 1px solid rgba(255,255,255,0.08);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* RADIO BUTTON TEXT */
.stRadio label {
    color: white !important;
    font-size: 16px;
    font-weight: 500;
}

/* TITLES */
h1, h2, h3, h4, h5 {
    color: white !important;
}

/* ===== INPUT FIX - THE MAIN FIX ===== */
input[type="text"],
input[type="number"],
input[type="email"],
input[type="password"],
textarea {
    color: white !important;
    background-color: #1e293b !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 12px !important;
    caret-color: #00ffaa !important;
}

input[type="text"]::placeholder,
input[type="number"]::placeholder,
textarea::placeholder {
    color: rgba(255,255,255,0.4) !important;
}

/* Streamlit specific input wrappers */
.stTextInput > div > div > input {
    color: white !important;
    background-color: #1e293b !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 12px !important;
}

.stTextInput > div > div > input::placeholder {
    color: rgba(255,255,255,0.4) !important;
}

/* Selectbox */
.stSelectbox > div > div {
    background-color: #1e293b !important;
    color: white !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
}

.stSelectbox div[data-baseweb="select"] span {
    color: white !important;
}

/* Multiselect */
.stMultiSelect > div > div {
    background-color: #1e293b !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
}

.stMultiSelect div[data-baseweb="select"] span {
    color: white !important;
}

/* Dropdown popover options */
div[data-baseweb="popover"] li {
    background-color: #0f172a !important;
    color: white !important;
}

div[data-baseweb="popover"] li:hover {
    background-color: rgba(0,255,170,0.15) !important;
}

/* Number input */
.stNumberInput > div > div > input {
    color: white !important;
    background-color: #1e293b !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 12px !important;
}

/* ===== HERO SECTION ===== */
.hero {
    padding: 50px;
    border-radius: 30px;
    background: linear-gradient(135deg, rgba(0,255,170,0.08), rgba(0,150,255,0.08));
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 8px 40px rgba(0,0,0,0.4);
    margin-bottom: 40px;
    position: relative;
    overflow: hidden;
}

.hero::before {
    content: "";
    position: absolute;
    width: 500px;
    height: 500px;
    background: radial-gradient(rgba(0,255,170,0.15), transparent 70%);
    top: -200px;
    right: -100px;
    border-radius: 50%;
}

/* ===== GLASS CARDS ===== */
.card {
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(16px);
    border-radius: 24px;
    padding: 25px;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 8px 32px rgba(0,0,0,0.35);
    transition: 0.4s;
    color: white;
    margin-bottom: 20px;
}

.card:hover {
    transform: translateY(-8px);
    border: 1px solid rgba(0,255,170,0.3);
    box-shadow: 0 12px 40px rgba(0,255,170,0.12);
}

.card p, .card h1, .card h2, .card h3, .card li {
    color: white !important;
}

/* ===== BUTTONS ===== */
.stButton > button {
    width: 100%;
    border-radius: 16px;
    height: 3.5em;
    background: linear-gradient(90deg, #00ffaa, #00c3ff);
    color: black;
    font-size: 18px;
    font-weight: bold;
    border: none;
    transition: 0.4s;
    box-shadow: 0 0 20px rgba(0,255,170,0.2);
}

.stButton > button:hover {
    transform: scale(1.03);
    background: linear-gradient(90deg, #00e09a, #00aaff);
    box-shadow: 0 0 30px rgba(0,255,170,0.4);
}

/* ===== PROGRESS BAR ===== */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #00ffaa, #00c3ff);
}

/* ===== SUCCESS BOX ===== */
.stSuccess {
    background: rgba(0,255,170,0.08);
    border: 1px solid rgba(0,255,170,0.2);
    color: white;
}

/* ===== FEATURE TITLE ===== */
.feature-title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 12px;
}

/* ===== RECOMMENDATION BOX ===== */
.recommendation {
    padding: 25px;
    border-radius: 20px;
    background: linear-gradient(135deg, rgba(34,197,94,0.2), rgba(16,185,129,0.1));
    border: 1px solid rgba(34,197,94,0.3);
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)
# -----------------------------------
# LOAD MODEL FILES
# -----------------------------------

model = joblib.load("model/career_model.pkl")
feature_columns = joblib.load("model/feature_columns.pkl")
encoders = joblib.load("model/label_encoder.pkl")
career_encoder = joblib.load("model/career_encoder.pkl")
# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.title("🚀 Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "Home",
        "Career Prediction",
        "Skill Assessment",
        "Dashboard",
        "About"
    ]
)


# -----------------------------------
# HOME PAGE
# -----------------------------------

if page == "Home":

    st.markdown("""
    <div class="hero">

    <h1>
    🧭 PathGenie AI
    </h1>

    <h3>
    AI-Powered Career Guidance Platform
    </h3>

    <p>
    Discover your perfect career path using:
    AI, Machine Learning, Skill Assessment,
    and Personalized Career Analytics.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("""
    Discover the best career path based on:
    - Skills
    - Interests
    - Certifications
    - Education
    - Academic Performance
    """)

    # FEATURE CARDS

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("""
        <div class="card">

        <h2>🎯 Career Prediction</h2>

        <p>
        Get AI-powered career recommendations
        based on skills, interests, certifications,
        and academic performance.
        </p>

        <br>

        <h4 style='color:#00ffaa;'>
        ✔ Personalized Career Mapping
        </h4>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="card">

        <h2>🧠 Skill Assessment</h2>

        <p>
        Analyze technical readiness using
        intelligent MCQ-based assessments
        across multiple domains.
        </p>

        <br>

        <h4 style='color:#00ffaa;'>
        ✔ AI Readiness Analysis
        </h4>

        </div>
        """, unsafe_allow_html=True)

    with col3:

        st.markdown("""
        <div class="card">

        <h2>📊 Career Analytics</h2>

        <p>
        Track performance, identify weak areas,
        and receive personalized improvement
        roadmaps.
        </p>

        <br>

        <h4 style='color:#00ffaa;'>
        ✔ Smart Improvement Insights
        </h4>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # PLATFORM HIGHLIGHTS

    st.subheader("⚡ Platform Highlights")

    stat1, stat2, stat3, stat4 = st.columns(4)

    with stat1:
        st.metric("Career Domains", "15+")

    with stat2:
        st.metric("Skills Analyzed", "50+")

    with stat3:
        st.metric("AI Assessments", "100+")

    with stat4:
        st.metric("Personalized Guidance", "24/7")

    # AI ENGINE SECTION

    st.markdown("""

    <div class="recommendation">

    <h2>
    🤖 AI Career Intelligence Engine
    </h2>

    <p style="font-size:18px;">

    Our intelligent recommendation engine analyzes:

    ✔ Skills  
    ✔ Interests  
    ✔ Certifications  
    ✔ Academic Performance  
    ✔ Technical Readiness  

    to generate personalized career guidance
    and learning roadmaps.

    </p>

    </div>

    """, unsafe_allow_html=True)   

# -----------------------------------
# CAREER PREDICTION PAGE
# -----------------------------------
if page == "Career Prediction":

    st.title("🎯 Career Prediction")
    st.markdown("### Fill Your Details")

    col1, col2 = st.columns(2)

    with col1:
        name           = st.text_input("Enter Your Name")
        gender         = st.selectbox("Select Gender", ["Male", "Female", "Prefer not to say"])
        ug_course      = st.text_input("UG Course")
        specialization = st.text_input("Specialization")
        cgpa           = st.slider("CGPA", 0.0, 10.0, 7.0)

    with col2:
        interests = st.multiselect("Select Interests",
            ["AI", "Web Development", "Cyber Security",
             "Cloud Computing", "Data Science", "UI/UX"])
        skills = st.multiselect("Select Skills",
            ["Python", "Java", "Machine Learning",
             "HTML/CSS", "React", "SQL", "Networking"])
        certification      = st.selectbox("Any Certification?", ["Yes", "No"])
        masters            = st.selectbox("Masters Completed?", ["Yes", "No"])
        certificate_course = st.text_input("Certificate Course")
        working            = st.selectbox("Currently Working?", ["Yes", "No"])

    # ── Everything inside the button block ──────────────────
    if st.button("🚀 Predict Career"):

        # 1. Build raw dataframe
        input_data = {
            "gender":             gender,
            "ug_course":          ug_course,
            "specialization":     specialization,
            "interests":          ", ".join(interests),
            "skills":             ", ".join(skills),
            "cgpa":               cgpa,
            "certification":      certification,
            "certificate_course": certificate_course,
            "working":            working,
            "masters":            masters
        }
        input_df = pd.DataFrame([input_data])

        # 2. Encode
        gender_map  = {"Male": 1, "Female": 0, "Prefer not to say": 2}
        yes_no_map  = {"Yes": 1, "No": 0}

        input_df["gender"]        = input_df["gender"].map(gender_map)
        input_df["certification"] = input_df["certification"].map(yes_no_map)
        input_df["masters"]       = input_df["masters"].map(yes_no_map)
        input_df["working"]       = input_df["working"].map(yes_no_map)

        text_columns = ["ug_course", "specialization",
                        "interests", "skills", "certificate_course"]
        for col in text_columns:
            input_df[col] = input_df[col].astype("category").cat.codes

        # 3. Align columns to what the model expects
        input_df = input_df.reindex(columns=feature_columns, fill_value=0)

        # 4. Convert everything to numeric and fill nulls
        for col in input_df.columns:
            input_df[col] = pd.to_numeric(input_df[col], errors="coerce")
        input_df = input_df.fillna(0)

        # 5. Predict
        prediction       = model.predict(input_df)
        predicted_career = career_encoder.inverse_transform(prediction)[0]

        # 6. Readiness score
        readiness_score  = 60
        readiness_score += len(skills) * 5
        if cgpa >= 8:          readiness_score += 10
        if certification == "Yes": readiness_score += 10
        readiness_score  = min(readiness_score, 100)

        # 7. Save to session state
        st.session_state.name             = name
        st.session_state.skills           = skills
        st.session_state.interests        = interests
        st.session_state.predicted_career = predicted_career
        st.session_state.readiness_score  = readiness_score

        # 8. Show result
        st.success(f"🎯 Recommended Career: **{predicted_career}**")
        st.info(f"⭐ Career Readiness Score: **{readiness_score}%**")
        st.progress(readiness_score / 100)
# -----------------------------------
# SKILL ASSESSMENT PAGE
# -----------------------------------

elif page == "Skill Assessment":

    st.title("🧠 Skill Assessment")

    st.write("""
    Analyze your technical readiness
    using intelligent assessments.
    """)

    # -----------------------------------
    # SELECT SKILL
    # -----------------------------------

    skill = st.selectbox(
        "Choose Skill",
        [
            "Python",
            "Machine Learning",
            "Web Development",
            "Cyber Security"
        ]
    )

    # -----------------------------------
    # LOAD QUESTIONS
    # -----------------------------------

    if skill == "Python":

        selected_questions = python_questions

    elif skill == "Machine Learning":

        selected_questions = ml_questions

    elif skill == "Web Development":

        selected_questions = web_questions

    else:

        selected_questions = cyber_questions

    # -----------------------------------
    # STORE USER ANSWERS
    # -----------------------------------

    user_answers = []

    # -----------------------------------
    # QUESTION LOOP
    # -----------------------------------

    for i, q in enumerate(selected_questions):

        st.markdown("---")

        st.subheader(f"Q{i+1}. {q['question']}")

        answer = ""

        # -----------------------------------
        # MCQ QUESTIONS
        # -----------------------------------

        if q["type"] == "mcq":

            answer = st.radio(
                "Choose Answer",
                q["options"],
                key=f"mcq_{i}"
            )

        # -----------------------------------
        # FILL BLANK / SCENARIO / CODE
        # -----------------------------------

        else:

            answer = st.text_input(
                "Your Answer",
                key=f"text_{i}"
            )

        # STORE ANSWER

        user_answers.append({

            "question": q,

            "answer": answer
        })

    # -----------------------------------
    # SUBMIT BUTTON
    # -----------------------------------

    if st.button("🚀 Submit Assessment"):

        score = 0

        weak_areas = []

        correct_answers = 0

        # -----------------------------------
        # CHECK ANSWERS
        # -----------------------------------

        for item in user_answers:

            question = item["question"]

            user_answer = str(
                item["answer"]
            ).strip().lower()

            correct_answer = str(
                question["answer"]
            ).strip().lower()

            # CORRECT

            if user_answer == correct_answer:

                score += 5

                correct_answers += 1

            # WRONG

            else:

                weak_areas.append(
                    question["type"]
                )

        # -----------------------------------
        # FINAL SCORE
        # -----------------------------------

        percentage = score

        # -----------------------------------
        # STORE SESSION DATA
        # -----------------------------------

        st.session_state.assessment_skill = skill

        st.session_state.assessment_score = percentage

        st.session_state.correct_answers = correct_answers

        st.session_state.weak_areas = weak_areas

        # -----------------------------------
        # RESULT SECTION
        # -----------------------------------

        st.success(
            f"✅ Your Score: {percentage}/100"
        )

        st.info(
            f"✔ Correct Answers: {correct_answers}/20"
        )

        # -----------------------------------
        # PERFORMANCE ANALYSIS
        # -----------------------------------

        if percentage >= 90:

            st.success("""
            🚀 Expert Level Performance

            You are highly industry-ready
            with strong technical skills.
            """)

        elif percentage >= 70:

            st.info("""
            👍 Strong Performance

            Your fundamentals are solid.
            Improve advanced concepts
            and coding practice.
            """)

        elif percentage >= 50:

            st.warning("""
            ⚠ Intermediate Performance

            You have basic understanding
            but need more practical exposure.
            """)

        else:

            st.error("""
            ❌ Needs Improvement

            Focus more on fundamentals,
            coding practice,
            and real-world problem solving.
            """)

        # -----------------------------------
        # WEAK AREA ANALYSIS
        # -----------------------------------

        st.markdown("---")

        st.subheader("📉 Weak Areas Analysis")

        if len(weak_areas) == 0:

            st.success("""
            Excellent!
            No major weak areas detected.
            """)

        else:

            unique_weak_areas = list(
                set(weak_areas)
            )

            for area in unique_weak_areas:

                st.warning(f"Improve: {area}")

        # -----------------------------------
        # RECOMMENDED STUDY PLAN
        # -----------------------------------

        st.markdown("---")

        st.subheader("📚 Recommended Study Plan")

        if percentage >= 90:

            st.success("""
            Recommended Daily Practice:
            1 Hour/Day

            Focus on:
            - Advanced Projects
            - Interview Preparation
            - System Design
            """)

        elif percentage >= 70:

            st.info("""
            Recommended Daily Practice:
            2 Hours/Day

            Focus on:
            - Coding Practice
            - Problem Solving
            - Real-world Projects
            """)

        else:

            st.warning("""
            Recommended Daily Practice:
            3 Hours/Day

            Focus on:
            - Fundamentals
            - Beginner Projects
            - Hands-on Practice
            """)
# -----------------------------------
# DASHBOARD PAGE
# -----------------------------------

elif page == "Dashboard":

    st.title("📊 Personalized Career Dashboard")
    st.markdown("---")

    # ── User Profile ─────────────────────────────────────────
    st.subheader("👤 User Profile")

    name             = st.session_state.get("name", "Not provided")
    interests        = st.session_state.get("interests", [])
    skills           = st.session_state.get("skills", [])
    predicted_career = st.session_state.get("predicted_career", "No prediction yet")
    readiness_score  = st.session_state.get("readiness_score", 0)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class="card">
            <h3>👨‍🎓 Name</h3>
            <p>{name}</p>
            <h3>📚 Interests</h3>
            <p>{", ".join(interests) if interests else "None selected"}</p>
            <h3>💻 Skills</h3>
            <p>{", ".join(skills) if skills else "None selected"}</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="card">
            <h3>🎯 Recommended Career</h3>
            <h1 style='color:#00ffaa;'>{predicted_career}</h1>
            <h3>⭐ Readiness Score</h3>
            <h2>{readiness_score}%</h2>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

       # ── ASSESSMENT ANALYTICS ───────────────────────────────

    st.subheader("🧠 Assessment Analytics")

    assessment_skill = st.session_state.get(
        "assessment_skill",
        "Not Attempted"
    )

    assessment_score = st.session_state.get(
        "assessment_score",
        0
    )

    weak_areas = st.session_state.get(
        "weak_areas",
        []
    )

    correct_answers = st.session_state.get(
        "correct_answers",
        0
    )

    # ANALYTICS CARDS

    ana_col1, ana_col2, ana_col3 = st.columns(3)

    with ana_col1:

        st.metric(
            "Skill Tested",
            assessment_skill
        )

    with ana_col2:

        st.metric(
            "Assessment Score",
            f"{assessment_score}/100"
        )

    with ana_col3:

        st.metric(
            "Correct Answers",
            f"{correct_answers}/20"
        )

    st.markdown("---")

    # ── PERFORMANCE METER ─────────────────────────────────

    st.subheader("📊 Career Readiness Meter")

    st.progress(readiness_score / 100)

    st.info(
        f"Overall Career Readiness: {readiness_score}%"
    )

    st.markdown("---")

    # ── WEAK AREA ANALYSIS ────────────────────────────────

    st.subheader("📉 Weak Areas Analysis")

    if len(weak_areas) == 0:

        st.success("""
        Excellent!
        No major weak areas detected.
        """)

    else:

        unique_weak_areas = list(set(weak_areas))

        for area in unique_weak_areas:

            st.warning(f"⚠ Improve: {area}")

    st.markdown("---")

    # ── AI IMPROVEMENT SUGGESTIONS ────────────────────────

    st.subheader("🤖 AI Improvement Suggestions")

    sug_col1, sug_col2 = st.columns(2)

    with sug_col1:

        st.markdown(f"""
        <div class="card">

        <h3>🎯 Career Match</h3>

        <h2 style='color:#00ffaa;'>
        {predicted_career}
        </h2>

        <p>
        Based on your assessment and profile,
        this career best matches your skills
        and interests.
        </p>

        </div>
        """, unsafe_allow_html=True)

    with sug_col2:

        if assessment_score >= 80:

            practice_time = "1 Hour/Day"

            focus = """
            - Advanced Projects
            - Interview Preparation
            - System Design
            """

        elif assessment_score >= 50:

            practice_time = "2 Hours/Day"

            focus = """
            - Coding Practice
            - SQL
            - Real-world Projects
            """

        else:

            practice_time = "3 Hours/Day"

            focus = """
            - Fundamentals
            - Beginner Projects
            - Problem Solving
            """

        st.markdown(f"""
        <div class="card">

        <h3>📚 Recommended Plan</h3>

        <p>
        Recommended Practice Time:
        </p>

        <h2 style='color:#00ffaa;'>
        {practice_time}
        </h2>

        <p>
        Focus Areas:
        </p>

        <p>
        {focus}
        </p>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # ── FINAL AI INSIGHT ──────────────────────────────────

    st.subheader("🚀 Final AI Insight")

    if assessment_score >= 80:

        st.success(f"""
        You are highly prepared for the role of
        {predicted_career}.

        Continue advanced practice and
        project development for placements.
        """)

    elif assessment_score >= 50:

        st.warning(f"""
        You have moderate readiness for
        {predicted_career}.

        Improve practical implementation
        and coding consistency.
        """)

    else:

        st.error(f"""
        You currently need stronger fundamentals
        for becoming a successful
        {predicted_career}.

        Focus on skill-building and
        consistent daily learning.
        """)

    # ── AI Career Insights ───────────────────────────────────
    st.subheader("🤖 AI Career Insights")

    ins_col1, ins_col2 = st.columns(2)

    with ins_col1:
        st.markdown(f"""
        <div class="card">
            <h3>🎯 Best Career Match</h3>
            <h2 style='color:#00ffaa;'>{predicted_career}</h2>
            <p>Your profile strongly aligns with AI and Data Science career paths.</p>
        </div>
        """, unsafe_allow_html=True)

    with ins_col2:
        st.markdown("""
        <div class="card">
            <h3>📈 Improvement Suggestion</h3>
            <p>Focus more on:</p>
            <ul>
                <li>SQL Optimization</li>
                <li>Deep Learning</li>
                <li>DSA Practice</li>
            </ul>
            <p>Recommended Practice: <b>2 Hours/Day</b></p>
        </div>
        """, unsafe_allow_html=True)
# ════════════════════════════════════════════════════════════
# ABOUT PAGE
# ════════════════════════════════════════════════════════════

elif page == "About":

    st.markdown("""
    <h1 style="
    font-size:60px;
    font-weight:900;
    background:linear-gradient(
    90deg,
    #00ffaa,
    #00c3ff,
    #7c4dff
    );
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    ">

    PathGenie AI

    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h3 style="
    color:#d1d5db;
    margin-bottom:20px;
    ">
    Next-Generation AI Career Intelligence Platform
    </h3>
    """, unsafe_allow_html=True)

    st.write("""
    PathGenie AI is an advanced intelligent career guidance
    and analytics platform designed to help students and learners
    discover ideal career paths using Artificial Intelligence
    and Machine Learning.
    """)

    st.markdown("---")

    # FEATURE CARDS

    col1, col2, col3 = st.columns(3)

    with col1:

        st.info("""
        💻 Technical Skills
        
        Analyze programming,
        development,
        and problem-solving abilities.
        """)

        st.info("""
        📊 Smart Analytics
        
        Track strengths,
        weak areas,
        and growth insights.
        """)

    with col2:

        st.success("""
        🎯 Career Interests
        
        Match user passion
        with career domains.
        """)

        st.success("""
        🚀 AI Recommendations
        
        Generate personalized
        career roadmaps instantly.
        """)

    with col3:

        st.warning("""
        📚 Academic Performance
        
        Evaluate CGPA,
        certifications,
        and specialization.
        """)

        st.warning("""
        🌐 Intelligent Dashboard
        
        Visualize career readiness
        and analytics.
        """)

    st.markdown("---")

    # FOOTER

    footer_col1, footer_col2 = st.columns([4, 2])

    with footer_col2:

        st.markdown("""
        <div style="
        text-align:right;
        padding:20px;
        border-radius:20px;
        background:rgba(255,255,255,0.04);
        border:1px solid rgba(255,255,255,0.08);
        ">

        <p style="
        font-size:13px;
        color:gray;
        letter-spacing:2px;
        ">
        DESIGNED & DEVELOPED BY
        </p>

        <h1 style="
        font-size:38px;
        font-weight:900;
        background:linear-gradient(
        90deg,
        #00ffaa,
        #00c3ff,
        #7c4dff
        );
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
        ">
        ✨ Harshitha ✨
        </h1>

        </div>
        """, unsafe_allow_html=True)