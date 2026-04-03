from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from config import GROQ_API_KEY, MODEL_NAME


def build_llm():
    return ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name=MODEL_NAME,
        max_tokens=1500,
        temperature=0.3,
    )


def analyze_resume(resume_text):
    llm = build_llm()

    template = """
You are a helpful HR assistant. Read the resume below and reply in this exact format. Do not add anything extra.

NAME: (full name or Unknown)
ROLE: (current or most recent job title)
EXPERIENCE: (total years, e.g. 2 years or Fresher)
EDUCATION: (degree and college)
SKILLS: (list skills separated by commas)
SCORE: (give a number from 0 to 100 based on resume quality)
STRENGTHS: (write 3 strengths, each on a new line starting with -)
IMPROVEMENTS: (write 2 things to improve, each on a new line starting with -)
SUMMARY: (write 2 sentences about this candidate)

Resume:
{resume}
"""

    prompt = PromptTemplate(input_variables=["resume"], template=template)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(resume=resume_text)


def match_with_job(resume_text, job_text):
    llm = build_llm()

    template = """
You are a recruiter comparing a resume to a job description. Reply in this exact format only.

MATCH_SCORE: (number from 0 to 100)
FIT: (one of: Strong Fit / Average Fit / Weak Fit)
DECISION: (one of: Shortlist / Consider / Reject)
MATCHED_SKILLS: (skills from resume that match the job, comma separated)
MISSING_SKILLS: (important skills in job not found in resume, comma separated)
TIPS: (3 tips to improve the resume for this job, each on a new line starting with -)
QUESTIONS: (3 interview questions for this candidate, each on a new line starting with -)

Resume:
{resume}

Job Description:
{job}
"""

    prompt = PromptTemplate(input_variables=["resume", "job"], template=template)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(resume=resume_text, job=job_text)


def write_cover_letter(resume_text, job_text, company):
    llm = build_llm()

    template = """
Write a short, professional cover letter for the candidate below applying to {company}.
Use the resume and job description. Keep it under 220 words. Sound human and confident. No placeholders.

Resume:
{resume}

Job Description:
{job}
"""

    prompt = PromptTemplate(input_variables=["resume", "job", "company"], template=template)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(resume=resume_text, job=job_text, company=company)
