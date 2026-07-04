import os
import json
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

from src.url_detection.predict_url import predict_url
from src.database.database import (
    create_database,
    insert_record
)

# ==========================================================
# INITIALIZE DATABASE
# ==========================================================

create_database()

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="URL Phishing Scanner",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# LOAD CSS
# ==========================================================

if os.path.exists("assets/style.css"):
    with open("assets/style.css", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# ==========================================================
# HERO SECTION
# ==========================================================

st.markdown("""

<div class="hero">

<h1>🌐 Intelligent URL Scanner</h1>

<p>

Analyze suspicious URLs using

Machine Learning • Adaptive Rule Engine • Explainable AI

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# LIVE CLOCK
# ==========================================================

clock_col, _ = st.columns([2, 6])

with clock_col:

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

"🌐 Always verify URLs before clicking.",

"🛡 HTTPS alone is not enough.",

"⚠ Shortened URLs may hide phishing websites.",

"🔒 Never enter credentials without checking the domain.",

"🚨 Think Before You Click."

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
# URL INPUT
# ==========================================================

st.markdown(

"<h2 class='section-title'>🔍 URL Scanner</h2>",

unsafe_allow_html=True

)

st.markdown("""

<div class="card">

Paste any website URL below.

The system performs:

<ul>

<li>Machine Learning Detection</li>

<li>Adaptive Rule Analysis</li>

<li>Explainable AI Decision</li>

<li>Real-Time Feature Extraction</li>

</ul>

</div>

""", unsafe_allow_html=True)

url = st.text_input(

"Website URL",

placeholder="https://example.com"

)

scan = st.button(

"🚀 Scan URL",

use_container_width=True

)

# ==========================================================
# SCAN
# ==========================================================

if scan:

    if not url.strip():

        st.warning("Please enter a valid URL.")

        st.stop()

    with st.spinner("🔍 Scanning URL..."):

        result = predict_url(url)

    # ----------------------------
    # DATABASE
    # ----------------------------

    insert_record(

        "URL",

        url,

        result["prediction"],

        result["risk"],

        result["score"]

    )

    # ----------------------------
    # VARIABLES
    # ----------------------------

    prediction = result["prediction"]

    risk = result["risk"]

    score = float(result["score"])

    ml_score = float(result["ml_score"])

    rule_score = result["rule_score"]

    reasons = result["reasons"]

    url_features = result["url_features"]

    website_features = result["website_features"]
    
        # ==========================================================
    # RESULT CARD
    # ==========================================================

    st.markdown("<br>", unsafe_allow_html=True)

    if prediction == "SAFE":

        st.markdown(f"""

        <div class="result-safe result-card">

        <h1>✅ SAFE</h1>

        <h3>Risk Score : {score:.2f}%</h3>

        </div>

        """, unsafe_allow_html=True)

    elif prediction == "SUSPICIOUS":

        st.markdown(f"""

        <div class="result-warning result-card">

        <h1>⚠ SUSPICIOUS</h1>

        <h3>Risk Score : {score:.2f}%</h3>

        </div>

        """, unsafe_allow_html=True)

    else:

        st.markdown(f"""

        <div class="result-danger result-card">

        <h1>🚨 PHISHING</h1>

        <h3>Risk Score : {score:.2f}%</h3>

        </div>

        """, unsafe_allow_html=True)

    # ==========================================================
    # SCORE CARDS
    # ==========================================================

    st.markdown(
        "<h2 class='section-title'>📊 Detection Scores</h2>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(

            "🎯 Final Score",

            f"{score:.2f}%"

        )

    with col2:

        st.metric(

            "🧠 ML Score",

            f"{ml_score:.2f}%"

        )

    with col3:

        st.metric(

            "⚙ Rule Score",

            f"{rule_score}"

        )

    # ==========================================================
    # RISK METER
    # ==========================================================

    st.markdown(

        "<h2 class='section-title'>📈 Risk Meter</h2>",

        unsafe_allow_html=True

    )

    st.progress(

        min(score / 100, 1.0)

    )

    st.write(

        f"Overall Risk : **{score:.2f}%**"

    )

    # ==========================================================
    # EXPLAINABLE AI
    # ==========================================================

    st.markdown(

        "<h2 class='section-title'>🤖 Explainable AI</h2>",

        unsafe_allow_html=True

    )

    if prediction == "SAFE":

        st.success("""

The URL appears legitimate.

Both the Machine Learning model and the Adaptive Rule Engine
did not find any significant phishing indicators.

""")

    elif prediction == "SUSPICIOUS":

        st.warning("""

The URL contains suspicious characteristics.

Please verify the domain before visiting it
or entering any credentials.

""")

    else:

        st.error("""

The URL has multiple phishing indicators.

Avoid visiting this website.

Never enter passwords or banking information.

""")

    # ==========================================================
    # DETECTION REASONS
    # ==========================================================

    st.markdown(

        "<h2 class='section-title'>📌 Detection Reasons</h2>",

        unsafe_allow_html=True

    )

    if len(reasons) == 0:

        st.success(

            "✅ No suspicious indicators detected."

        )

    else:

        for reason in reasons:

            st.markdown(

                f"""

<div class="reason-box">

🔹 {reason}

</div>

""",

                unsafe_allow_html=True

            )
            
                # ==========================================================
    # URL FEATURES
    # ==========================================================

    st.markdown(
        "<h2 class='section-title'>🌐 URL Features</h2>",
        unsafe_allow_html=True
    )

    url_df = pd.DataFrame(
        list(url_features.items()),
        columns=["Feature", "Value"]
    )

    st.dataframe(
        url_df,
        use_container_width=True,
        hide_index=True
    )

    # ==========================================================
    # WEBSITE FEATURES
    # ==========================================================

    st.markdown(
        "<h2 class='section-title'>🖥 Website Features</h2>",
        unsafe_allow_html=True
    )

    website_df = pd.DataFrame(
        list(website_features.items()),
        columns=["Feature", "Value"]
    )

    st.dataframe(
        website_df,
        use_container_width=True,
        hide_index=True
    )

    # ==========================================================
    # DOMAIN INFORMATION
    # ==========================================================

    st.markdown(
        "<h2 class='section-title'>🌍 Domain Information</h2>",
        unsafe_allow_html=True
    )

    d1, d2, d3, d4 = st.columns(4)

    with d1:

        st.metric(
            "HTTPS",
            "✅ Yes" if url_features.get("IsHTTPS", 0) else "❌ No"
        )

    with d2:

        st.metric(
            "DNS",
            "Available" if url_features.get("DNS_Available", 0)
            else "Unavailable"
        )

    with d3:

        st.metric(
            "Subdomains",
            url_features.get("NoOfSubDomain", 0)
        )

    with d4:

        st.metric(
            "Domain Length",
            url_features.get("DomainLength", 0)
        )

    # ==========================================================
    # URL QUALITY
    # ==========================================================

    st.markdown(
        "<h2 class='section-title'>📈 URL Quality</h2>",
        unsafe_allow_html=True
    )

    q1, q2, q3 = st.columns(3)

    with q1:

        st.metric(
            "Similarity",
            url_features.get("URLSimilarityIndex", 0)
        )

    with q2:

        st.metric(
            "Character Probability",
            url_features.get("URLCharProb", 0)
        )

    with q3:

        st.metric(
            "TLD Trust",
            url_features.get("TLDLegitimateProb", 0)
        )

    # ==========================================================
    # SECURITY CHECKLIST
    # ==========================================================

    st.markdown(
        "<h2 class='section-title'>🛡 Security Checklist</h2>",
        unsafe_allow_html=True
    )

    checklist = [

        ("HTTPS Enabled",
         url_features.get("IsHTTPS", 0)),

        ("DNS Available",
         url_features.get("DNS_Available", 0)),

        ("No IP Address",
         not url_features.get("IsDomainIP", 0)),

        ("No Obfuscation",
         not url_features.get("HasObfuscation", 0)),

        ("No @ Symbol",
         not url_features.get("HasAtSymbol", 0)),

        ("No Hyphen Abuse",
         not url_features.get("HasHyphen", 0))

    ]

    for title, status in checklist:

        if status:

            st.success(f"✔ {title}")

        else:

            st.error(f"✖ {title}")

    # ==========================================================
    # SECURITY RECOMMENDATIONS
    # ==========================================================

    st.markdown(
        "<h2 class='section-title'>💡 Security Recommendations</h2>",
        unsafe_allow_html=True
    )

    if prediction == "SAFE":

        st.success("""

✔ URL appears safe.

✔ Verify the domain before entering credentials.

✔ Continue browsing carefully.

""")

    elif prediction == "SUSPICIOUS":

        st.warning("""

⚠ Verify the sender.

⚠ Check spelling of the domain.

⚠ Avoid entering passwords.

⚠ Open only if trusted.

""")

    else:

        st.error("""

🚨 Do NOT visit this website.

🚨 Never enter passwords.

🚨 Never provide banking details.

🚨 Report this URL.

""")
            # ==========================================================
    # DOWNLOAD REPORT
    # ==========================================================

    st.markdown(
        "<h2 class='section-title'>📥 Download Scan Report</h2>",
        unsafe_allow_html=True
    )

    report = {

        "URL": url,

        "Prediction": prediction,

        "Risk": risk,

        "Final Score": score,

        "ML Score": ml_score,

        "Rule Score": rule_score,

        "Reasons": reasons,

        "URL Features": url_features,

        "Website Features": website_features

    }

    st.download_button(

        label="📄 Download JSON Report",

        data=json.dumps(

            report,

            indent=4,

            default=str

        ),

        file_name="URL_Scan_Report.json",

        mime="application/json"

    )

    # ==========================================================
    # DETECTION ENGINE
    # ==========================================================

    st.markdown(
        "<h2 class='section-title'>🤖 Detection Engine</h2>",
        unsafe_allow_html=True
    )

    info1, info2 = st.columns(2)

    with info1:

        st.info("""

Machine Learning

✔ Adaptive Stacking Ensemble

✔ Runtime Prediction

✔ Confidence Score

✔ Feature Extraction

""")

    with info2:

        st.info("""

Adaptive Rule Engine

✔ Brand Detection

✔ URL Analysis

✔ DNS Verification

✔ Explainable AI

""")

    # ==========================================================
    # SCAN SUMMARY
    # ==========================================================

    st.markdown(
        "<h2 class='section-title'>📋 Scan Summary</h2>",
        unsafe_allow_html=True
    )

    st.markdown(f"""

<div class="card">

### 🌐 URL

`{url}`

---

### Prediction

**{prediction}**

---

### Risk Level

**{risk}**

---

### Final Score

**{score:.2f}%**

---

### Detection Method

✔ Machine Learning

✔ Adaptive Rule Engine

✔ Explainable AI

</div>

""", unsafe_allow_html=True)

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""

<div class="footer">

<h2>

🛡 Adaptive Explainable Phishing Detection System

</h2>

<hr>

<h5>
Developed By
</h5>

<h4>
Animesh Kushwaha & Madeeha Laiq
</h4>
<br>

© 2026 All Rights Reserved

</div>

""", unsafe_allow_html=True)