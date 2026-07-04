import os
import streamlit as st
import streamlit.components.v1 as components

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(

    page_title="About Project",

    page_icon="ℹ️",

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
# HERO
# ==========================================================

st.markdown("""

<div class="hero">

<h1>

🛡 Adaptive Explainable Phishing Detection System

</h1>

<p>

Artificial Intelligence Based Cyber Security Framework

for Real-Time URL & Email Phishing Detection

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# LIVE CLOCK
# ==========================================================

c1, c2 = st.columns([2,6])

with c1:

    components.html("""

    <div id="clock"

    style="

    background:#102036;

    color:#00E676;

    padding:12px;

    border-radius:15px;

    text-align:center;

    font-size:22px;

    font-weight:bold;

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

    """, height=70)

# ==========================================================
# CYBER QUOTES
# ==========================================================

components.html("""

<div id="quote"

style="

background:#102036;

padding:18px;

border-left:5px solid #00C8FF;

border-radius:15px;

font-size:18px;

font-weight:500;

color:white;

">

Loading...

</div>

<script>

const quotes=[

"🛡 Cyber Security Starts With Awareness.",

"⚠ Every Click Can Be A Risk.",

"🔒 Think Before You Trust.",

"🌐 AI Makes Cyber Defense Smarter.",

"🚨 Detect Early. Stay Secure.",

"💻 Prevention Is Better Than Recovery."

];

function changeQuote(){

let q=quotes[Math.floor(Math.random()*quotes.length)];

document.getElementById("quote").innerHTML=q;

}

changeQuote();

setInterval(changeQuote,5000);

</script>

""", height=90)

# ==========================================================
# PROJECT OVERVIEW
# ==========================================================

st.markdown(

"<h2 class='section-title'>📖 Project Overview</h2>",

unsafe_allow_html=True

)

st.markdown("""

<div class="card">

<h3>Adaptive Explainable Phishing Detection System</h3>

<p>

The Adaptive Explainable Phishing Detection System is an
AI-powered cybersecurity application developed to detect
phishing attacks in URLs and Email/SMS messages.

Unlike traditional phishing detection systems that only
classify content as safe or malicious, this framework
combines Machine Learning, Adaptive Rule Engine and
Explainable Artificial Intelligence (XAI) to provide
accurate predictions along with the reasons behind every
decision.

The system performs real-time feature extraction,
intelligent phishing analysis and generates a transparent
security report that helps users understand why a URL or
message has been classified as Safe, Suspicious or
Phishing.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# PROJECT OBJECTIVE
# ==========================================================

st.markdown(

"<h2 class='section-title'>🎯 Project Objectives</h2>",

unsafe_allow_html=True

)

o1, o2, o3 = st.columns(3)

with o1:

    st.markdown("""

<div class="feature-card">

<h2>🛡</h2>

<h4>Detect Phishing</h4>

<p>

Identify malicious URLs and
Email messages in real time.

</p>

</div>

""", unsafe_allow_html=True)

with o2:

    st.markdown("""

<div class="feature-card">

<h2>🤖</h2>

<h4>Explain AI Decisions</h4>

<p>

Provide clear explanations
for every prediction.

</p>

</div>

""", unsafe_allow_html=True)

with o3:

    st.markdown("""

<div class="feature-card">

<h2>⚡</h2>

<h4>Improve Security</h4>

<p>

Help users make safer
online decisions.

</p>

</div>

""", unsafe_allow_html=True)
    
    # ==========================================================
# SYSTEM WORKFLOW
# ==========================================================

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

<p>Runtime Feature Generation</p>

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

<h3>🤖 Explainable AI</h3>

<p>Reason Generation</p>

</div>

<div class="workflow-step">

<h3>✅ Final Decision</h3>

<p>Safe / Suspicious / Phishing</p>

</div>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# MACHINE LEARNING MODELS
# ==========================================================

st.markdown(
    "<h2 class='section-title'>🧠 Machine Learning Models</h2>",
    unsafe_allow_html=True
)

m1, m2, m3, m4 = st.columns(4)

with m1:

    st.markdown("""

<div class="feature-card">

<h2>🌲</h2>

<h4>Random Forest</h4>

<p>

Decision-tree ensemble used as a
base learner.

</p>

</div>

""", unsafe_allow_html=True)

with m2:

    st.markdown("""

<div class="feature-card">

<h2>⚡</h2>

<h4>XGBoost</h4>

<p>

Gradient boosting model
for high accuracy.

</p>

</div>

""", unsafe_allow_html=True)

with m3:

    st.markdown("""

<div class="feature-card">

<h2>💡</h2>

<h4>LightGBM</h4>

<p>

Fast boosting model
for efficient learning.

</p>

</div>

""", unsafe_allow_html=True)

with m4:

    st.markdown("""

<div class="feature-card">

<h2>🏆</h2>

<h4>Stacking Ensemble</h4>

<p>

Final prediction generated
using multiple models.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# RULE ENGINE
# ==========================================================

st.markdown(
    "<h2 class='section-title'>🛡 Adaptive Rule Engine</h2>",
    unsafe_allow_html=True
)

st.markdown("""

<div class="card">

<h3>Hybrid Rule-Based Detection</h3>

<p>

The Rule Engine strengthens the Machine Learning model by
checking real-world phishing indicators such as:

<ul>

<li>Suspicious keywords</li>

<li>Brand impersonation</li>

<li>Shortened URLs</li>

<li>Suspicious Top-Level Domains</li>

<li>HTTPS availability</li>

<li>DNS validation</li>

<li>Obfuscation patterns</li>

<li>Special characters</li>

<li>Email phishing keywords</li>

</ul>

This hybrid approach significantly improves phishing
detection reliability.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# EXPLAINABLE AI
# ==========================================================

st.markdown(
    "<h2 class='section-title'>🤖 Explainable AI</h2>",
    unsafe_allow_html=True
)

st.markdown("""

<div class="card">

<h3>Transparent Decision Making</h3>

<p>

Unlike traditional AI systems,
our Explainable AI module provides
the reasons behind every prediction.

Instead of simply saying

<b>SAFE</b>

or

<b>PHISHING</b>

the system explains

<ul>

<li>Why the URL was suspicious</li>

<li>Which phishing keywords were found</li>

<li>Which security rules were triggered</li>

<li>Machine Learning confidence score</li>

<li>Final risk level</li>

</ul>

This increases user trust and helps in cyber awareness.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# TECHNOLOGY STACK
# ==========================================================

st.markdown(
    "<h2 class='section-title'>🛠 Technology Stack</h2>",
    unsafe_allow_html=True
)

t1, t2, t3, t4 = st.columns(4)

tech = [

("🐍", "Python"),

("🌐", "Streamlit"),

("📊", "Pandas"),

("🤖", "Scikit-Learn")

]

for col, item in zip([t1, t2, t3, t4], tech):

    with col:

        st.markdown(f"""

<div class="card" align="center">

<h1>{item[0]}</h1>

<h3>{item[1]}</h3>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# KEY FEATURES
# ==========================================================

st.markdown(
    "<h2 class='section-title'>⭐ Key Features</h2>",
    unsafe_allow_html=True
)

features = [

"🌐 Real-Time URL Detection",

"📧 Email Phishing Detection",

"🤖 Explainable AI",

"🛡 Adaptive Rule Engine",

"🧠 Stacking Ensemble Learning",

"📊 Interactive Dashboard",

"📜 Scan History",

"📥 Report Download",

"⚡ Real-Time Feature Extraction",

"🎯 High Detection Accuracy"

]

c1, c2 = st.columns(2)

half = len(features)//2

with c1:

    for f in features[:half]:

        st.success(f)

with c2:

    for f in features[half:]:

        st.success(f)

        # ==========================================================
# PERFORMANCE HIGHLIGHTS
# ==========================================================

st.markdown(
    "<h2 class='section-title'>📈 Performance Highlights</h2>",
    unsafe_allow_html=True
)

p1, p2, p3, p4 = st.columns(4)

with p1:
    st.metric("🎯 Accuracy", "97%+")

with p2:
    st.metric("⚡ Response Time", "< 2 sec")

with p3:
    st.metric("🛡 Explainability", "Enabled")

with p4:
    st.metric("🌐 Detection", "Real-Time")

# ==========================================================
# FUTURE SCOPE
# ==========================================================

st.markdown(
    "<h2 class='section-title'>🚀 Future Scope</h2>",
    unsafe_allow_html=True
)

st.markdown("""

<div class="card">

<h3>Future Enhancements</h3>

<p>

The current system provides reliable phishing detection using
Machine Learning and Explainable AI.

Future versions may include:

<ul>

<li>VirusTotal API Integration</li>

<li>WHOIS Domain Lookup</li>

<li>Domain Age Detection</li>

<li>IP Geolocation</li>

<li>QR Code Phishing Detection</li>

<li>Browser Extension</li>

<li>Android Application</li>

<li>Cloud Deployment</li>

<li>Threat Intelligence Integration</li>

<li>Deep Learning based Email Detection</li>

</ul>

These enhancements will improve both usability and
detection capability.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# DEVELOPERS
# ==========================================================

st.markdown(
    "<h2 class='section-title'>👨‍💻 Development Team</h2>",
    unsafe_allow_html=True
)

d1, d2 = st.columns(2)

with d1:

    st.markdown("""

<div class="card" align="center">

<h1>👨‍💻</h1>

<h2>Animesh Kushwaha</h2>

<h4>AI Developer</h4>

<p>

Machine Learning

Cyber Security

Python Development

Explainable AI

</p>

</div>

""", unsafe_allow_html=True)

with d2:

    st.markdown("""

<div class="card" align="center">

<h1>👩‍💻</h1>

<h2>Madeeha Laiq</h2>

<h4>Research Scholar</h4>

<p>

Department of Artificial Intelligence
& Machine Learning

Research

Machine Learning

Cyber Security

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# DEPARTMENT
# ==========================================================

st.markdown(
    "<h2 class='section-title'>🏫 Department</h2>",
    unsafe_allow_html=True
)

st.markdown("""

<div class="card">

<h3>

Department of Artificial Intelligence & Machine Learning

</h3>

<h4>

Sam Higginbottom University of Agriculture,
Technology and Sciences (SHUATS)

</h4>

<p>

Prayagraj

Uttar Pradesh

India

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# ACKNOWLEDGEMENT
# ==========================================================

st.markdown(
    "<h2 class='section-title'>🙏 Acknowledgement</h2>",
    unsafe_allow_html=True
)

st.markdown("""

<div class="card">

<p>

We sincerely acknowledge the continuous support and
guidance received throughout the development of this
project.

This work combines Artificial Intelligence,
Machine Learning,
Explainable AI and Cyber Security concepts
to improve awareness against phishing attacks.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# REFERENCES
# ==========================================================

st.markdown(
    "<h2 class='section-title'>📚 References</h2>",
    unsafe_allow_html=True
)

st.markdown("""

<div class="card">

<ul>

<li>Scikit-Learn Documentation</li>

<li>Streamlit Documentation</li>

<li>XGBoost Documentation</li>

<li>LightGBM Documentation</li>

<li>Pandas Documentation</li>

<li>OWASP Phishing Guidelines</li>

<li>NIST Cyber Security Framework</li>

<li>Google Safe Browsing Concepts</li>

</ul>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# COPYRIGHT
# ==========================================================

st.markdown(
    "<h2 class='section-title'>📜 Copyright</h2>",
    unsafe_allow_html=True
)

st.info("""

Adaptive Explainable Phishing Detection System

Version 1.0

© 2026

Developed for Academic and Research Purpose.

""")

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""

<div class="footer">

<h2>

🛡 Adaptive Explainable Phishing Detection System

</h2>

<br>

Developed by

<br>

<b>
Animesh Kushwaha & Madeeha Laiq
</b>

<br>
© 2026 All Rights Reserved

</div>

""", unsafe_allow_html=True)
