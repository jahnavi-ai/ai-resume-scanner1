required_skills = ['python', 'machine learning', 'data analysis', 'numpy', 'pandas']

def match_skills(resume_text):
    resume_text = resume_text.lower()
    matched = [skill for skill in required_skills if skill in resume_text]
    return int((len(matched) / len(required_skills)) * 100)
