"""
BankNova AI - Wealth OS
A premium, AI-powered personal wealth intelligence landing page & demo dashboard
built with Streamlit.
"""

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="BankNova AI | Wealth OS",
    page_icon="B",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def load_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .stApp {
            background: radial-gradient(circle at 15% 10%, #241608 0%, #0d0b08 35%, #0a0a0a 100%);
            color: #f2f2f2;
        }

        #MainMenu, header, footer {visibility: hidden;}

        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 1200px;
        }

        .bn-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 999px;
            padding: 6px 16px;
            font-size: 0.8rem;
            color: #d8d8d8;
            margin-bottom: 1.2rem;
        }

        .bn-logo {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .bn-logo-mark {
            width: 40px;
            height: 40px;
            border-radius: 10px;
            background: linear-gradient(135deg, #ffb648, #ff8a2b);
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 800;
            font-size: 1.1rem;
            color: #16110a;
        }

        .bn-logo-text-main {
            font-weight: 700;
            font-size: 1.05rem;
            color: #f5f5f5;
        }

        .bn-logo-text-sub {
            font-size: 0.65rem;
            letter-spacing: 0.12em;
            color: #9a9a9a;
        }

        .bn-hero-title {
            font-size: 3.6rem;
            font-weight: 800;
            line-height: 1.08;
            letter-spacing: -0.02em;
            color: #f5f5f5;
            margin: 0.4rem 0 1rem 0;
        }

        .bn-accent {
            color: #ff9d3d;
        }

        .bn-hero-sub {
            font-size: 1.1rem;
            color: #b8b8b8;
            line-height: 1.6;
            max-width: 520px;
            margin-bottom: 1.8rem;
        }

        .bn-pill-row {
            display: flex;
            gap: 22px;
            margin-top: 1.6rem;
            flex-wrap: wrap;
        }

        .bn-pill {
            font-size: 0.85rem;
            color: #b8b8b8;
            display: flex;
            align-items: center;
            gap: 7px;
        }

        .bn-dot {
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: #33d69f;
            display: inline-block;
        }

        .bn-card {
            background: rgba(255, 255, 255, 0.035);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 18px;
            padding: 28px;
            backdrop-filter: blur(6px);
        }

        .bn-portfolio-label {
            font-size: 0.72rem;
            letter-spacing: 0.14em;
            color: #8f8f8f;
            text-transform: uppercase;
        }

        .bn-portfolio-value {
            font-family: 'JetBrains Mono', monospace;
            font-size: 2.4rem;
            font-weight: 700;
            color: #f7f7f7;
            margin-top: 4px;
        }

        .bn-portfolio-sub {
            font-size: 0.8rem;
            color: #7a7a7a;
            margin-top: 2px;
        }

        .bn-yoy {
            color: #33d69f;
            font-weight: 600;
            font-size: 0.85rem;
        }

        .bn-mini-stat {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 12px;
            padding: 14px 16px;
        }

        .bn-mini-label {
            font-size: 0.68rem;
            letter-spacing: 0.1em;
            color: #8f8f8f;
            text-transform: uppercase;
        }

        .bn-mini-value {
            font-family: 'JetBrains Mono', monospace;
            font-size: 1.1rem;
            font-weight: 600;
            color: #f0f0f0;
            margin-top: 2px;
        }

        .bn-insight {
            background: rgba(20, 16, 12, 0.9);
            border: 1px solid rgba(255, 157, 61, 0.25);
            border-radius: 14px;
            padding: 16px 18px;
            font-size: 0.85rem;
            color: #dddddd;
            line-height: 1.5;
        }

        .bn-insight-title {
            font-size: 0.68rem;
            letter-spacing: 0.1em;
            color: #ff9d3d;
            text-transform: uppercase;
            font-weight: 600;
            margin-bottom: 6px;
        }

        .bn-feature-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.07);
            border-radius: 16px;
            padding: 24px;
            height: 100%;
            transition: border-color 0.2s ease;
        }

        .bn-feature-icon {
            font-size: 1.4rem;
            margin-bottom: 14px;
        }

        .bn-feature-title {
            font-weight: 700;
            font-size: 1.02rem;
            color: #f2f2f2;
            margin-bottom: 8px;
        }

        .bn-feature-desc {
            font-size: 0.86rem;
            color: #9d9d9d;
            line-height: 1.55;
        }

        .bn-section-heading {
            font-size: 1.8rem;
            font-weight: 700;
            color: #f2f2f2;
            margin-bottom: 0.4rem;
        }

        .bn-section-sub {
            color: #9a9a9a;
            font-size: 0.95rem;
            margin-bottom: 2rem;
        }

        .bn-footer {
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            margin-top: 3rem;
            padding-top: 1.4rem;
            display: flex;
            justify-content: space-between;
            font-size: 0.8rem;
            color: #7a7a7a;
            flex-wrap: wrap;
            gap: 10px;
        }

        .bn-goal-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.07);
            border-radius: 14px;
            padding: 20px;
        }

        .bn-goal-title {
            font-weight: 600;
            color: #f0f0f0;
            font-size: 0.95rem;
            margin-bottom: 10px;
        }

        .bn-goal-percent {
            font-family: 'JetBrains Mono', monospace;
            color: #ff9d3d;
            font-weight: 700;
        }

        div.stButton > button {
            background: linear-gradient(135deg, #ffb648, #ff8a2b);
            color: #16110a;
            font-weight: 700;
            border: none;
            border-radius: 10px;
            padding: 0.6rem 1.4rem;
        }

        div.stButton > button:hover {
            background: linear-gradient(135deg, #ffc36a, #ff9a44);
            color: #16110a;
        }

        section[data-testid="stSidebar"] {
            background: #0d0b08;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def top_nav():
    col1, col2, col3 = st.columns([5, 1, 1.4])
    with col1:
        st.markdown(
            """
            <div class="bn-logo">
                <div class="bn-logo-mark">B</div>
                <div>
                    <div class="bn-logo-text-main">BankNova <span class="bn-accent">AI</span></div>
                    <div class="bn-logo-text-sub">WEALTH OS</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown("<div style='padding-top:10px;text-align:right;color:#ddd;'>Log in</div>", unsafe_allow_html=True)
    with col3:
        st.button("Get started", key="nav_get_started")


def hero_section():
    left, right = st.columns([1.15, 1], gap="large")

    with left:
        st.markdown(
            """
            <div class="bn-badge">✨ Powered by Gemini 3 &middot; Built for India</div>
            <div class="bn-hero-title">Your <span class="bn-accent">personal wealth</span><br>intelligence layer.</div>
            <div class="bn-hero-sub">
                BankNova AI is a premium digital wealth OS that understands your money in ₹,
                forecasts your goals, and explains every recommendation like a private banker would.
            </div>
            """,
            unsafe_allow_html=True,
        )
        b1, b2 = st.columns([1, 1.4])
        with b1:
            st.button("Open free account →", key="hero_cta", use_container_width=True)
        with b2:
            st.markdown(
                "<div style='padding-top:10px;color:#ccc;text-decoration:underline;font-size:0.9rem;'>I already have an account</div>",
                unsafe_allow_html=True,
            )
        st.markdown(
            """
            <div class="bn-pill-row">
                <div class="bn-pill"><span class="bn-dot"></span>Bank-grade security</div>
                <div class="bn-pill"><span class="bn-dot"></span>Explainable AI</div>
                <div class="bn-pill"><span class="bn-dot"></span>INR-native</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        st.markdown('<div class="bn-card">', unsafe_allow_html=True)
        st.markdown(
            """
            <div style="display:flex;justify-content:space-between;align-items:flex-start;">
                <div>
                    <div class="bn-portfolio-label">Portfolio</div>
                    <div class="bn-portfolio-value">₹24,85,320</div>
                    <div class="bn-portfolio-sub">Total wealth &middot; Feb 2026</div>
                </div>
                <div class="bn-yoy">+12.4% YoY</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("<div style='height:16px;'></div>", unsafe_allow_html=True)

        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown(
                '<div class="bn-mini-stat"><div class="bn-mini-label">Savings</div><div class="bn-mini-value">₹3.5L</div></div>',
                unsafe_allow_html=True,
            )
        with m2:
            st.markdown(
                '<div class="bn-mini-stat"><div class="bn-mini-label">Investments</div><div class="bn-mini-value">₹18.2L</div></div>',
                unsafe_allow_html=True,
            )
        with m3:
            st.markdown(
                '<div class="bn-mini-stat"><div class="bn-mini-label">Emergency</div><div class="bn-mini-value">₹3.1L</div></div>',
                unsafe_allow_html=True,
            )

        st.markdown("<div style='height:18px;'></div>", unsafe_allow_html=True)

        rng = np.random.default_rng(42)
        months = pd.date_range("2025-03-01", periods=12, freq="MS")
        base = np.linspace(19.5, 24.85, 12)
        noise = rng.normal(0, 0.25, 12)
        values = base + noise
        chart_df = pd.DataFrame({"Month": months, "Wealth (₹ Lakhs)": values}).set_index("Month")
        st.area_chart(chart_df, height=160, color="#ff8a2b")

        st.markdown(
            """
            <div class="bn-insight">
                <div class="bn-insight-title">✨ AI Insight</div>
                You're on track for retirement at 58. Bumping SIP by ₹5K lands you there at 55.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)


def features_section():
    st.markdown("<div style='height:2.4rem;'></div>", unsafe_allow_html=True)
    features = [
        ("🤖", "AI Financial Advisor", "Chat with a Gemini-powered advisor trained on Indian markets, taxes & personal finance."),
        ("📈", "Portfolio X-Ray", "Upload CSV. Get diversification score, risk metrics & AI rebalancing suggestions."),
        ("✨", "Goal Planning", "Inflation-adjusted SIP calculators for retirement, education, home & every life goal."),
        ("🛡️", "Financial Health", "7-pillar health score with explainable insights across savings, debt, insurance & more."),
    ]
    cols = st.columns(4, gap="medium")
    for col, (icon, title, desc) in zip(cols, features):
        with col:
            st.markdown(
                f"""
                <div class="bn-feature-card">
                    <div class="bn-feature-icon">{icon}</div>
                    <div class="bn-feature-title">{title}</div>
                    <div class="bn-feature-desc">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def demo_section():
    st.markdown("<div style='height:3.2rem;'></div>", unsafe_allow_html=True)
    st.markdown('<div class="bn-section-heading">Try the Wealth OS demo</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="bn-section-sub">A quick look at how BankNova AI breaks your goals down and tracks progress in real time.</div>',
        unsafe_allow_html=True,
    )

    tab1, tab2 = st.tabs(["Goal Planning", "Portfolio X-Ray"])

    with tab1:
        goals = [
            {"name": "Retirement at 55", "target": 20000000, "saved": 8200000},
            {"name": "Child's Education", "target": 5000000, "saved": 1400000},
            {"name": "Dream Home (Down Payment)", "target": 3500000, "saved": 2650000},
            {"name": "Emergency Fund (12mo)", "target": 900000, "saved": 620000},
        ]
        cols = st.columns(2, gap="medium")
        for i, g in enumerate(goals):
            pct = int(g["saved"] / g["target"] * 100)
            with cols[i % 2]:
                st.markdown(
                    f"""
                    <div class="bn-goal-card">
                        <div class="bn-goal-title">{g['name']}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.progress(pct / 100)
                st.markdown(
                    f"<div style='color:#9a9a9a;font-size:0.82rem;margin-top:-8px;'>₹{g['saved']:,} of ₹{g['target']:,} &nbsp; "
                    f"<span class='bn-goal-percent'>{pct}%</span></div>",
                    unsafe_allow_html=True,
                )
                st.markdown("<div style='height:14px;'></div>", unsafe_allow_html=True)

    with tab2:
        st.markdown("<div style='height:0.6rem;'></div>", unsafe_allow_html=True)
        allocation = pd.DataFrame(
            {
                "Asset Class": ["Equity (Direct)", "Mutual Funds", "Fixed Deposits", "Gold / Digital Gold", "Cash & Savings"],
                "Allocation (%)": [34, 28, 18, 10, 10],
            }
        ).set_index("Asset Class")
        c1, c2 = st.columns([1.2, 1])
        with c1:
            st.bar_chart(allocation, height=280, color="#ff8a2b")
        with c2:
            st.markdown(
                """
                <div class="bn-insight">
                    <div class="bn-insight-title">✨ Diversification Score: 7.4 / 10</div>
                    Your equity exposure is healthy, but Fixed Deposits are dragging real returns
                    below inflation. Consider shifting 5-8% into diversified equity mutual funds
                    over the next 2 quarters.
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)
            st.markdown(
                """
                <div class="bn-insight">
                    <div class="bn-insight-title">Risk Metrics</div>
                    Volatility: Moderate &middot; Sharpe Ratio: 1.18 &middot; Max Drawdown: -14.2%
                </div>
                """,
                unsafe_allow_html=True,
            )


def footer_section():
    st.markdown(
        """
        <div class="bn-footer">
            <div>© 2026 BankNova AI &middot; Built for IDBI Innovate 2026</div>
            <div>This is a demo prototype &mdash; not licensed investment advice.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def main():
    load_css()
    top_nav()
    st.markdown("<div style='height:1.6rem;'></div>", unsafe_allow_html=True)
    hero_section()
    features_section()
    demo_section()
    footer_section()


if __name__ == "__main__":
    main()
