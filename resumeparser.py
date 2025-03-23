import pdfplumber
import spacy
import json
import redis
import numpy as np
from pymongo import MongoClient
from sentence_transformers import SentenceTransformer, util

# Load NLP Models
nlp = spacy.load("en_core_web_sm")
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Section Labels (Expanded for Higher Accuracy)
SECTION_LABELS = [
    "Professional Profile", "Education", "Skills", "Experience", "Projects", "Certifications",
    "Publications", "Achievements", "Volunteer Work", "Languages", "Career Objective", "Work Experience",
    "Leadership Roles", "Interests/Hobbies", "Referees", "Key Skills", "Availability"
]

# Precompute section embeddings
section_embeddings = embedding_model.encode(SECTION_LABELS, convert_to_tensor=True)

# Redis and MongoDB clients
redis_client = redis.Redis(host="localhost", port=6379, db=0)
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client.resume_parser

def extract_text_from_pdf(pdf_path):
    """Extracts raw text from a PDF."""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
        return text
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {str(e)}")
        return ""

def process_resume(pdf_path):
    """Processes a resume, extracts structured data, and stores results in MongoDB & Redis."""

    # Check Redis Cache
    cached_result = redis_client.get(pdf_path)
    if cached_result:
        return json.loads(cached_result.decode("utf-8"))

    # Extract text
    text = extract_text_from_pdf(pdf_path)
    if not text:
        return {"error": f"Failed to extract text from {pdf_path}"}

    # Process text with NLP
    doc = nlp(text)
    structured_data = {}
    current_section = None

    # Step 1: Identify Sections and Extract Content
    lines = text.split("\n")
    for line in lines:
        stripped_line = line.strip()
        if not stripped_line:
            continue

        # Compute similarity with section headers
        sentence_embedding = embedding_model.encode(stripped_line, convert_to_tensor=True)
        similarity_scores = util.pytorch_cos_sim(sentence_embedding, section_embeddings)
        best_match_idx = np.argmax(similarity_scores.cpu().numpy())
        best_match_score = similarity_scores[0][best_match_idx].item()

        # Improved Section Detection - Dynamic Threshold
        if best_match_score > 0.7:
            current_section = SECTION_LABELS[best_match_idx]
            structured_data[current_section] = ""
        elif current_section:
            structured_data[current_section] += stripped_line + "\n"

    # Step 2: Clean and Format JSON Output
    structured_json = {k: v.strip() for k, v in structured_data.items() if v.strip()}

    # Store in MongoDB and Redis
    try:
        db.parsed_resumes.insert_one({"pdf_path": pdf_path, "data": structured_json})
        redis_client.set(pdf_path, json.dumps(structured_json), ex=3600)
    except Exception as e:
        print(f"Database error: {str(e)}")

    return structured_json

def process_multiple_resumes(pdf_files):
    """Processes multiple resumes sequentially (without multiprocessing)."""
    return [process_resume(pdf) for pdf in pdf_files]

# Example usage
if __name__ == "__main__":
    pdf_files = ["resume_juanjosecarin.pdf", "resume_sample.pdf"]
    parsed_resumes = process_multiple_resumes(pdf_files)

    for resume in parsed_resumes:
        print(json.dumps(resume, indent=2))
