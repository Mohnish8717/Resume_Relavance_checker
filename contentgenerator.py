import ollama
from sentence_transformers import SentenceTransformer, util
from nltk.tokenize import sent_tokenize

# Load sentence embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def clean_text(text):
    return " ".join(text.strip().split())

def process_section(section_name, section_text, job_description, use_deepseek=True):
    print(section_name,": \n\n")
    print(section_text)
    section_text = clean_text(section_text)
    job_description = clean_text(job_description)

    try:
        sentences = sent_tokenize(section_text)
    except:
        sentences = [s.strip() + "." for s in section_text.split(".") if s.strip()]

    # Cosine similarity
    job_embedding = embedding_model.encode(job_description, convert_to_tensor=True)
    scored = []
    for sent in sentences:
        score = util.pytorch_cos_sim(
            embedding_model.encode(sent, convert_to_tensor=True),
            job_embedding
        ).item()
        scored.append((sent, score))

    top_cosine = sorted(scored, key=lambda x: x[1], reverse=True)[:3]
    cosine_sentences = [s[0] for s in top_cosine]
    top_score = top_cosine[0][1] if top_cosine else 0

    # LLM prompt
    llm_prompt = fllm_prompt = f"""
You are a resume optimizer.

Given a job description and a resume section, extract only the most relevant sentences from the resume section that align with the job requirements.

Instructions:
- Only include text relevant to the section. Ignore or remove unrelated content.
- If the section is a professional summary, keep it short and impactful.
- Donot add any data that is irrelevant to job description.
     example: if the job is about data scientist donot add data regarding web development,sales.
- Remove redundancy, verbose lines, and explanations.
- Do not include code, commentary, or formatting instructions.
- Return the final result as it would appear in a polished resume — clean, concise, and professional.

Job Description:
{job_description}

Resume Section: ({section_name})
{section_text}

Return only the rewritten resume section as below :
example:
            Professional Profile 
Passionate  about  data  analysis  and  experiments,  mainly  focused  on  user  behavior,  experience,  and  engagement,  with  a  solid 
background in data science and statistics, and extensive experience using data insights to drive business growth. 
Education
2016 University of California, Berkeley Master of Information and Data Science GPA: 3.93
 
 
 
Relevant courses: 
•  Machine Learning 
•  Machine Learning at Scale 
•  Storing and Retrieving Data 
•  Field Experiments 
•  Applied Regression and Time Series 
Analysis 
•  Exploring and Analyzing Data 
•  Data Visualization and 
Communication 
•  Research Design and Applications for 
Data Analysis 
2014 Universidad Politécnica de Madrid M.S. in Statistical and Computational Information Processing GPA: 3.69
 
 
 
Relevant courses:  
•  Data Mining 
•  Multivariate Analysis 
•  Time Series 
•  Neural Networks and Statistical 
Learning 
•  Regression and Prediction Methods 
•  Optimization Techniques 
•  Monte Carlo Techniques 
•  Numerical Methods in Finance 
•  Stochastic Models in Finance 
•  Bayesian Networks
2005 Universidad Politécnica de Madrid M.S. in Telecommunication Engineering GPA: 3.03
Focus Area: Radio communication systems (radar and mobile). 
Fellowship: First year at University, due to Honors obtained last year at high school. 
Skills 
 Programming / Statistics Big Data Visualization Others 
Proficient: R, Python, SQL Hadoop, Hive, MrJob Tableau Git, AWS 
Intermediate: SPSS, SAS, Matlab Spark, Storm  Bash 
Basic: EViews, Demetra+  D3.js Gephi, Neo4j, QGIS 
Experience 
DATA SCIENCE 
Jan. 2016 – Mar. 2016 Data Scientist 
 CONENTO  Madrid, Spain (working remotely) 
•  Designed  and  implemented  the  ETL  pipeline  for  a  predictive  model  of  traffic  on  the  main  roads  in 
eastern Spain (a project for the Spanish government). 
•  Automated scripts in R to extract, transform, clean (incl. anomaly detection), and load into MySQL 
data from multiple data sources: road traffic sensors, accidents, road works, weather.
Jun. 2014 – Sep. 2014 Data Scientist  
 CONENTO Madrid, Spain 
•  Designed  an  experiment  for  Google  Spain  (conducted  in  October  2014)  to  measure  the  impact  of 
YouTube ads on the sales of a car manufacturer's dealer network. 
•  A  matched-pair,  cluster-randomized  design,  which  involved  selecting  the  test  and  control  groups 
from  a  sample  of  50+  cities  in  Spain  (where  geo-targeted  ads  were  possible)  based  on  their  sales-
wise similarity over time, using wavelets (and R). 
MANAGEMENT – SALES (Electrical Eng.) 
Feb. 2009 – Aug. 2013 Head of Sales, Spain & Portugal – Test &Measurement dept.
 YOKOGAWA Madrid, Spain 
•  Applied analysis of sales and market trends to decide the direction of the department. 
•  Led a team of 7 people.  
 
2 of 2 
Juan Jose Carin Data Scientist 
 
Mountain View, CA 94041 
 650-336-4590  |  juanjose.carin@gmail.com 
 linkedin.com/in/juanjosecarin  | juanjocarin.github.io  
•  Increased revenue by 6.3%, gross profit by 4.2%, and operating income by 146%, and achieved a 30% 
ratio of new customers (3x growth), by entering new markets and improving customer service and 
training.
SALES (Electrical Eng. & Telecom.) 
Apr. 2008 – Jan. 2009 Sales Engineer – Test & Measurement dept. 
 YOKOGAWA Madrid, Spain 
•  Promoted to head of sales after 5 months leading the sales team. 
Sep. 2004 – Mar. 2008 Sales & Application Engineer 
 AYSCOM Madrid, Spain 
•  Exceeded sales target every year from 2005 to 2007 (achieved 60% of the target in the first 3 months 
of 2008). 
EDUCATION
Jul. 2002 – Jun. 2004 Tutor of Differential & Integral Calculus, Physics, and Digital Electronic Circuits
 ACADEMIA UNIVERSITARIA Madrid, Spain 
•  Highest-rated professor in student surveys, in 4 of the 6 terms. 
•  Increased ratio of students passing the course by 25%. 
Projects  See juanjocarin.github.io for additional information
2016 SmartCam 
Capstone Python, OpenCV, TensorFlow, AWS (EC2, S3, DynamoDB) 
A scalable cloud-based video monitoring system that features motion detection, face counting, and image recognition.
2015 Implementation of the Shortest Path and PageRank algorithms with the Wikipedia graph dataset 
Machine Learning at Scale Hadoop MrJob, Python, AWS EC2, AWS S3
Using a graph dataset of almost half a million nodes. 
2015 Forest cover type prediction 
Machine Learning Python, Scikit-Learn, Matplotlib 
A Kaggle competition: predictions of the predominant kind of tree cover, from strictly cartographic variables such as elevation 
and soil type, using random forests, SVMs, kNNs, Naive Bayes, Gradient Descent, GMMs, ...
2015 Redefining the job search process 
Storing and Retrieving Data Hadoop HDFS, Hive, Spark, Python, AWS EC2, Tableau
A  pipeline  that  combines  data  from  Indeed  API  and  the  U.S.  Census  Bureau  to  select  the  best  locations  for  data  scientists 
based on the number of job postings, housing cost, etc.
2015 A fresh perspective on Citi Bike 
Data Visualization and Communication Tableau, SQLite
An interactive website to visualize NYC Citi Bike bicycle sharing service.
2015 Investigating the effect of competition on the ability to solve arithmetic problems 
Field Experiments R 
A  randomized  controlled  trial  in  which  300+  participants  were  assigned  to  a  control  group  or  one  of  two  test  groups  to 
evaluate the effect of competition (being compared to no one or someone better or worse). 
2014 Prediction of customer churn for a mobile network carrier 
Data Mining SAS
Predictions from a sample of 45,000+ customers, using tree decisions, logistic regression, and neural networks. 
2014 Different models of Harmonized Index of Consumer Prices (HICP) in Spain 
Time Series SPSS, Demetra+
Forecasts based on exponential smoothing, ARIMA, and transfer function (using petrol price as independent variable) models.

"""
    model_name = "deepseek-coder" if use_deepseek else "llama3"
    response = ollama.chat(model=model_name, messages=[{"role": "user", "content": llm_prompt}])
    llm_text = response["message"]["content"]

    # Merge and deduplicate
    cosine_set = set(s.strip() for s in cosine_sentences)
    llm_set = set(s.strip() for s in llm_text.split('.') if s.strip())
    merged = list(cosine_set) + [s for s in llm_set if s not in cosine_set]
    tailored = ". ".join(merged) + "."

    bullet_points = "\n".join(f"- {s}" for s in merged)
    formatted_text = f"{section_name.capitalize()} Highlights:\n{bullet_points}"

    return {
        "formatted_text": formatted_text
    }

def match_resume_to_job_description(resume_json, job_description, use_deepseek=True):
    """
    Applies hybrid matching to all sections of the resume.
    :param resume_json: dict of sections with text
    :param job_description: string
    :param use_deepseek: True to use DeepSeek, False to use LLaMA
    :return: dict of matched results for all sections
    """
    results = {}
    for section_name, section_text in resume_json.items():
        print(f"Processing section: {section_name}")
        result = process_section(section_name, section_text, job_description, use_deepseek)
        results[section_name] = result
        print(result["formatted_text"])
        print("=" * 60)
    return results