import os
import random
import datetime
import streamlit as st
import streamlit.components.v1 as components

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(

    page_title="Adaptive Explainable Phishing Detection",

    page_icon="🛡️",

    layout="wide",

    initial_sidebar_state="expanded"

)

# ==========================================================
# LOAD CSS
# ==========================================================

if os.path.exists("assets/style.css"):

    with open("assets/style.css") as f:

        st.markdown(

            f"<style>{f.read()}</style>",

            unsafe_allow_html=True

        )

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.markdown("# 🛡️")

    st.markdown("## Adaptive Explainable")
    st.markdown("## Phishing Detection")

    st.divider()

    st.success("AI Powered Cyber Security")

    st.info("Real-Time Threat Detection")

    st.divider()

    st.markdown("### 👨‍💻 Developers")

    st.write("**Animesh Kushwaha**")

    st.write("**Madeeha Laiq**")

    st.divider()

    st.caption("© 2026 All Rights Reserved")

# ==========================================================
# LIVE CLOCK
# ==========================================================

clock_col, blank = st.columns([2,6])

with clock_col:

    components.html("""

    <div id="clock"

    style="

    background:#102036;

    color:#00E676;

    padding:12px;

    border-radius:15px;

    font-size:22px;

    font-weight:bold;

    text-align:center;

    ">

    </div>

    <script>

    function updateClock(){

    const now=new Date();

    document.getElementById("clock").innerHTML=

    now.toLocaleTimeString();

    }

    setInterval(updateClock,1000);

    updateClock();

    </script>

    """,height=70)

# ==========================================================
# HERO
# ==========================================================

st.markdown("""

<div class="hero">

<h1>

🛡️ Adaptive Explainable Phishing Detection System

</h1>

<p>

AI Powered Cyber Security Platform for

Real-Time URL & Email Phishing Detection

</p>

</div>

""",unsafe_allow_html=True)

# ==========================================================
# CYBER QUOTES
# ==========================================================

components.html("""

<div id="quote"

style="

background:#102036;

padding:18px;

border-radius:15px;

color:white;

font-size:20px;

font-weight:500;

border-left:5px solid #00C8FF;

">

Loading Cyber Quote...

</div>

<script>

const quotes=[

"🛡️ Think Before You Click.",

"🔒 Verify Every URL Before Opening.",

"⚠️ Never Trust Urgent Emails.",

"🌐 Cyber Awareness Is Your Best Defense.",

"📧 Phishing Starts With Curiosity.",

"🚨 Protect Your Credentials.",

"🧠 AI + Rule Engine = Better Security.",

"💻 Stay One Step Ahead Of Attackers."

];

function changeQuote(){

let q=quotes[Math.floor(Math.random()*quotes.length)];

document.getElementById("quote").innerHTML=q;

}

changeQuote();

setInterval(changeQuote,5000);

</script>

""",height=90)
# ==========================================================
# QUICK ACTIONS
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    "<h2 class='section-title'>🚀 Quick Access</h2>",
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.markdown("""

    <div class="card hover-lift">

    <div class="icon-box">🌐</div>

    <h3>URL Scanner</h3>

    <p>

    Scan suspicious URLs using

    Machine Learning + Rule Engine.

    </p>

    </div>

    """, unsafe_allow_html=True)

    if st.button("Open URL Scanner", key="url"):

        st.switch_page("pages/2_URL_Scanner.py")


with c2:

    st.markdown("""

    <div class="card hover-lift">

    <div class="icon-box">📧</div>

    <h3>Email Scanner</h3>

    <p>

    Detect phishing emails using

    NLP + Explainable AI.

    </p>

    </div>

    """, unsafe_allow_html=True)

    if st.button("Open Email Scanner", key="email"):

        st.switch_page("pages/3_📧_Email_Scanner.py")


with c3:

    st.markdown("""

    <div class="card hover-lift">

    <div class="icon-box">📊</div>

    <h3>Dashboard</h3>

    <p>

    View analytics, reports,

    trends and scan statistics.

    </p>

    </div>

    """, unsafe_allow_html=True)

    if st.button("Open Dashboard", key="dashboard"):

        st.switch_page("pages/1_🏠_Dashboard.py")


with c4:

    st.markdown("""

    <div class="card hover-lift">

    <div class="icon-box">📜</div>

    <h3>History</h3>

    <p>

    View previous scans

    and export reports.

    </p>

    </div>

    """, unsafe_allow_html=True)

    if st.button("Open History", key="history"):

        st.switch_page("pages/4_📜_History.py")


# ==========================================================
# PROJECT FEATURES
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(

"<h2 class='section-title'>✨ Project Features</h2>",

unsafe_allow_html=True

)

f1, f2, f3 = st.columns(3)

with f1:

    st.markdown("""

    <div class="feature-card">

    <h2>🧠</h2>

    <h4>Machine Learning</h4>

    <p>

    Uses ensemble models including

    Random Forest,

    XGBoost,

    LightGBM

    and Stacking.

    </p>

    </div>

    """, unsafe_allow_html=True)


with f2:

    st.markdown("""

    <div class="feature-card">

    <h2>⚙️</h2>

    <h4>Adaptive Rule Engine</h4>

    <p>

    Detects suspicious keywords,

    malicious domains,

    URL shorteners,

    brand impersonation

    and phishing patterns.

    </p>

    </div>

    """, unsafe_allow_html=True)


with f3:

    st.markdown("""

    <div class="feature-card">

    <h2>🛡️</h2>

    <h4>Explainable AI</h4>

    <p>

    Shows why a website

    or email is considered

    Safe,

    Suspicious,

    or Phishing.

    </p>

    </div>

    """, unsafe_allow_html=True)
# ==========================================================
# SYSTEM WORKFLOW
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    "<h2 class='section-title'>⚙️ System Workflow</h2>",
    unsafe_allow_html=True
)

st.markdown("""

<div class="workflow">

<div class="workflow-step">

<h3>🌐 URL / 📧 Email</h3>

<p>User Input</p>

</div>

<div class="workflow-step">

<h3>⚙️ Feature Extraction</h3>

<p>Extract Runtime Features</p>

</div>

<div class="workflow-step">

<h3>🧠 Machine Learning</h3>

<p>Stacking Ensemble Prediction</p>

</div>

<div class="workflow-step">

<h3>🛡 Rule Engine</h3>

<p>Adaptive Security Rules</p>

</div>

<div class="workflow-step">

<h3>💡 Explainable AI</h3>

<p>Reasons & Confidence Score</p>

</div>

<div class="workflow-step">

<h3>✅ Final Result</h3>

<p>Safe / Suspicious / Phishing</p>

</div>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# TECHNOLOGY STACK
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    "<h2 class='section-title'>🛠 Technology Stack</h2>",
    unsafe_allow_html=True
)

t1, t2, t3, t4 = st.columns(4)

with t1:
    st.markdown("""
    <div class="card hover-lift" align="center">
    <h1>🐍</h1>
    <h3>Python</h3>
    </div>
    """, unsafe_allow_html=True)

with t2:
    st.markdown("""
    <div class="card hover-lift" align="center">
    <h1>🧠</h1>
    <h3>Scikit-Learn</h3>
    </div>
    """, unsafe_allow_html=True)

with t3:
    st.markdown("""
    <div class="card hover-lift" align="center">
    <h1>⚡</h1>
    <h3>XGBoost</h3>
    </div>
    """, unsafe_allow_html=True)

with t4:
    st.markdown("""
    <div class="card hover-lift" align="center">
    <h1>🌐</h1>
    <h3>Streamlit</h3>
    </div>
    """, unsafe_allow_html=True)

# ==========================================================
# WHY THIS PROJECT
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    "<h2 class='section-title'>🎯 Why This Project?</h2>",
    unsafe_allow_html=True
)

st.markdown("""

<div class="card">

<h3>Adaptive Explainable Phishing Detection</h3>

<p>

Traditional phishing detection systems often provide only a binary
prediction without explaining the reason behind the decision.

This project combines Machine Learning, Adaptive Rule Engine and
Explainable AI to detect phishing attacks with greater transparency,
improved reliability and real-time analysis.

The system analyzes URLs and Email messages, extracts intelligent
features, evaluates security rules and finally generates an
interpretable prediction along with risk level and detection reasons.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# PROJECT HIGHLIGHTS
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    "<h2 class='section-title'>🚀 Project Highlights</h2>",
    unsafe_allow_html=True
)

h1, h2, h3, h4 = st.columns(4)

with h1:
    st.metric("🤖 ML Models", "5+")

with h2:
    st.metric("🔍 Detection", "Real-Time")

with h3:
    st.metric("🛡 Explainable AI", "Enabled")

with h4:
    st.metric("⚡ Decision Engine", "Adaptive")

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""

<div class="footer">

<h3>🛡 Adaptive Explainable Phishing Detection System</h3>

<p>

An AI-powered cybersecurity platform for real-time phishing detection
using Machine Learning, Adaptive Rule Engine and Explainable AI.

</p>

<br>

<b>Developed by</b>

<br>

<h3>Animesh Kushwaha & Madeeha Laiq</h3>

<br>

© 2026 All Rights Reserved

</div>

""", unsafe_allow_html=True)