from parser import extract_text
from llm_engine import analyze_resume
from scorer import calculate_match
import json

required_skills = ["python", 
                   "sql",
                    "excel", 
                    "tableau", 
                    "data analysis",
                    "data visualization"]

with open("sample_resume.pdf", "rb") as f:
    text = extract_text(f)
    text = text[:2000]
result = analyze_resume(text)

try:
    data = json.loads(result)
except:
    print(" JSON ERROR. RAW OUTPUT!!!")
    print(result)
    exit()

llm_skills = data.get("skills",[])

final_score = calculate_match(llm_skills, required_skills,text)

print("\n=== FINAL OUTPUT ===")
print("Skills:", llm_skills)
print("Experience:", data.get("experience_summary"))
print("LLM Score:", data.get("match_score"))  # just for reference
print("Final Score:", final_score)
print("Missing Skills:", data.get("missing_skills"))
print("Recommendation:", data.get("recommendation"))
