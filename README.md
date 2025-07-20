# Nebula9.ai

📌 **Problem Statement**  
Modern research requires fast, reliable, and fact-checked insights from vast online information.
However, manually researching a complex topic is time-consuming, prone to bias, and often lacks proper citation validation.

We need an autonomous multi-agent AI system that can:  

✅ Plan a research strategy for any complex query  
✅ Search the web & gather relevant data  
✅ Validate facts against credible sources  
✅ Generate a polished, well-structured research report with clickable references  
✅ Allow users to interactively run research via a simple web interface  

This project solves that problem by creating a Self-Correcting Multi-Agent Research Team that works like a team of virtual scientists—planning, researching, fact-checking, and compiling professional-quality reports.

---



# 🤖 Self-Correcting Multi-Agent Research Team

A **multi-agent research assistant** built with **LangChain, Gemini API, and Streamlit**, capable of:

 Breaking down a topic into **subtopics**

 Performing **web research & scraping**

 **Summarizing & validating claims**

Generating a **beautiful PDF report** with clickable links

 Providing a **Streamlit UI** for easy use  

<img width="1867" height="336" alt="image" src="https://github.com/user-attachments/assets/23b73922-16cf-418f-b95e-83d3dd0fda5f" />  

---

## 🚀 Features

* **Planner Agent** → Breaks a topic into 3–5 researchable subtopics
* **Researcher Agent** → Searches the web, scrapes top pages, and summarizes content
* **Critic Agent** → Validates and filters unreliable claims
* **Report Writer Agent** → Generates a **Markdown preview** & **styled PDF report**
* **Streamlit UI** → Enter a topic, run research, **preview report**, and **download PDF**

---

## 🖼️ Demo

<img width="1811" height="673" alt="image" src="https://github.com/user-attachments/assets/026e914c-d589-47f9-ac67-da0c1365d121" />
<img width="1179" height="833" alt="image" src="https://github.com/user-attachments/assets/c4fb0f44-2900-42a2-864e-ba78309c6b73" />



---

## 🛠️ Tech Stack

* **Python 3.9+**
* [LangChain](https://www.langchain.com/)
* [Google Gemini API](https://ai.google.dev/)
* [Streamlit](https://streamlit.io/)
* [ReportLab](https://pypi.org/project/reportlab/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for web scraping

---

## 📦 Installation

```bash
# Clone repo
[[git clone https://github.com/YOUR_USERNAME/self-correcting-research-agent.git](https://github.com/Nirbhay2410/Nebula9.ai.git)]
(https://github.com/Nirbhay2410/Nebula9.ai.git)
cd self-correcting-research-agent

# Create virtual environment
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

# Install dependencies
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

1. Get a **Google Gemini API Key** → [https://ai.google.dev](https://ai.google.dev)
2. Add it to your code:

```python
gemini_api_key = "YOUR_GEMINI_API_KEY"
```

*(You can also set it via `.env` and load with `python-dotenv`.)*

---

## ▶️ Running the Project

### ✅ 1. Command-line mode

```bash
streamlit run app.py
```

Then open **[http://localhost:8501](http://localhost:8501)**

---

## 📂 Project Structure

```
📦 self-correcting-research-agent
 ┣ 📂 agents
 ┃ ┣ planner.py         # PlannerAgent → Generates subtopics
 ┃ ┣ researcher.py      # ResearcherAgent → Web scraping + summarization
 ┃ ┣ critic.py          # CriticAgent → Validates claims
 ┃ ┣ report_writer.py   # ReportWriter → Generates Markdown & PDF
 ┣ main.py      # Orchestrates all agents
 ┣ app.py               # Streamlit UI
 ┣ requirements.txt     # Dependencies
 ┗ README.md

