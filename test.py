test_resume_json = {
    "summary": "Experienced software engineer with a focus on backend development using Python and Django. Skilled in REST APIs and cloud deployment.",
    "experience": "Software Engineer at TechCorp (2020–Present): Built scalable REST APIs using Django and Flask. Deployed services to AWS. Collaborated with frontend team using React.",
    "education": "B.Sc. in Computer Science from University of XYZ, graduated in 2018.",
    "skills": "Python, Django, Flask, AWS, REST APIs, Git, SQL"
}

test_job_description = """
We are looking for a backend software engineer proficient in Python and Django. Experience with cloud platforms such as AWS is a plus.
The candidate should have strong knowledge of RESTful API development and version control using Git.
"""

from contentgenerator import match_resume_to_job_description

# Run the test
matched = match_resume_to_job_description(test_resume_json, test_job_description)

# Optional: Print the structured response
import json
print(json.dumps(matched, indent=2))