from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse
from jinja2 import Environment, FileSystemLoader
from resumeparser import process_resume
from contentgenerator import match_resume_to_job_description
from xhtml2pdf import pisa
import os

TEMPLATE_DIR = "templates"
OUTPUT_DIR = "/tmp/generated"
UPLOAD_DIR = "/tmp/uploads"

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI()

def convert_html_to_pdf(source_html: str, output_path: str) -> bool:
    with open(output_path, "wb") as output_file:
        pisa_status = pisa.CreatePDF(src=source_html, dest=output_file)
    return not pisa_status.err

@app.post("/generate_resume/")
async def generate_resume(
    resume_file: UploadFile = File(...),
    job_description: str = Form(...)
):
    try:
        # Save uploaded file
        temp_path = os.path.join(UPLOAD_DIR, resume_file.filename)
        with open(temp_path, "wb") as buffer:
            buffer.write(await resume_file.read())

        # Step 1: Parse uploaded resume
        parsed_data = process_resume(temp_path)
        os.remove(temp_path)

        # Step 2: Match with job description
        match_results = match_resume_to_job_description(parsed_data, job_description)

        # Debug Print
        print("=== MATCHING RESULTS ===")
        for section, content in match_results.items():
            print(f"\n[{section}]\n{content.get('formatted_text', '')}\n")

        # Step 3: Render into HTML
        env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
        template = env.get_template("resume_template.html")
        html_content = template.render(candidate=parsed_data.get("name", "Candidate"), sections=match_results)

        # Step 4: Convert to PDF
        output_pdf_path = os.path.join(OUTPUT_DIR, f"{resume_file.filename}_resume.pdf")
        success = convert_html_to_pdf(html_content, output_pdf_path)
        if not success:
            raise HTTPException(status_code=500, detail="Failed to generate PDF.")

        return FileResponse(output_pdf_path, filename="tailored_resume.pdf", media_type="application/pdf")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating resume: {str(e)}")
    