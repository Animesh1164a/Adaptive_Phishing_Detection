import os
import json
import streamlit as st
import streamlit.components.v1 as components

from src.text_detection.predict_text import predict_text
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

    page_title="Email Phishing Scanner",

    page_icon="📧",

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
# HEADER
# ==========================================================

st.markdown("""

<div class="hero">

<h1>

📧 Intelligent Email Scanner

</h1>

<p>

Analyze suspicious Email messages using

Machine Learning +

Adaptive Rule Engine +

Explainable AI

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

        const now = new Date();

        document.getElementById("clock").innerHTML =

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

"📧 Never trust unexpected emails.",

"🛡 Verify sender identity before clicking links.",

"⚠ Urgent emails are often phishing attempts.",

"🔒 Never share OTP or passwords through email.",

"🚨 Think Before You Click."

];

function changeQuote(){

let q = quotes[Math.floor(Math.random()*quotes.length)];

document.getElementById("quote").innerHTML = q;

}

changeQuote();

setInterval(changeQuote,5000);

</script>

""", height=90)

# ==========================================================
# EMAIL INPUT
# ==========================================================

st.markdown(

"<h2 class='section-title'>📨 Scan Email Message</h2>",

unsafe_allow_html=True

)

st.markdown("""

<div class="card">

Paste the complete Email or SMS message below.

The system will analyze it using

<ul>

<li>Machine Learning</li>

<li>Adaptive Rule Engine</li>

<li>Explainable AI</li>

</ul>

</div>

""", unsafe_allow_html=True)

message = st.text_area(

"Email / SMS",

height=260,

placeholder="""

Congratulations!

You have won $5000.

Click here:

http://bit.ly/abc123

Verify your account immediately.

"""

)

scan = st.button(

"🚀 Scan Email",

use_container_width=True

)

# ==========================================================
# SCAN EMAIL
# ==========================================================

if scan:

    if message.strip() == "":

        st.warning("Please enter an Email or SMS message.")

    else:

        with st.spinner("📧 Analyzing Message..."):

            result = predict_text(message)

        # --------------------------------------------------
        # DATABASE
        # --------------------------------------------------

        insert_record(

            "EMAIL",

            message[:250],

            result["prediction"],

            result["risk"],

            result["score"]

        )

        prediction = result["prediction"]

        risk = result["risk"]

        score = result["score"]

        ml_score = result["ml_score"]

        rule_score = result["rule_score"]

        probability = result["probability"]

        reasons = result["reasons"]

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

        st.markdown("<br>", unsafe_allow_html=True)

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            st.metric(

                "🎯 Final Score",

                f"{score:.2f}%"

            )

        with c2:

            st.metric(

                "🧠 ML Score",

                f"{ml_score:.2f}%"

            )

        with c3:

            st.metric(

                "⚙ Rule Score",

                rule_score

            )

        with c4:

            st.metric(

                "📈 Probability",

                f"{probability*100:.2f}%"

            )

# ==========================================================
# RISK METER
# ==========================================================

        st.markdown(

            "<h2 class='section-title'>📊 Risk Meter</h2>",

            unsafe_allow_html=True

        )

        st.progress(

            min(max(score / 100, 0), 1)

        )

        st.write(

            f"Overall Threat Score : **{score:.2f}%**"

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

The message appears to be legitimate.

No major phishing indicators were detected by the
Machine Learning model or Rule Engine.

""")

        elif prediction == "SUSPICIOUS":

            st.warning("""

The message contains suspicious patterns.

Please verify the sender, avoid clicking unknown links,
and do not share sensitive information.

""")

        else:

            st.error("""

The message is highly likely to be a phishing attempt.

Avoid clicking any links.

Do not reply.

Never share passwords, OTPs or banking information.

Delete or report this message immediately.

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
                "✅ No suspicious keywords or phishing patterns detected."
            )

        else:

            for r in reasons:

                st.markdown(f"""
                <div class="reason-box">
                🔹 {r}
                </div>
                """, unsafe_allow_html=True)

# ==========================================================
# MESSAGE SUMMARY
# ==========================================================

        st.markdown(
            "<h2 class='section-title'>📨 Message Summary</h2>",
            unsafe_allow_html=True
        )

        total_words = len(message.split())

        total_chars = len(message)

        urls = message.lower().count("http")

        money = message.count("$") + message.count("₹")

        s1, s2, s3, s4 = st.columns(4)

        with s1:
            st.metric("Words", total_words)

        with s2:
            st.metric("Characters", total_chars)

        with s3:
            st.metric("URLs Found", urls)

        with s4:
            st.metric("Currency Symbols", money)

# ==========================================================
# SECURITY RECOMMENDATIONS
# ==========================================================

        st.markdown(
            "<h2 class='section-title'>🛡 Security Recommendations</h2>",
            unsafe_allow_html=True
        )

        if prediction == "SAFE":

            st.success("""

✔ Message appears legitimate.

✔ Still verify unknown senders.

✔ Never share OTP or passwords.

✔ Avoid downloading unknown attachments.

""")

        elif prediction == "SUSPICIOUS":

            st.warning("""

⚠ Verify the sender identity.

⚠ Do not click shortened URLs.

⚠ Confirm payment requests independently.

⚠ Scan attachments before opening.

""")

        else:

            st.error("""

🚨 Delete the message immediately.

🚨 Never click any links.

🚨 Never share OTP, Password or Bank Details.

🚨 Block and report the sender.

🚨 Inform your IT/Security Team if received at work.

""")

# ==========================================================
# DETECTION ENGINE
# ==========================================================

        st.markdown(
            "<h2 class='section-title'>🤖 Detection Engine</h2>",
            unsafe_allow_html=True
        )

        st.info("""

Machine Learning :
Adaptive NLP Classifier

Rule Engine :
Keyword + Pattern Detection

Decision Engine :
Hybrid Explainable AI

Real-Time Analysis :
Enabled

Confidence Analysis :
Enabled

""")

# ==========================================================
# DOWNLOAD REPORT
# ==========================================================

        st.markdown(
            "<h2 class='section-title'>📥 Download Report</h2>",
            unsafe_allow_html=True
        )

        report = {

            "Message": message,

            "Prediction": prediction,

            "Risk": risk,

            "Final Score": score,

            "ML Score": ml_score,

            "Rule Score": rule_score,

            "Probability": probability,

            "Reasons": reasons

        }

        st.download_button(

            label="⬇ Download JSON Report",

            data=json.dumps(

                report,

                indent=4,

                default=str

            ),

            file_name="email_scan_report.json",

            mime="application/json"

        )

# ==========================================================
# ABOUT THIS SCAN
# ==========================================================

        st.markdown(
            "<h2 class='section-title'>ℹ About This Analysis</h2>",
            unsafe_allow_html=True
        )

        st.markdown("""

<div class="card">

<h3>Email Phishing Detection</h3>

<p>

This message has been analyzed using an adaptive phishing
detection framework that combines:

<ul>

<li>Machine Learning Classification</li>

<li>Adaptive Rule Engine</li>

<li>Explainable AI Decision Engine</li>

</ul>

The final prediction is generated by combining the ML
confidence score with expert-defined phishing rules,
making the detection more reliable and transparent.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""

<div class="footer">

<h2>

📧 Adaptive Explainable Phishing Detection System

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
