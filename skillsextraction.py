import spacy


nlp = spacy.load('en_core_web_lg')

predefined_skills = [
    "Python", "R", "SQL", "TensorFlow", "PyTorch", "AWS", "Azure", "Tableau", "Machine Learning", 
    "Data Science", "Natural Language Processing", "Deep Learning", "Java", "JavaScript", "C++", 
    "Hadoop", "Spark", "Git", "Docker", "Kubernetes", "Linux", "Data Visualization"
]

def extract_skills_using_semantic_similarity(job_description):
    
    job_doc = nlp(job_description)

    
    matched_skills = []

    
    for skill in predefined_skills:
        skill_doc = nlp(skill)
        
        
        similarity = job_doc.similarity(skill_doc)

        
        if similarity > 0.6:  
            matched_skills.append(skill)
    
    return matched_skills


job_description = """
We are looking for a Data Scientist with expertise in Python, R, and machine learning frameworks like TensorFlow, PyTorch.
Knowledge of SQL databases and experience with AWS and Azure cloud services is a must. Experience with Tableau and data visualization is a plus.
"""


extracted_skills = extract_skills_using_semantic_similarity(job_description)
print("Extracted Skills:", extracted_skills)