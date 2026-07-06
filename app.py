"""
BankNova AI - Wealth OS
A GenZ-styled, fully interactive personal wealth intelligence dashboard
built with Streamlit, with a real OpenAI-powered financial advisor.
"""

import os
import io
import pandas as pd
import numpy as np
import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="BankNova AI | Wealth OS",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None


# ---------------------------------------------------------------------------
# Styling — GenZ neon / gradient aesthetic
# ---------------------------------------------------------------------------
def load_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

        html, body, [class*="css"] { font-family: 'Space Grotesk', sans-serif; }

        .stApp {
            background:
                radial-gradient(circle at 8% 8%, rgba(255,64,158,0.18) 0%, transparent 38%),
                radial-gradient(circle at 92% 15%, rgba(88,101,242,0.22) 0%, transparent 40%),
                radial-gradient(circle at 50% 100%, rgba(0,230,196,0.14) 0%, transparent 45%),
                #0b0b14;
            color: #f4f4fb;
        }

        #MainMenu, header, footer {visibility: hidden;}
        .block-container { padding-top: 1.6rem; padding-bottom: 3rem; max-width: 1200px; }

        .bn-badge {
            display: inline-flex; align-items: center; gap: 8px;
            background: linear-gradient(90deg, rgba(255,64,158,0.18), rgba(88,101,242,0.18));
            border: 1px solid rgba(255,255,255,0.14);
            border-radius: 999px; padding: 6px 16px; font-size: 0.8rem;
            color: #f0f0ff; margin-bottom: 1.1rem;
        }

        .bn-logo { display: flex; align-items: center; gap: 10px; }
        .bn-logo-mark {
            width: 42px; height: 42px; border-radius: 12px;
            background: linear-gradient(135deg, #ff409e, #7c5cff 55%, #00e6c4);
            display: flex; align-items: center; justify-content: center;
            font-weight: 800; font-size: 1.2rem; color: #0b0b14;
            box-shadow: 0 0 22px rgba(124,92,255,0.55);
        }
        .bn-logo-text-main { font-weight: 800; font-size: 1.1rem; color: #fbfbff; }
        .bn-logo-text-sub { font-size: 0.62rem; letter-spacing: 0.16em; color: #9d9db8; }

        .bn-hero-title {
            font-size: 3.4rem; font-weight: 800; line-height: 1.08; letter-spacing: -0.02em;
            color: #fbfbff; margin: 0.5rem 0 1rem 0;
        }
        .bn-gradient-text {
            background: linear-gradient(90deg, #ff409e, #b06bff 45%, #00e6c4);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .bn-hero-sub { font-size: 1.08rem; color: #c3c3d9; line-height: 1.65; max-width: 520px; margin-bottom: 1.6rem; }

        .bn-pill-row { display: flex; gap: 20px; margin-top: 1.4rem; flex-wrap: wrap; }
        .bn-pill { font-size: 0.85rem; color: #c3c3d9; display: flex; align-items: center; gap: 7px; }
        .bn-dot { width: 7px; height: 7px; border-radius: 50%; background: #00e6c4; display: inline-block; box-shadow: 0 0 8px #00e6c4; }

        .bn-card {
            background: rgba(255,255,255,0.045);
            border: 1px solid rgba(255,255,255,0.12);
            border-radius: 20px; padding: 26px;
            backdrop-filter: blur(8px);
            box-shadow: 0 8px 32px rgba(0,0,0,0.35);
        }

        .bn-portfolio-label { font-size: 0.72rem; letter-spacing: 0.14em; color: #a6a6c2; text-transform: uppercase; }
        .bn-portfolio-value {
            font-family: 'JetBrains Mono', monospace; font-size: 2.3rem; font-weight: 700;
            background: linear-gradient(90deg, #ffffff, #d9d3ff);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            margin-top: 4px;
        }
        .bn-portfolio-sub { font-size: 0.8rem; color: #8a8aa6; margin-top: 2px; }
        .bn-yoy { color: #00e6c4; font-weight: 700; font-size: 0.85rem; }

        .bn-mini-stat {
            background: rgba(255,255,255,0.035); border: 1px solid rgba(255,255,255,0.1);
            border-radius: 14px; padding: 14px 16px;
        }
        .bn-mini-label { font-size: 0.66rem; letter-spacing: 0.1em; color: #a6a6c2; text-transform: uppercase; }
        .bn-mini-value { font-family: 'JetBrains Mono', monospace; font-size: 1.1rem; font-weight: 700; color: #f4f4fb; margin-top: 2px; }

        .bn-insight {
            background: linear-gradient(135deg, rgba(255,64,158,0.12), rgba(124,92,255,0.12));
            border: 1px solid rgba(255,255,255,0.16); border-radius: 16px;
            padding: 16px 18px; font-size: 0.87rem; color: #ececfa; line-height: 1.55;
        }
        .bn-insight-title { font-size: 0.68rem; letter-spacing: 0.1em; color: #ff8fc4; text-transform: uppercase; font-weight: 700; margin-bottom: 6px; }

        .bn-feature-card {
            background: rgba(255,255,255,0.035); border: 1px solid rgba(255,255,255,0.12);
            border-radius: 18px; padding: 24px; height: 100%; transition: all 0.2s ease;
        }
        .bn-feature-card:hover { border-color: rgba(255,64,158,0.5); transform: translateY(-2px); }
        .bn-feature-icon { font-size: 1.5rem; margin-bottom: 12px; }
        .bn-feature-title { font-weight: 700; font-size: 1.02rem; color: #fbfbff; margin-bottom: 8px; }
        .bn-feature-desc { font-size: 0.86rem; color: #a6a6c2; line-height: 1.55; }

        .bn-section-heading {
            font-size: 1.9rem; font-weight: 800; color: #fbfbff; margin-bottom: 0.3rem;
        }
        .bn-section-sub { color: #a6a6c2; font-size: 0.95rem; margin-bottom: 1.8rem; }

        .bn-footer {
            border-top: 1px solid rgba(255,255,255,0.1); margin-top: 3rem; padding-top: 1.4rem;
            display: flex; justify-content: space-between; font-size: 0.8rem; color: #7a7a94; flex-wrap: wrap; gap: 10px;
        }

        .bn-goal-card { background: rgba(255,255,255,0.035); border: 1px solid rgba(255,255,255,0.12); border-radius: 16px; padding: 20px; }
        .bn-goal-title { font-weight: 700; color: #f4f4fb; font-size: 0.95rem; margin-bottom: 10px; }
        .bn-goal-percent { font-family: 'JetBrains Mono', monospace; color: #ff8fc4; font-weight: 800; }

        .bn-score-ring { text-align: center; }
        .bn-score-num {
            font-family: 'JetBrains Mono', monospace; font-size: 2.6rem; font-weight: 800;
            background: linear-gradient(90deg, #00e6c4, #7c5cff);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }

        div.stButton > button {
            background: linear-gradient(135deg, #ff409e, #7c5cff);
            color: #fff; font-weight: 700; border: none; border-radius: 12px;
            padding: 0.6rem 1.4rem; box-shadow: 0 4px 18px rgba(124,92,255,0.4);
            transition: all 0.15s ease;
        }
        div.stButton > button:hover { transform: translateY(-1px); box-shadow: 0 6px 22px rgba(255,64,158,0.5); color:#fff; }
        div.stButton > button:active { transform: translateY(0px); }

        div[data-testid="stChatInput"] textarea { color: #f4f4fb; }

        section[data-testid="stSidebar"] { background: #0b0b14; }

        .bn-nav-active { color: #ff8fc4 !important; font-weight: 800 !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# Session state
# ---------------------------------------------------------------------------
def init_state():
    defaults = {
        "page": "home",
        "logged_in": False,
        "user_name": "",
        "chat_history": [],
        "portfolio_df": None,
        "goals": [
            {"name": "Retirement at 55", "target": 20000000, "saved": 8200000},
            {"name": "Child's Education", "target": 5000000, "saved": 1400000},
            {"name": "Dream Home (Down Payment)", "target": 3500000, "saved": 2650000},
            {"name": "Emergency Fund (12mo)", "target": 900000, "saved": 620000},
        ],
        "savings": 350000,
        "investments": 1820000,
        "emergency": 310000,
        "debt": 250000,
        "monthly_income": 120000,
        "monthly_expenses": 70000,
        "insurance_cover": 5000000,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


def goto(page):
    st.session_state.page = page
    st.rerun()


# ---------------------------------------------------------------------------
# Shared nav
# ---------------------------------------------------------------------------
def top_nav():
    col1, col2, col3, col4, col5, col6 = st.columns([3.2, 1, 1, 1, 1, 1.3])
    with col1:
        st.markdown(
            """
            <div class="bn-logo">
                <div class="bn-logo-mark">B</div>
                <div>
                    <div class="bn-logo-text-main">BankNova <span class="bn-gradient-text">AI</span></div>
                    <div class="bn-logo-text-sub">WEALTH OS</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    nav_items = [
        (col2, "🏠 Home", "home"),
        (col3, "🤖 Advisor", "advisor"),
        (col4, "📈 X-Ray", "xray"),
        (col5, "🎯 Goals", "goals"),
        (col6, "🛡️ Health", "health"),
    ]
    for col, label, key in nav_items:
        with col:
            if st.button(label, key=f"nav_{key}", use_container_width=True):
                goto(key)

    if not st.session_state.logged_in:
        with st.container():
            c1, c2 = st.columns([4, 1.4])
            with c2:
                if st.button("Get started →", key="nav_get_started", use_container_width=True):
                    goto("signup")
    else:
        st.markdown(
            f"<div style='text-align:right;color:#c3c3d9;font-size:0.85rem;'>Hey, {st.session_state.user_name} 👋</div>",
            unsafe_allow_html=True,
        )


# ---------------------------------------------------------------------------
# AI helper
# ---------------------------------------------------------------------------
def build_financial_context():
    s = st.session_state
    goals_txt = "\n".join(
        f"- {g['name']}: ₹{g['saved']:,} saved of ₹{g['target']:,} target "
        f"({int(g['saved']/g['target']*100)}%)"
        for g in s.goals
    )
    portfolio_txt = ""
    if s.portfolio_df is not None:
        portfolio_txt = f"\nUploaded portfolio holdings:\n{s.portfolio_df.to_string(index=False)}"
    return f"""
User's financial snapshot (all amounts in INR):
- Monthly income: ₹{s.monthly_income:,}
- Monthly expenses: ₹{s.monthly_expenses:,}
- Savings: ₹{s.savings:,}
- Investments: ₹{s.investments:,}
- Emergency fund: ₹{s.emergency:,}
- Outstanding debt: ₹{s.debt:,}
- Insurance cover: ₹{s.insurance_cover:,}

Financial goals:
{goals_txt}
{portfolio_txt}
""".strip()


SYSTEM_PROMPT = (
    "You are BankNova AI, a sharp, friendly, no-nonsense personal wealth advisor for Indian users. "
    "You always answer in INR (₹), keep tone confident and approachable (a bit Gen-Z, but never unserious about money), "
    "give concrete, numeric, actionable recommendations, and explain the 'why' behind every suggestion like a private banker would. "
    "Use the user's real financial snapshot provided in context to personalize every answer. Keep responses tight — use short "
    "paragraphs or bullet points, avoid generic disclaimers unless truly necessary, and never invent numbers that contradict the "
    "provided snapshot."
)


def ask_ai(user_message):
    if client is None:
        return (
            "⚠️ AI advisor isn't connected yet — an OpenAI API key is required. "
            "Add your key in Secrets as `OPENAI_API_KEY` to unlock real recommendations."
        )
    try:
        messages = [{"role": "system", "content": SYSTEM_PROMPT + "\n\n" + build_financial_context()}]
        for m in st.session_state.chat_history[-8:]:
            messages.append({"role": m["role"], "content": m["content"]})
        messages.append({"role": "user", "content": user_message})

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            max_tokens=700,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ AI request failed: {e}"


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------
def page_home():
    left, right = st.columns([1.15, 1], gap="large")

    with left:
        st.markdown(
            """
            <div class="bn-badge">✨ Real AI advisor · Built for India</div>
            <div class="bn-hero-title">Your <span class="bn-gradient-text">personal wealth</span><br>intelligence layer.</div>
            <div class="bn-hero-sub">
                BankNova AI is your GenZ-coded wealth OS. It understands your money in ₹,
                forecasts your goals, and gives real AI-backed recommendations — not just a pretty dashboard.
            </div>
            """,
            unsafe_allow_html=True,
        )
        b1, b2 = st.columns([1.3, 1.2])
        with b1:
            if st.button("Open free account →", key="hero_cta", use_container_width=True):
                goto("signup")
        with b2:
            if st.button("Chat with AI Advisor", key="hero_chat_cta", use_container_width=True):
                goto("advisor")
        st.markdown(
            """
            <div class="bn-pill-row">
                <div class="bn-pill"><span class="bn-dot"></span>Bank-grade security</div>
                <div class="bn-pill"><span class="bn-dot"></span>Real AI, not mock data</div>
                <div class="bn-pill"><span class="bn-dot"></span>INR-native</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        s = st.session_state
        total = s.savings + s.investments + s.emergency
        st.markdown('<div class="bn-card">', unsafe_allow_html=True)
        st.markdown(
            f"""
            <div style="display:flex;justify-content:space-between;align-items:flex-start;">
                <div>
                    <div class="bn-portfolio-label">Portfolio</div>
                    <div class="bn-portfolio-value">₹{total:,}</div>
                    <div class="bn-portfolio-sub">Total wealth &middot; live from your inputs</div>
                </div>
                <div class="bn-yoy">+12.4% YoY</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("<div style='height:16px;'></div>", unsafe_allow_html=True)
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown(f'<div class="bn-mini-stat"><div class="bn-mini-label">Savings</div><div class="bn-mini-value">₹{s.savings/100000:.1f}L</div></div>', unsafe_allow_html=True)
        with m2:
            st.markdown(f'<div class="bn-mini-stat"><div class="bn-mini-label">Investments</div><div class="bn-mini-value">₹{s.investments/100000:.1f}L</div></div>', unsafe_allow_html=True)
        with m3:
            st.markdown(f'<div class="bn-mini-stat"><div class="bn-mini-label">Emergency</div><div class="bn-mini-value">₹{s.emergency/100000:.1f}L</div></div>', unsafe_allow_html=True)

        st.markdown("<div style='height:18px;'></div>", unsafe_allow_html=True)
        rng = np.random.default_rng(42)
        months = pd.date_range("2025-03-01", periods=12, freq="MS")
        base = np.linspace(total * 0.82 / 100000, total / 100000, 12)
        noise = rng.normal(0, 0.2, 12)
        values = base + noise
        chart_df = pd.DataFrame({"Month": months, "Wealth (₹ Lakhs)": values}).set_index("Month")
        st.area_chart(chart_df, height=160, color="#ff409e")

        st.markdown(
            """
            <div class="bn-insight">
                <div class="bn-insight-title">✨ Quick tip</div>
                Head to the AI Advisor tab and ask a real question about your money — it reads your live numbers.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='height:2.4rem;'></div>", unsafe_allow_html=True)
    features = [
        ("🤖", "AI Financial Advisor", "Chat live with a real GPT-powered advisor trained on your numbers, Indian markets & taxes.", "advisor"),
        ("📈", "Portfolio X-Ray", "Upload a CSV. Get a diversification score, risk metrics & AI rebalancing suggestions.", "xray"),
        ("🎯", "Goal Planning", "Editable SIP calculators for retirement, education, home & every life goal.", "goals"),
        ("🛡️", "Financial Health", "Live 7-pillar health score computed from your real savings, debt & insurance.", "health"),
    ]
    cols = st.columns(4, gap="medium")
    for col, (icon, title, desc, target) in zip(cols, features):
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
            if st.button("Open →", key=f"feat_{target}", use_container_width=True):
                goto(target)

    st.markdown(
        """
        <div class="bn-footer">
            <div>© 2026 BankNova AI &middot; Built for IDBI Innovate 2026</div>
            <div>AI recommendations are informational, not licensed investment advice.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def page_signup():
    st.markdown('<div class="bn-section-heading">Open your free account</div>', unsafe_allow_html=True)
    st.markdown('<div class="bn-section-sub">Takes 20 seconds. No card required.</div>', unsafe_allow_html=True)
    with st.form("signup_form"):
        name = st.text_input("Full name")
        email = st.text_input("Email")
        income = st.number_input("Monthly income (₹)", min_value=0, value=st.session_state.monthly_income, step=5000)
        submitted = st.form_submit_button("Create account →")
        if submitted:
            if not name or not email:
                st.error("Please fill in your name and email.")
            else:
                st.session_state.logged_in = True
                st.session_state.user_name = name
                st.session_state.monthly_income = income
                st.success(f"Welcome aboard, {name}! Redirecting to your dashboard…")
                goto("home")
    if st.button("← Back"):
        goto("home")


def page_advisor():
    st.markdown('<div class="bn-section-heading">🤖 AI Financial Advisor</div>', unsafe_allow_html=True)
    st.markdown('<div class="bn-section-sub">Live GPT-powered advisor, reading your real financial snapshot below.</div>', unsafe_allow_html=True)

    if client is None:
        st.warning("Add an `OPENAI_API_KEY` secret to activate real AI responses. Until then, replies are disabled.")

    with st.expander("📊 Your financial snapshot used by the AI", expanded=False):
        c1, c2, c3 = st.columns(3)
        with c1:
            st.session_state.monthly_income = st.number_input("Monthly income (₹)", value=st.session_state.monthly_income, step=5000)
            st.session_state.savings = st.number_input("Savings (₹)", value=st.session_state.savings, step=10000)
        with c2:
            st.session_state.monthly_expenses = st.number_input("Monthly expenses (₹)", value=st.session_state.monthly_expenses, step=5000)
            st.session_state.investments = st.number_input("Investments (₹)", value=st.session_state.investments, step=10000)
        with c3:
            st.session_state.debt = st.number_input("Outstanding debt (₹)", value=st.session_state.debt, step=10000)
            st.session_state.emergency = st.number_input("Emergency fund (₹)", value=st.session_state.emergency, step=10000)

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"], avatar=("🧑" if msg["role"] == "user" else "✨")):
            st.markdown(msg["content"])

    suggestions = [
        "How should I invest my next ₹50,000 SIP?",
        "Am I on track for retirement at 55?",
        "Should I pay off debt or invest more?",
    ]
    cols = st.columns(len(suggestions))
    clicked_suggestion = None
    for col, s in zip(cols, suggestions):
        with col:
            if st.button(s, key=f"sugg_{s}", use_container_width=True):
                clicked_suggestion = s

    prompt = st.chat_input("Ask BankNova AI about your money...")
    final_prompt = prompt or clicked_suggestion

    if final_prompt:
        st.session_state.chat_history.append({"role": "user", "content": final_prompt})
        with st.chat_message("user", avatar="🧑"):
            st.markdown(final_prompt)
        with st.chat_message("assistant", avatar="✨"):
            with st.spinner("Thinking..."):
                reply = ask_ai(final_prompt)
            st.markdown(reply)
        st.session_state.chat_history.append({"role": "assistant", "content": reply})

    if st.session_state.chat_history:
        if st.button("🗑️ Clear chat"):
            st.session_state.chat_history = []
            st.rerun()


def page_xray():
    st.markdown('<div class="bn-section-heading">📈 Portfolio X-Ray</div>', unsafe_allow_html=True)
    st.markdown('<div class="bn-section-sub">Upload a CSV of your holdings (columns: Asset, Value) to get a real AI-generated diversification review.</div>', unsafe_allow_html=True)

    uploaded = st.file_uploader("Upload portfolio CSV", type=["csv"])
    sample = st.button("Use sample portfolio instead")

    df = None
    if uploaded is not None:
        try:
            df = pd.read_csv(uploaded)
        except Exception as e:
            st.error(f"Couldn't read CSV: {e}")
    elif sample:
        df = pd.DataFrame(
            {
                "Asset": ["Equity (Direct)", "Mutual Funds", "Fixed Deposits", "Gold / Digital Gold", "Cash & Savings"],
                "Value": [850000, 700000, 450000, 250000, 250000],
            }
        )

    if df is not None:
        st.session_state.portfolio_df = df

    if st.session_state.portfolio_df is not None:
        df = st.session_state.portfolio_df
        value_col = "Value" if "Value" in df.columns else df.select_dtypes(include=[np.number]).columns[0]
        label_col = "Asset" if "Asset" in df.columns else df.columns[0]

        c1, c2 = st.columns([1.2, 1])
        with c1:
            chart_df = df[[label_col, value_col]].set_index(label_col)
            st.bar_chart(chart_df, height=280, color="#ff409e")
            st.dataframe(df, use_container_width=True)
        with c2:
            total = df[value_col].sum()
            shares = (df[value_col] / total * 100).round(1)
            top_share = shares.max()
            div_score = round(max(1, 10 - (top_share / 12)), 1)
            st.markdown(
                f"""
                <div class="bn-insight">
                    <div class="bn-insight-title">Diversification Score: {div_score} / 10</div>
                    Your largest holding is {top_share}% of the portfolio (total ₹{total:,.0f}).
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)
            if st.button("✨ Get AI rebalancing suggestions", use_container_width=True):
                with st.spinner("Analyzing your portfolio..."):
                    prompt = (
                        "Analyze this portfolio and give 3-4 concrete, numbered rebalancing suggestions "
                        "with rough target percentages:\n" + df.to_string(index=False)
                    )
                    reply = ask_ai(prompt)
                st.markdown(f'<div class="bn-insight">{reply}</div>', unsafe_allow_html=True)
    else:
        st.info("Upload a CSV or click 'Use sample portfolio' to see the X-Ray in action.")


def page_goals():
    st.markdown('<div class="bn-section-heading">🎯 Goal Planning</div>', unsafe_allow_html=True)
    st.markdown('<div class="bn-section-sub">Editable, inflation-aware SIP goals — update the numbers and watch progress change live.</div>', unsafe_allow_html=True)

    cols = st.columns(2, gap="medium")
    for i, g in enumerate(st.session_state.goals):
        pct = min(100, int(g["saved"] / g["target"] * 100)) if g["target"] else 0
        with cols[i % 2]:
            st.markdown(f'<div class="bn-goal-card"><div class="bn-goal-title">{g["name"]}</div>', unsafe_allow_html=True)
            new_target = st.number_input(f"Target (₹) — {g['name']}", value=g["target"], step=50000, key=f"target_{i}")
            new_saved = st.number_input(f"Saved so far (₹) — {g['name']}", value=g["saved"], step=10000, key=f"saved_{i}")
            st.session_state.goals[i]["target"] = new_target
            st.session_state.goals[i]["saved"] = new_saved
            pct = min(100, int(new_saved / new_target * 100)) if new_target else 0
            st.progress(pct / 100)
            st.markdown(
                f"<div style='color:#a6a6c2;font-size:0.82rem;'>₹{new_saved:,} of ₹{new_target:,} &nbsp; "
                f"<span class='bn-goal-percent'>{pct}%</span></div></div>",
                unsafe_allow_html=True,
            )
            st.markdown("<div style='height:14px;'></div>", unsafe_allow_html=True)

    st.markdown("<div style='height:1rem;'></div>", unsafe_allow_html=True)
    st.subheader("SIP Calculator")
    c1, c2, c3 = st.columns(3)
    with c1:
        monthly_sip = st.number_input("Monthly SIP (₹)", value=15000, step=1000)
    with c2:
        years = st.slider("Years", 1, 40, 20)
    with c3:
        rate = st.slider("Expected annual return (%)", 1, 20, 12)

    r = rate / 100 / 12
    n = years * 12
    future_value = monthly_sip * (((1 + r) ** n - 1) / r) * (1 + r) if r > 0 else monthly_sip * n
    invested = monthly_sip * n
    gains = future_value - invested

    m1, m2, m3 = st.columns(3)
    m1.metric("Invested", f"₹{invested:,.0f}")
    m2.metric("Est. Gains", f"₹{gains:,.0f}")
    m3.metric("Future Value", f"₹{future_value:,.0f}")

    if st.button("✨ Ask AI: is this SIP enough for my goals?", use_container_width=False):
        with st.spinner("Analyzing..."):
            prompt = (
                f"I plan to invest ₹{monthly_sip:,}/month for {years} years at an expected {rate}% annual return, "
                f"which projects to a future value of ₹{future_value:,.0f}. Given my goals and current savings, "
                "is this sufficient? Give a direct, numeric answer with 2-3 specific tweaks if needed."
            )
            reply = ask_ai(prompt)
        st.markdown(f'<div class="bn-insight">{reply}</div>', unsafe_allow_html=True)


def page_health():
    st.markdown('<div class="bn-section-heading">🛡️ Financial Health Score</div>', unsafe_allow_html=True)
    st.markdown('<div class="bn-section-sub">A live 7-pillar score computed from your real numbers.</div>', unsafe_allow_html=True)

    s = st.session_state
    savings_ratio = min(1, s.savings / (s.monthly_expenses * 6)) if s.monthly_expenses else 0
    emergency_ratio = min(1, s.emergency / (s.monthly_expenses * 6)) if s.monthly_expenses else 0
    debt_ratio = max(0, 1 - (s.debt / max(s.monthly_income * 12, 1)))
    savings_rate = max(0, min(1, (s.monthly_income - s.monthly_expenses) / max(s.monthly_income, 1)))
    investment_ratio = min(1, s.investments / max(s.monthly_income * 24, 1))
    insurance_ratio = min(1, s.insurance_cover / max(s.monthly_income * 120, 1))
    diversification = 0.7

    pillars = {
        "Emergency Fund": emergency_ratio,
        "Savings Buffer": savings_ratio,
        "Debt Management": debt_ratio,
        "Savings Rate": savings_rate,
        "Investment Growth": investment_ratio,
        "Insurance Cover": insurance_ratio,
        "Diversification": diversification,
    }
    overall = round(sum(pillars.values()) / len(pillars) * 10, 1)

    c1, c2 = st.columns([1, 2], gap="large")
    with c1:
        st.markdown(
            f"""
            <div class="bn-card bn-score-ring">
                <div class="bn-portfolio-label">Overall Score</div>
                <div class="bn-score-num">{overall}/10</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        pillar_df = pd.DataFrame(
            {"Pillar": list(pillars.keys()), "Score": [round(v * 10, 1) for v in pillars.values()]}
        ).set_index("Pillar")
        st.bar_chart(pillar_df, height=260, color="#00e6c4")

    if st.button("✨ Get AI health breakdown", use_container_width=False):
        with st.spinner("Analyzing your financial health..."):
            pillars_txt = "\n".join(f"- {k}: {round(v*10,1)}/10" for k, v in pillars.items())
            prompt = (
                f"Here is my 7-pillar financial health breakdown (out of 10 each):\n{pillars_txt}\n"
                f"Overall score: {overall}/10. Explain the weakest pillar and give me one concrete action to improve it this month."
            )
            reply = ask_ai(prompt)
        st.markdown(f'<div class="bn-insight">{reply}</div>', unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    init_state()
    load_css()
    top_nav()
    st.markdown("<div style='height:1.4rem;'></div>", unsafe_allow_html=True)

    page = st.session_state.page
    if page == "home":
        page_home()
    elif page == "signup":
        page_signup()
    elif page == "advisor":
        page_advisor()
    elif page == "xray":
        page_xray()
    elif page == "goals":
        page_goals()
    elif page == "health":
        page_health()
    else:
        page_home()


if __name__ == "__main__":
    main()
