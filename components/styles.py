DARK_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Syne:wght@400;600;800&display=swap');

*, html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
    box-sizing: border-box;
}

.stApp {
    background: #0d0d0f;
    color: #e2e2e2;
}

section[data-testid="stSidebar"] {
    background: #111114;
    border-right: 1px solid #1f1f27;
}

section[data-testid="stSidebar"] * {
    color: #c9c9d4 !important;
}

.stRadio label {
    color: #c9c9d4 !important;
    font-size: 14px;
}

.stButton > button {
    background: #18181f;
    color: #a78bfa;
    border: 1px solid #a78bfa;
    border-radius: 6px;
    padding: 0.55rem 1.6rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.03em;
    transition: all 0.18s ease;
    cursor: pointer;
}

.stButton > button:hover {
    background: #a78bfa;
    color: #0d0d0f;
    border-color: #a78bfa;
}

.stTextArea textarea, .stTextInput input {
    background: #18181f !important;
    color: #e2e2e2 !important;
    border: 1px solid #2a2a35 !important;
    border-radius: 6px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 13px !important;
}

.stTextArea textarea:focus, .stTextInput input:focus {
    border-color: #a78bfa !important;
    box-shadow: 0 0 0 2px rgba(167,139,250,0.12) !important;
}

.stFileUploader {
    background: #18181f;
    border: 1px dashed #2a2a35;
    border-radius: 8px;
    padding: 0.5rem;
}

.stExpander {
    background: #18181f !important;
    border: 1px solid #1f1f27 !important;
    border-radius: 8px !important;
}

.stSuccess {
    background: #0f1f18 !important;
    border-left: 3px solid #34d399 !important;
    color: #34d399 !important;
}

.stWarning {
    background: #1f1800 !important;
    border-left: 3px solid #fbbf24 !important;
    color: #fbbf24 !important;
}

.stInfo {
    background: #111827 !important;
    border-left: 3px solid #60a5fa !important;
    color: #93c5fd !important;
}

.stMetric {
    background: #18181f;
    border: 1px solid #1f1f27;
    border-radius: 8px;
    padding: 1rem;
}

.stMetric label {
    color: #6b6b80 !important;
    font-size: 11px !important;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

.stMetric [data-testid="metric-container"] > div:last-child {
    color: #e2e2e2 !important;
    font-size: 18px !important;
    font-weight: 600;
}

.hero {
    background: linear-gradient(135deg, #18181f 0%, #1a1025 100%);
    border: 1px solid #2a2a35;
    border-radius: 12px;
    padding: 2.2rem 2.4rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
}

.hero::before {
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 180px; height: 180px;
    background: radial-gradient(circle, rgba(167,139,250,0.08) 0%, transparent 70%);
    border-radius: 50%;
}

.hero h1 {
    font-family: 'Syne', sans-serif;
    font-size: 1.9rem;
    font-weight: 800;
    color: #ffffff;
    margin: 0 0 0.4rem;
    letter-spacing: -0.02em;
}

.hero p {
    color: #7070a0;
    font-size: 14px;
    margin: 0;
    font-family: 'JetBrains Mono', monospace;
}

.hero .tag {
    display: inline-block;
    background: rgba(167,139,250,0.12);
    color: #a78bfa;
    border: 1px solid rgba(167,139,250,0.25);
    border-radius: 4px;
    padding: 2px 10px;
    font-size: 11px;
    font-family: 'JetBrains Mono', monospace;
    margin-bottom: 1rem;
    letter-spacing: 0.06em;
}

.card {
    background: #18181f;
    border: 1px solid #1f1f27;
    border-radius: 10px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 1rem;
}

.card-title {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #6b6b80;
    margin-bottom: 0.8rem;
    font-family: 'JetBrains Mono', monospace;
}

.skill-chip {
    display: inline-block;
    background: rgba(167,139,250,0.1);
    color: #c4b5fd;
    border: 1px solid rgba(167,139,250,0.2);
    border-radius: 4px;
    padding: 3px 10px;
    font-size: 12px;
    margin: 3px;
    font-family: 'JetBrains Mono', monospace;
}

.skill-chip.missing {
    background: rgba(248,113,113,0.1);
    color: #fca5a5;
    border-color: rgba(248,113,113,0.2);
}

.skill-chip.matched {
    background: rgba(52,211,153,0.1);
    color: #6ee7b7;
    border-color: rgba(52,211,153,0.2);
}

.bullet-item {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    padding: 8px 0;
    border-bottom: 1px solid #1a1a22;
    color: #c9c9d4;
    font-size: 14px;
}

.bullet-item:last-child { border-bottom: none; }

.dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #a78bfa;
    margin-top: 6px;
    flex-shrink: 0;
}

.dot.green { background: #34d399; }
.dot.red { background: #f87171; }
.dot.yellow { background: #fbbf24; }

.badge {
    display: inline-block;
    border-radius: 4px;
    padding: 4px 14px;
    font-size: 13px;
    font-weight: 600;
    font-family: 'JetBrains Mono', monospace;
}

.badge-green { background: rgba(52,211,153,0.15); color: #34d399; border: 1px solid rgba(52,211,153,0.3); }
.badge-yellow { background: rgba(251,191,36,0.15); color: #fbbf24; border: 1px solid rgba(251,191,36,0.3); }
.badge-red { background: rgba(248,113,113,0.15); color: #f87171; border: 1px solid rgba(248,113,113,0.3); }

.cover-box {
    background: #18181f;
    border: 1px solid #2a2a35;
    border-left: 3px solid #a78bfa;
    border-radius: 8px;
    padding: 1.8rem 2rem;
    color: #e2e2e2;
    font-size: 14.5px;
    line-height: 1.85;
    white-space: pre-wrap;
    font-family: 'Syne', sans-serif;
}

.section-label {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #a78bfa;
    font-family: 'JetBrains Mono', monospace;
    margin-bottom: 0.6rem;
    display: block;
}

.divider {
    border: none;
    border-top: 1px solid #1f1f27;
    margin: 1.8rem 0;
}

.upload-prompt {
    background: #18181f;
    border: 1px dashed #2a2a35;
    border-radius: 10px;
    padding: 3rem 2rem;
    text-align: center;
}

.upload-prompt h3 { color: #e2e2e2; margin-bottom: 0.4rem; }
.upload-prompt p { color: #6b6b80; font-size: 13px; font-family: 'JetBrains Mono', monospace; }

.feature-card {
    background: #18181f;
    border: 1px solid #1f1f27;
    border-radius: 10px;
    padding: 1.4rem;
    text-align: center;
}

.feature-card h4 { color: #e2e2e2; margin: 0.5rem 0 0.3rem; font-size: 15px; }
.feature-card p { color: #6b6b80; font-size: 12px; margin: 0; font-family: 'JetBrains Mono', monospace; }

div[data-testid="stMarkdownContainer"] p {
    color: #c9c9d4;
}

h1, h2, h3, h4 { color: #e2e2e2 !important; }
</style>
"""
