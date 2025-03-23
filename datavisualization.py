import matplotlib.pyplot as plt
import seaborn as sns

def visualize_resume_relevance(job_description_skills, resume_skills):
    
    present_skills = [skill for skill in job_description_skills if skill in resume_skills]
    not_present_skills = [skill for skill in job_description_skills if skill not in resume_skills]

    
    relevance_score = len(present_skills) / len(job_description_skills) * 100

    
    skill_status = {
        'Present Skills': len(present_skills),
        'Not Present Skills': len(not_present_skills)
    }

    
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=list(skill_status.keys()), y=list(skill_status.values()), ax=ax, palette='Blues')

    
    ax.set_title('Skills Present vs Not Present in Resume', fontsize=16)
    ax.set_ylabel('Number of Skills', fontsize=12)
    ax.set_xlabel('Skill Status', fontsize=12)
    plt.tight_layout()
    plt.show()

    
    labels = ['Present Skills', 'Not Present Skills']
    sizes = [len(present_skills), len(not_present_skills)]
    colors = ['#66b3ff', '#ff9999']
    explode = (0.1, 0)  

    fig1, ax1 = plt.subplots(figsize=(8, 8))
    ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')  

    
    plt.title('Skills Relevance in Resume', fontsize=16)
    plt.show()

    
    print(f"Resume Relevance Score: {relevance_score:.2f}%")
