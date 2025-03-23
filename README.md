#  Tailored Resume Generator

This project is an AI-powered tool that **analyzes your resume** and **matches it to a specific job description** to generate a **custom-tailored PDF resume**. 

Powered by:
- **FastAPI** (Backend)
- **React.js** (Frontend)
- **Python NLP/LLM Tools** (SpaCy, Transformers, Sentence Transformers)
- **xhtml2pdf + Jinja2** (for PDF rendering)

---

##  Features

-  Upload a resume (PDF format).
-  Paste a job description.
-  AI filters relevant experience, skills, education.
-  Outputs a **tailored resume PDF**.
-  View resume instantly in-browser (PDF preview).

---

##  Folder Structure

```
tailoredresume/
│
├── app.py                      # FastAPI backend
├── resumeparser.py            # Resume extraction logic
├── contentgenerator.py        # Matching algorithm using AI/LLMs
├── templates/
│   └── resume_template.html   # Jinja2 template for PDF
├── /frontend                  # React frontend
└── /uploads & /generated      # Temp files
```

---

## ⚙️Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/Mohnish8717/Resume_Relavance_checker.git
cd Resume_Relavance_checker
```

---

### 2.  Backend Setup (FastAPI)

**Create virtual environment and install:**

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt
```

**Start the FastAPI server:**

```bash
uvicorn app:app --reload
```

---

### 3.  Frontend Setup (React)

```bash
cd frontend
npm install
npm run dev
```

Make sure your `frontend/package.json` has this line for proxying requests:

```json
"proxy": "http://localhost:8000"
```

---

##  AI/ML Technologies Used

- `spaCy`, `nltk`, `transformers`, `sentence-transformers`
- Embedding + cosine similarity
- OpenAI / DeepSeek / LLaMA (LLM model support)
- PDF generation with `xhtml2pdf`

---

##  Example Flow

1. **Upload** your raw resume.
2. **Paste** the job description.
3. AI extracts and rewrites only relevant info.
4. PDF gets auto-generated and **shown in-browser**.
5. **Download** the optimized resume!

---

##  Future Improvements

-  Save resume history
-  Customize design templates
-  Host on cloud (e.g., Vercel + Render)

---

##  Author

**Mohnish**  
 [LinkedIn](https://www.linkedin.com/in/your-link)  
 [GitHub](https://github.com/Mohnish8717)

---

##  License

MIT License – free to use and modify.
