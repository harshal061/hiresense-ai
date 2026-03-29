import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
def analyze_resume(text, job_role="Data Analyst"):

    prompt = f"""
    You are an AI recruiter.

    Return ONLY valid JSON. Do not add explanation, notes, or markdown.

    Format strictly:

    {{
        "skills": [],
        "experience_summary": "",
        "match_score": 0,
        "missing_skills": [],
        "recommendation": ""
    }}

    Resume:
    {text}
    """
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content