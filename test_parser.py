from parser import extract_text
with open("sample_resume.pdf","rb") as f:
    text = extract_text(f)
print(text[:5000])# shows the exact text from the pdf of sample_resume.pdf