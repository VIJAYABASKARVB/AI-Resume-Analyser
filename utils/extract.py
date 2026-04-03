import pdfplumber
import io
from docx import Document


def get_resume_text(uploaded_file):
    name = uploaded_file.name.lower()

    if name.endswith(".pdf"):
        text = ""
        with pdfplumber.open(io.BytesIO(uploaded_file.read())) as pdf:
            for page in pdf.pages:
                content = page.extract_text()
                if content:
                    text += content + "\n"
        return text.strip()

    elif name.endswith(".docx"):
        doc = Document(io.BytesIO(uploaded_file.read()))
        return "\n".join([p.text for p in doc.paragraphs]).strip()

    else:
        return uploaded_file.read().decode("utf-8").strip()
