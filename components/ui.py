import streamlit as st
import plotly.graph_objects as go
from utils.parse import parse_response, get, get_score, get_list, get_bullets


def score_gauge(score, label):
    if score >= 70:
        bar_color = "#34d399"
    elif score >= 45:
        bar_color = "#fbbf24"
    else:
        bar_color = "#f87171"

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={"text": label, "font": {"size": 13, "color": "#7070a0", "family": "JetBrains Mono"}},
        number={"font": {"size": 38, "color": "#e2e2e2", "family": "Syne"}, "suffix": "/100"},
        gauge={
            "axis": {"range": [0, 100], "tickcolor": "#2a2a35", "tickfont": {"color": "#6b6b80", "size": 10}},
            "bar": {"color": bar_color, "thickness": 0.22},
            "bgcolor": "#18181f",
            "bordercolor": "#1f1f27",
            "steps": [
                {"range": [0, 100], "color": "#1a1a22"},
            ],
        }
    ))
    fig.update_layout(
        height=220,
        margin=dict(t=40, b=5, l=10, r=10),
        paper_bgcolor="#18181f",
        plot_bgcolor="#18181f",
        font={"color": "#e2e2e2"},
    )
    st.plotly_chart(fig, use_container_width=True)


def skill_chips(skills, chip_class=""):
    if not skills:
        st.markdown('<span style="color:#6b6b80;font-size:13px;">None found</span>', unsafe_allow_html=True)
        return
    html = " ".join([f'<span class="skill-chip {chip_class}">{s}</span>' for s in skills])
    st.markdown(html, unsafe_allow_html=True)


def bullet_list(items, dot_class=""):
    html = ""
    for item in items:
        html += f'<div class="bullet-item"><div class="dot {dot_class}"></div><span>{item}</span></div>'
    st.markdown(html, unsafe_allow_html=True)


def decision_badge(text):
    badge_map = {
        "Shortlist": "badge-green",
        "Consider": "badge-yellow",
        "Reject": "badge-red",
        "Strong Fit": "badge-green",
        "Average Fit": "badge-yellow",
        "Weak Fit": "badge-red",
    }
    cls = badge_map.get(text, "badge-yellow")
    st.markdown(f'<span class="badge {cls}">{text}</span>', unsafe_allow_html=True)


def render_resume_result(raw):
    data = parse_response(raw)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown('<span class="section-label">Candidate Overview</span>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Name", get(data, "NAME"))
    c2.metric("Role", get(data, "ROLE"))
    c3.metric("Experience", get(data, "EXPERIENCE"))
    c4.metric("Education", get(data, "EDUCATION"))

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    col_left, col_right = st.columns([1, 1.5])

    with col_left:
        score = get_score(data, "SCORE")
        score_gauge(score, "RESUME SCORE")

    with col_right:
        st.markdown('<span class="section-label">Summary</span>', unsafe_allow_html=True)
        summary = get(data, "SUMMARY")
        st.markdown(f'<div class="card" style="color:#c9c9d4;font-size:14px;line-height:1.7;">{summary}</div>', unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown('<span class="section-label">Skills</span>', unsafe_allow_html=True)
    skills = get_list(data, "SKILLS")
    skill_chips(skills)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    col_s, col_w = st.columns(2)

    with col_s:
        st.markdown('<span class="section-label">Strengths</span>', unsafe_allow_html=True)
        strengths_raw = get(data, "STRENGTHS")
        strengths = get_bullets(strengths_raw) or [strengths_raw]
        bullet_list(strengths, "green")

    with col_w:
        st.markdown('<span class="section-label">Areas to Improve</span>', unsafe_allow_html=True)
        improve_raw = get(data, "IMPROVEMENTS")
        improvements = get_bullets(improve_raw) or [improve_raw]
        bullet_list(improvements, "yellow")


def render_job_match_result(raw):
    data = parse_response(raw)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown('<span class="section-label">Match Results</span>', unsafe_allow_html=True)

    col_gauge, col_info = st.columns([1, 1.5])

    with col_gauge:
        score = get_score(data, "MATCH_SCORE")
        score_gauge(score, "JOB MATCH SCORE")

    with col_info:
        st.markdown('<span class="section-label">Verdict</span>', unsafe_allow_html=True)
        fit = get(data, "FIT")
        decision = get(data, "DECISION")
        decision_badge(fit)
        st.markdown("&nbsp;", unsafe_allow_html=True)
        decision_badge(decision)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    col_m, col_miss = st.columns(2)
    with col_m:
        st.markdown('<span class="section-label">Matched Skills</span>', unsafe_allow_html=True)
        skill_chips(get_list(data, "MATCHED_SKILLS"), "matched")
    with col_miss:
        st.markdown('<span class="section-label">Missing Skills</span>', unsafe_allow_html=True)
        skill_chips(get_list(data, "MISSING_SKILLS"), "missing")

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    col_t, col_q = st.columns(2)
    with col_t:
        st.markdown('<span class="section-label">Tips to Improve Resume</span>', unsafe_allow_html=True)
        tips = get_bullets(get(data, "TIPS")) or [get(data, "TIPS")]
        bullet_list(tips, "yellow")

    with col_q:
        st.markdown('<span class="section-label">Likely Interview Questions</span>', unsafe_allow_html=True)
        questions = get_bullets(get(data, "QUESTIONS")) or [get(data, "QUESTIONS")]
        bullet_list(questions)
