# 🚀 HireSense AI – Resume Screening System

An AI-powered resume screening system that analyzes resumes using LLMs and provides structured insights, scoring, and recommendations.

---

## 🧠 Overview

HireSense AI automates the resume evaluation process by combining:
- 🤖 LLM-based information extraction
- ⚙️ Rule-based scoring logic
- 📊 Interactive dashboard for visualization

It is designed to simulate a real-world recruitment workflow, helping identify strong candidates efficiently.

---

## ✨ Features

- 📄 **Resume Parsing** (PDF support)
- 🤖 **LLM Integration (Groq API)** for:
  - Skill extraction
  - Experience summarization
  - Recommendations
- 🎯 **Deterministic Scoring System** (custom logic)
- 📉 **Missing Skill Detection**
- 📊 **Interactive Dashboard (Streamlit)**
- 🔄 **Consistent Output (Temperature Controlled)**

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Groq API (LLaMA 3.1)**
- **Pandas**
- **Regex (for JSON parsing & cleaning)**

---

## ⚙️ How It Works

1. Upload a resume (PDF)
2. Extract text using parser
3. Send data to LLM for structured extraction
4. Apply rule-based scoring logic
5. Display results in dashboard

---

## 📊 Output Includes

- ✅ Extracted Skills  
- 🧠 Experience Summary  
- 🎯 Match Score (0–100)  
- ⚠️ Missing Skills  
- 💡 Recommendation  

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/hiresense-ai.git

# Navigate to folder
cd hiresense-ai

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py