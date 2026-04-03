import streamlit as st
from components.styles import DARK_CSS
from components.ui import render_resume_result, render_job_match_result
from utils.extract import get_resume_text
from utils.ai_helper import analyze_resume, match_with_job, write_cover_letter

st.set_page_config(
    page_title="ResumeAI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(DARK_CSS, unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div style="padding: 0.5rem 0 1.5rem;">
        <div style="font-family:'JetBrains Mono',monospace;font-size:11px;color:#6b6b80;letter-spacing:0.1em;margin-bottom:6px;">TOOL</div>
        <div style="font-family:'Syne',sans-serif;font-size:20px;font-weight:800;color:#ffffff;">ResumeAI ⚡</div>
        <div style="font-family:'JetBrains Mono',monospace;font-size:11px;color:#a78bfa;margin-top:4px;">Groq + LangChain</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr style="border-color:#1f1f27;margin:0 0 1.2rem;">', unsafe_allow_html=True)

    page = st.radio(
        "Navigate",
        ["Resume Analyzer", "Job Match Scorer", "Cover Letter"],
        label_visibility="collapsed",
    )

    st.markdown('<hr style="border-color:#1f1f27;margin:1.2rem 0;">', unsafe_allow_html=True)

    st.markdown("""
    <div style="font-family:'JetBrains Mono',monospace;font-size:11px;color:#6b6b80;line-height:1.9;">
        1. Upload your resume<br>
        2. Pick a tool from above<br>
        3. Get AI-powered results
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="tag">AI-POWERED · GROQ LLAMA 3.3</div>
    <h1>Resume Analyzer & Job Match Scorer</h1>
    <p>Upload your resume → get feedback, match jobs, generate cover letters.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<span class="section-label">Upload Resume</span>', unsafe_allow_html=True)
uploaded_file = st.file_uploader(
    "PDF, DOCX or TXT",
    type=["pdf", "docx", "txt"],
    label_visibility="collapsed",
)

if uploaded_file:
    st.success(f"✓ Loaded: {uploaded_file.name}")

    if st.session_state.get("file_name") != uploaded_file.name:
        with st.spinner("Reading resume..."):
            st.session_state["resume_text"] = get_resume_text(uploaded_file)
            st.session_state["file_name"] = uploaded_file.name
            st.session_state.pop("resume_result", None)
            st.session_state.pop("match_result", None)
            st.session_state.pop("cover_letter", None)

    resume_text = st.session_state["resume_text"]

    with st.expander("View extracted text"):
        st.text_area("", resume_text, height=160, label_visibility="collapsed")

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    if page == "Resume Analyzer":
        st.markdown('<span class="section-label">Resume Analyzer</span>', unsafe_allow_html=True)
        st.markdown('<p style="color:#6b6b80;font-size:13px;font-family:JetBrains Mono,monospace;margin-bottom:1rem;">Click below to get your resume scored and reviewed by AI.</p>', unsafe_allow_html=True)

        if st.button("⚡ Analyze Resume"):
            with st.spinner("Analyzing your resume..."):
                result = analyze_resume(resume_text)
                st.session_state["resume_result"] = result

        if "resume_result" in st.session_state:
            render_resume_result(st.session_state["resume_result"])

    elif page == "Job Match Scorer":
        st.markdown('<span class="section-label">Job Match Scorer</span>', unsafe_allow_html=True)
        st.markdown('<p style="color:#6b6b80;font-size:13px;font-family:JetBrains Mono,monospace;margin-bottom:1rem;">Paste the job description from LinkedIn, Naukri, or any portal.</p>', unsafe_allow_html=True)

        job_text = st.text_area(
            "Job Description",
            height=200,
            placeholder="Paste the full job description here...",
            label_visibility="collapsed",
        )

        if st.button("⚡ Check Match", key="match_btn"):
            if job_text.strip():
                with st.spinner("Comparing resume with job description..."):
                    result = match_with_job(resume_text, job_text)
                    st.session_state["match_result"] = result
            else:
                st.warning("Please paste a job description first.")

        if "match_result" in st.session_state:
            render_job_match_result(st.session_state["match_result"])

    elif page == "Cover Letter":
        st.markdown('<span class="section-label">Cover Letter Generator</span>', unsafe_allow_html=True)
        st.markdown('<p style="color:#6b6b80;font-size:13px;font-family:JetBrains Mono,monospace;margin-bottom:1rem;">Fill in the details and get a ready-to-send cover letter.</p>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            company = st.text_input("Company Name", placeholder="e.g. Zoho, Google, Infosys...")
        with col2:
            st.text_input("Job Role (optional, for context)", placeholder="e.g. Data Analyst", key="job_role_hint")

        job_for_cl = st.text_area(
            "Job Description",
            height=180,
            placeholder="Paste the job description here...",
            label_visibility="visible",
        )

        if st.button("⚡ Generate Cover Letter", key="cl_btn"):
            if company.strip() and job_for_cl.strip():
                with st.spinner("Writing your cover letter..."):
                    letter = write_cover_letter(resume_text, job_for_cl, company)
                    st.session_state["cover_letter"] = letter
            else:
                st.warning("Please enter the company name and job description.")

        if "cover_letter" in st.session_state:
            st.markdown('<hr class="divider">', unsafe_allow_html=True)
            st.markdown('<span class="section-label">Your Cover Letter</span>', unsafe_allow_html=True)
            st.markdown(
                f'<div class="cover-box">{st.session_state["cover_letter"]}</div>',
                unsafe_allow_html=True,
            )
            st.markdown("<br>", unsafe_allow_html=True)
            st.download_button(
                label="↓ Download as .txt",
                data=st.session_state["cover_letter"],
                file_name="cover_letter.txt",
                mime="text/plain",
            )

else:
    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown("""
    <div class="upload-prompt">
        <div style="font-size:2rem;margin-bottom:0.6rem;">⚡</div>
        <h3>Drop your resume to get started</h3>
        <p>Supports PDF · DOCX · TXT</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="feature-card">
            <div style="font-size:1.5rem;">📊</div>
            <h4>Resume Analyzer</h4>
            <p>Score, skills, strengths & feedback</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="feature-card">
            <div style="font-size:1.5rem;">🎯</div>
            <h4>Job Match Scorer</h4>
            <p>See how well you fit any role</p>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="feature-card">
            <div style="font-size:1.5rem;">✍️</div>
            <h4>Cover Letter</h4>
            <p>Auto-written, ready to send</p>
        </div>
        """, unsafe_allow_html=True)
