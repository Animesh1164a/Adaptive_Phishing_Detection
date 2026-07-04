import os
import sqlite3
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(

    page_title="Scan History",

    page_icon="📜",

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

    conn = sqlite3.connect(DB_NAME)

    df = pd.read_sql(

        "SELECT * FROM history ORDER BY id DESC",

        conn

    )

    conn.close()

    return df

df = load_history()

# ==========================================================
# HERO
# ==========================================================

st.markdown("""

<div class="hero">

<h1>

📜 Scan History

</h1>

<p>

View Previous URL & Email Scan Reports

</p>

</div>

""",unsafe_allow_html=True)

# ==========================================================
# LIVE CLOCK
# ==========================================================

c1,c2=st.columns([2,6])

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

""",height=70)

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

"🛡 Every scan improves cyber awareness.",

"📜 Logs help detect attack patterns.",

"🌐 Review suspicious activity regularly.",

"⚠ History is evidence of cyber threats.",

"🔒 Monitor your security continuously."

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
# SUMMARY
# ==========================================================

total=len(df)

safe=len(df[df["prediction"]=="SAFE"])

sus=len(df[df["prediction"]=="SUSPICIOUS"])

phish=len(df[df["prediction"]=="PHISHING"])

url=len(df[df["scan_type"]=="URL"])

email=len(df[df["scan_type"]=="EMAIL"])

st.markdown(

"<h2 class='section-title'>📊 History Overview</h2>",

unsafe_allow_html=True

)

m1,m2,m3,m4,m5=st.columns(5)

with m1:

    st.metric(

        "Total",

        total

    )

with m2:

    st.metric(

        "SAFE",

        safe

    )

with m3:

    st.metric(

        "SUSPICIOUS",

        sus

    )

with m4:

    st.metric(

        "PHISHING",

        phish

    )

with m5:

    st.metric(

        "URL / EMAIL",

        f"{url}/{email}"

    )

# ==========================================================
# SEARCH & FILTER
# ==========================================================

st.markdown(

"<h2 class='section-title'>🔍 Search History</h2>",

unsafe_allow_html=True

)

c1,c2,c3=st.columns(3)

with c1:

    search=st.text_input(

        "Search"

    )

with c2:

    prediction_filter=st.selectbox(

        "Prediction",

        [

            "ALL",

            "SAFE",

            "SUSPICIOUS",

            "PHISHING"

        ]

    )

with c3:

    type_filter=st.selectbox(

        "Scan Type",

        [

            "ALL",

            "URL",

            "EMAIL"

        ]

    )

filtered=df.copy()

if search!="":

    filtered=filtered[

        filtered["input_data"]

        .str.contains(

            search,

            case=False,

            na=False

        )

    ]

if prediction_filter!="ALL":

    filtered=filtered[

        filtered["prediction"]

        ==prediction_filter

    ]

if type_filter!="ALL":

    filtered=filtered[

        filtered["scan_type"]

        ==type_filter

    ]

    # ==========================================================
# HISTORY TABLE
# ==========================================================

st.markdown(

"<h2 class='section-title'>📋 Scan History</h2>",

unsafe_allow_html=True

)

if filtered.empty:

    st.warning("No records found.")

else:

    show = filtered[[

        "scan_time",

        "scan_type",

        "prediction",

        "risk",

        "score",

        "input_data"

    ]]

    st.dataframe(

        show,

        use_container_width=True,

        hide_index=True

    )

# ==========================================================
# EXPORT CSV
# ==========================================================

st.download_button(

    label="📥 Download CSV",

    data=filtered.to_csv(index=False),

    file_name="scan_history.csv",

    mime="text/csv"

)

# ==========================================================
# CHARTS
# ==========================================================

import plotly.express as px

st.markdown(

"<h2 class='section-title'>📊 Analytics</h2>",

unsafe_allow_html=True

)

left,right=st.columns(2)

# ==========================================================
# PIE CHART
# ==========================================================

with left:

    if len(filtered)>0:

        pie_df=filtered.groupby(

            "prediction"

        ).size().reset_index(name="Count")

        fig=px.pie(

            pie_df,

            values="Count",

            names="prediction",

            hole=0.55,

            color="prediction",

            color_discrete_map={

                "SAFE":"green",

                "SUSPICIOUS":"orange",

                "PHISHING":"red"

            }

        )

        fig.update_layout(

            paper_bgcolor="rgba(0,0,0,0)",

            plot_bgcolor="rgba(0,0,0,0)",

            font_color="white",

            height=430

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

# ==========================================================
# BAR CHART
# ==========================================================

with right:

    if len(filtered)>0:

        bar_df=filtered.groupby(

            "scan_type"

        ).size().reset_index(name="Count")

        fig=px.bar(

            bar_df,

            x="scan_type",

            y="Count",

            text="Count",

            color="scan_type",

            color_discrete_sequence=[

                "#00C8FF",

                "#00E676"

            ]

        )

        fig.update_layout(

            paper_bgcolor="rgba(0,0,0,0)",

            plot_bgcolor="rgba(0,0,0,0)",

            font_color="white",

            showlegend=False,

            height=430

        )

        fig.update_traces(

            textposition="outside"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

# ==========================================================
# DAILY TREND
# ==========================================================

st.markdown(

"<h2 class='section-title'>📈 Scan Timeline</h2>",

unsafe_allow_html=True

)

if len(filtered)>0:

    temp=filtered.copy()

    temp["scan_time"]=pd.to_datetime(

        temp["scan_time"]

    )

    trend=temp.groupby(

        temp["scan_time"].dt.date

    ).size().reset_index(name="Scans")

    fig=px.line(

        trend,

        x="scan_time",

        y="Scans",

        markers=True

    )

    fig.update_layout(

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font_color="white",

        height=430

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

# ==========================================================
# RECENT THREATS
# ==========================================================

st.markdown(

"<h2 class='section-title'>🚨 Recent Threats</h2>",

unsafe_allow_html=True

)

recent=filtered[

    filtered["prediction"]=="PHISHING"

].head(5)

if len(recent)==0:

    st.success(

        "No phishing entries found."

    )

else:

    st.dataframe(

        recent[[

            "scan_time",

            "scan_type",

            "input_data",

            "score"

        ]],

        use_container_width=True,

        hide_index=True

    )

    # ==========================================================
# CLEAR HISTORY
# ==========================================================

st.markdown(
    "<h2 class='section-title'>🗑 History Management</h2>",
    unsafe_allow_html=True
)

col1, col2 = st.columns([2,6])

with col1:

    if st.button("🗑 Clear Complete History", use_container_width=True):

        conn = sqlite3.connect(DB_NAME)

        cursor = conn.cursor()

        cursor.execute("DELETE FROM history")

        conn.commit()

        conn.close()

        st.success("History Deleted Successfully.")

        st.rerun()

# ==========================================================
# THREAT INSIGHTS
# ==========================================================

st.markdown(
    "<h2 class='section-title'>🧠 Threat Insights</h2>",
    unsafe_allow_html=True
)

c1, c2 = st.columns(2)

with c1:

    st.markdown(f"""

<div class="card">

<h3>📊 Scan Summary</h3>

<ul>

<li><b>Total Scans :</b> {total}</li>

<li><b>Safe :</b> {safe}</li>

<li><b>Suspicious :</b> {sus}</li>

<li><b>Phishing :</b> {phish}</li>

<li><b>URL Scans :</b> {url}</li>

<li><b>Email Scans :</b> {email}</li>

</ul>

</div>

""", unsafe_allow_html=True)

with c2:

    if total > 0:

        safe_rate = round((safe / total) * 100, 2)

        phishing_rate = round((phish / total) * 100, 2)

        suspicious_rate = round((sus / total) * 100, 2)

    else:

        safe_rate = 0

        phishing_rate = 0

        suspicious_rate = 0

    st.markdown(f"""

<div class="card">

<h3>📈 Detection Statistics</h3>

<ul>

<li><b>Safe Rate :</b> {safe_rate}%</li>

<li><b>Suspicious Rate :</b> {suspicious_rate}%</li>

<li><b>Threat Rate :</b> {phishing_rate}%</li>

<li><b>Detection Mode :</b> Hybrid AI</li>

<li><b>Rule Engine :</b> Enabled</li>

<li><b>Explainable AI :</b> Enabled</li>

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

    "Always verify the sender before opening attachments.",

    "Use Multi-Factor Authentication wherever possible.",

    "Check website spelling before entering credentials.",

    "Never share OTP or Passwords with anyone.",

    "Avoid downloading files from unknown sources.",

    "Always keep your browser and antivirus updated.",

    "Review scan history regularly to identify suspicious patterns."

]

import random

st.success(random.choice(tips))

# ==========================================================
# ABOUT HISTORY
# ==========================================================

st.markdown(
    "<h2 class='section-title'>ℹ About Scan History</h2>",
    unsafe_allow_html=True
)

st.markdown("""

<div class="card">

<h3>History Module</h3>

<p>

The Scan History module stores every URL and Email scan
performed by the system.

It allows users to:

<ul>

<li>Review previous detections.</li>

<li>Search and filter historical records.</li>

<li>Analyze phishing trends.</li>

<li>Export reports.</li>

<li>Monitor suspicious activities.</li>

</ul>

This improves security awareness and enables
better cyber threat monitoring.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# DEVELOPERS
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

📜 Adaptive Explainable Phishing Detection System

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
