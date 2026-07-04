import os
import sqlite3
import random
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

import plotly.express as px
import plotly.graph_objects as go

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(

    page_title="Cyber Security Dashboard",

    page_icon="📊",

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
# DATABASE
# ==========================================================

DB_NAME = "phishing_history.db"

def load_history():

    try:

        conn = sqlite3.connect(DB_NAME)

        df = pd.read_sql(

            "SELECT * FROM history",

            conn

        )

        conn.close()

        return df

    except:

        return pd.DataFrame()

df = load_history()

# ==========================================================
# HEADER
# ==========================================================

st.markdown("""

<div class="hero">

<h1>📊 Cyber Security Dashboard</h1>

<p>

Real-Time Analytics & Threat Intelligence

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

border-radius:15px;

border-left:5px solid #00C8FF;

font-size:18px;

color:white;

font-weight:500;

">

Loading...

</div>

<script>

const quotes=[

"🛡 Monitor Every Threat.",

"⚠ Every Click Matters.",

"🔒 Stay Alert. Stay Secure.",

"🌐 Cyber Awareness Saves Data.",

"🚨 Detect Before It's Too Late.",

"🧠 AI Makes Security Smarter.",

"📧 Never Trust Unknown Emails.",

"🌍 Protect Your Digital Identity."

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
# SUMMARY
# ==========================================================

total = len(df)

safe = len(df[df["prediction"]=="SAFE"]) if total else 0

sus = len(df[df["prediction"]=="SUSPICIOUS"]) if total else 0

phish = len(df[df["prediction"]=="PHISHING"]) if total else 0

url_count = len(df[df["scan_type"]=="URL"]) if total else 0

email_count = len(df[df["scan_type"]=="EMAIL"]) if total else 0

# ==========================================================
# METRIC CARDS
# ==========================================================

st.markdown(

"<h2 class='section-title'>📈 Dashboard Overview</h2>",

unsafe_allow_html=True

)

m1,m2,m3,m4,m5 = st.columns(5)

with m1:

    st.metric(

        "📄 Total Scans",

        total

    )

with m2:

    st.metric(

        "🟢 Safe",

        safe

    )

with m3:

    st.metric(

        "🟠 Suspicious",

        sus

    )

with m4:

    st.metric(

        "🔴 Phishing",

        phish

    )

with m5:

    accuracy = 0

    if total:

        accuracy = round(

            (safe/total)*100,

            1

        )

    st.metric(

        "🎯 Safe Ratio",

        f"{accuracy}%"

    )

# ==========================================================
# SCAN TYPE SUMMARY
# ==========================================================

st.markdown(

"<h2 class='section-title'>📂 Scan Categories</h2>",

unsafe_allow_html=True

)

a,b = st.columns(2)

with a:

    st.metric(

        "🌐 URL Scans",

        url_count

    )

with b:

    st.metric(

        "📧 Email Scans",

        email_count

    )

    # ==========================================================
# CHARTS
# ==========================================================

st.markdown(
    "<h2 class='section-title'>📊 Threat Analytics</h2>",
    unsafe_allow_html=True
)

left, right = st.columns(2)

# ==========================================================
# PIE CHART
# ==========================================================

with left:

    if total > 0:

        pie_df = pd.DataFrame({

            "Category":[

                "SAFE",

                "SUSPICIOUS",

                "PHISHING"

            ],

            "Count":[

                safe,

                sus,

                phish

            ]

        })

        fig = px.pie(

            pie_df,

            values="Count",

            names="Category",

            hole=0.60,

            title="Overall Scan Distribution",

            color="Category",

            color_discrete_map={

                "SAFE":"#00E676",

                "SUSPICIOUS":"orange",

                "PHISHING":"red"

            }

        )

        fig.update_layout(

            paper_bgcolor="rgba(0,0,0,0)",

            plot_bgcolor="rgba(0,0,0,0)",

            font_color="white",

            height=450

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    else:

        st.info("No scan history available.")

# ==========================================================
# BAR CHART
# ==========================================================

with right:

    if total > 0:

        bar_df = pd.DataFrame({

            "Prediction":[

                "SAFE",

                "SUSPICIOUS",

                "PHISHING"

            ],

            "Count":[

                safe,

                sus,

                phish

            ]

        })

        fig = px.bar(

            bar_df,

            x="Prediction",

            y="Count",

            text="Count",

            color="Prediction",

            color_discrete_map={

                "SAFE":"#00E676",

                "SUSPICIOUS":"orange",

                "PHISHING":"red"

            }

        )

        fig.update_layout(

            paper_bgcolor="rgba(0,0,0,0)",

            plot_bgcolor="rgba(0,0,0,0)",

            font_color="white",

            height=450,

            showlegend=False

        )

        fig.update_traces(

            textposition="outside"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    else:

        st.info("No data available.")

# ==========================================================
# URL vs EMAIL
# ==========================================================

st.markdown(
    "<h2 class='section-title'>🌐 URL vs Email Analysis</h2>",
    unsafe_allow_html=True
)

if total > 0:

    compare = pd.DataFrame({

        "Scan Type":[

            "URL",

            "EMAIL"

        ],

        "Count":[

            url_count,

            email_count

        ]

    })

    fig = px.bar(

        compare,

        x="Scan Type",

        y="Count",

        text="Count",

        color="Scan Type",

        color_discrete_sequence=[

            "#00C8FF",

            "#00E676"

        ]

    )

    fig.update_layout(

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font_color="white",

        height=400,

        showlegend=False

    )

    fig.update_traces(

        textposition="outside"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

else:

    st.info("No scan history available.")

# ==========================================================
# RISK DISTRIBUTION
# ==========================================================

st.markdown(

"<h2 class='section-title'>⚠ Risk Distribution</h2>",

unsafe_allow_html=True

)

if total > 0:

    risk = df.groupby(

        "risk"

    ).size().reset_index(name="Count")

    fig = px.bar(

        risk,

        x="risk",

        y="Count",

        color="risk",

        text="Count",

        color_discrete_map={

            "LOW":"green",

            "MEDIUM":"orange",

            "HIGH":"red"

        }

    )

    fig.update_layout(

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font_color="white",

        height=400,

        showlegend=False

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

else:

    st.info("No risk data available.")

# ==========================================================
# DAILY TREND
# ==========================================================

st.markdown(

"<h2 class='section-title'>📈 Daily Scan Trend</h2>",

unsafe_allow_html=True

)

if total > 0:

    df["scan_time"] = pd.to_datetime(

        df["scan_time"]

    )

    trend = df.groupby(

        df["scan_time"].dt.date

    ).size().reset_index(name="Scans")

    fig = px.line(

        trend,

        x="scan_time",

        y="Scans",

        markers=True

    )

    fig.update_layout(

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font_color="white",

        height=450

    )

    fig.update_traces(

        line_color="#00C8FF",

        marker_color="#00E676",

        marker_size=8

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

else:

    st.info("Trend data unavailable.")

    # ==========================================================
# RECENT ACTIVITY
# ==========================================================

st.markdown(
    "<h2 class='section-title'>📜 Recent Scan Activity</h2>",
    unsafe_allow_html=True
)

if total > 0:

    recent = df.sort_values(
        "scan_time",
        ascending=False
    ).head(10)

    show = recent[[
        "scan_time",
        "scan_type",
        "prediction",
        "risk",
        "score"
    ]]

    st.dataframe(

        show,

        use_container_width=True,

        hide_index=True

    )

else:

    st.info("No scan history available.")

# ==========================================================
# THREAT INSIGHTS
# ==========================================================

st.markdown(
    "<h2 class='section-title'>🧠 Threat Insights</h2>",
    unsafe_allow_html=True
)

c1, c2 = st.columns(2)

with c1:

    st.markdown("""

    <div class="card">

    <h3>🛡 Security Summary</h3>

    <ul>

    <li>Total Scans Performed : <b>{}</b></li>

    <li>Safe URLs / Emails : <b>{}</b></li>

    <li>Suspicious Cases : <b>{}</b></li>

    <li>Confirmed Phishing : <b>{}</b></li>

    </ul>

    </div>

    """.format(
        total,
        safe,
        sus,
        phish
    ),
    unsafe_allow_html=True
    )

with c2:

    if total > 0:

        phishing_percent = round((phish / total) * 100, 2)

        safe_percent = round((safe / total) * 100, 2)

    else:

        phishing_percent = 0

        safe_percent = 0

    st.markdown(f"""

    <div class="card">

    <h3>📊 Overall Detection</h3>

    <ul>

    <li>Safe Rate : <b>{safe_percent}%</b></li>

    <li>Threat Rate : <b>{phishing_percent}%</b></li>

    <li>Adaptive Rule Engine : <b>Enabled</b></li>

    <li>Explainable AI : <b>Enabled</b></li>

    </ul>

    </div>

    """, unsafe_allow_html=True)

# ==========================================================
# CYBER SECURITY TIPS
# ==========================================================

st.markdown(
    "<h2 class='section-title'>💡 Cyber Security Tips</h2>",
    unsafe_allow_html=True
)

tips = [

    "Never click unknown links received through Email or SMS.",

    "Always verify the website URL before entering credentials.",

    "Avoid downloading files from unknown senders.",

    "Enable Multi-Factor Authentication (MFA).",

    "Use strong and unique passwords.",

    "Keep your browser and operating system updated.",

    "Avoid logging in through shortened URLs unless verified.",

    "Check HTTPS and domain spelling carefully."

]

tip = random.choice(tips)

st.success(tip)

# ==========================================================
# PROJECT INFORMATION
# ==========================================================

st.markdown(
    "<h2 class='section-title'>ℹ About Dashboard</h2>",
    unsafe_allow_html=True
)

st.markdown("""

<div class="card">

<h3>Adaptive Explainable Phishing Detection Dashboard</h3>

<p>

This dashboard provides a centralized view of phishing detection
activities performed by the system.

It summarizes URL scans, Email scans,
prediction statistics, phishing trends,
risk distribution and recent activities.

The system combines

<b>Machine Learning</b>,

<b>Adaptive Rule Engine</b>

and

<b>Explainable Artificial Intelligence (XAI)</b>

to improve phishing detection accuracy
while providing transparent explanations
for every prediction.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# PROJECT DEVELOPERS
# ==========================================================

st.markdown(
    "<h2 class='section-title'>👨‍💻 Developers</h2>",
    unsafe_allow_html=True
)

d1, d2 = st.columns(2)

with d1:

    st.markdown("""

    <div class="card" align="center">

    <h2>👨‍💻</h2>

    <h3>Animesh Kushwaha</h3>

    <p>

    AI Developer

    <br>

    Machine Learning Engineer

    </p>

    </div>

    """, unsafe_allow_html=True)

with d2:

    st.markdown("""

    <div class="card" align="center">

    <h2>👩‍💻</h2>

    <h3>Madeeha Laiq</h3>

    <p>

    Research Scholar

    <br>

    Department of Artificial Intelligence & Machine Learning

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

🛡 Adaptive Explainable Phishing Detection System

</h2>

<br>

Developed by
<b>

Animesh Kushwaha & Madeeha Laiq

</b>

<br>

© 2026 All Rights Reserved

</div>

""", unsafe_allow_html=True)
