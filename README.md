# 📚 ResearchPilot AI

> An AI-powered Multi-Agent Research Assistant that helps researchers discover, analyze, compare, and summarize research papers using Google Gemini AI.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![Gemini](https://img.shields.io/badge/Google-Gemini%202.5%20Flash-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 🚀 Overview

ResearchPilot AI is a Multi-Agent AI research assistant that automates the academic research workflow.

Instead of manually reading dozens of research papers, users simply enter a research topic and ResearchPilot AI automatically:

- Creates a research plan
- Finds relevant papers from arXiv
- Analyzes research papers
- Compares multiple papers
- Identifies research gaps
- Generates literature reviews
- Creates citations
- Exports research reports as PDF

---

# ✨ Features

## 📋 Research Planner Agent

- Generates research objectives
- Creates research questions
- Suggests keywords
- Builds a research roadmap

---

## 📄 Paper Finder Agent

- Searches papers from arXiv
- Filters relevant papers
- Displays publication details
- Direct PDF access

---

## 🧠 Paper Analyzer Agent

Automatically extracts:

- Problem Statement
- Methodology
- Key Contributions
- Strengths
- Limitations
- Future Work

---

## ⚖️ Paper Comparison Agent

Compare multiple papers based on:

- Methodology
- Results
- Contributions
- Limitations
- Future Directions

---

## 💡 Research Gap Agent

Detects:

- Research gaps
- Unexplored areas
- Future research opportunities
- Suggested research topics

---

## 📝 Literature Review Agent

Automatically generates:

- Introduction
- Related Work
- Current Research Trends
- Research Gap
- Future Directions
- Conclusion

---

## 📑 Citation Generator

Supports multiple citation formats:

- APA
- IEEE
- MLA
- BibTeX

---

## 📥 PDF Export

Generate a professional PDF report containing:

- Research Plan
- Paper Analysis
- Research Gap
- Literature Review

---

## 📊 Interactive Dashboard

Includes:

- Research Progress
- Workflow Status
- Timeline
- Charts
- Project Completion

---

# 🏗 Multi-Agent Workflow

```
User
   │
   ▼
Research Planner Agent
   │
   ▼
Paper Finder Agent
   │
   ▼
Paper Analyzer Agent
   │
   ▼
Comparison Agent
   │
   ▼
Research Gap Agent
   │
   ▼
Literature Review Agent
   │
   ▼
Citation Generator
   │
   ▼
PDF Export
```

---

# 🛠 Tech Stack

- Python
- Streamlit
- Google Gemini 2.5 Flash
- arXiv API
- Plotly
- ReportLab
- python-dotenv

---

# 📂 Project Structure

```
ResearchPilot-AI/
│
├── agents/
│   ├── planner.py
│   ├── finder.py
│   ├── analyzer.py
│   ├── compare.py
│   ├── gap.py
│   ├── review.py
│
├── tools/
│   ├── arxiv_tool.py
│   ├── citation.py
│   ├── pdf_export.py
│
├── ui/
│   ├── dashboard.py
│   ├── papers.py
│   ├── analysis.py
│   ├── research.py
│   ├── components.py
│   ├── sidebar.py
│
├── app.py
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/SobiaSoomro/ResearchPilot-AI.git
```

Go into the project

```bash
cd ResearchPilot-AI
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Get your Gemini API Key from Google AI Studio.

---

# ▶ Run

```bash
streamlit run app.py
```

---

# 📸 Screenshots

- Dashboard
- Research Workspace
- Research Papers
- Paper Analysis
- Research Gap
- Literature Review

---

# 🌟 Future Improvements

- Semantic Search
- Vector Database Integration
- CrossRef DOI Support
- Research History
- AI Chat Assistant
- Zotero Integration
- Mendeley Integration

---

# 👩‍💻 Author

**Sobia Soomro**

BS Computer Science Student

GitHub:
https://github.com/SobiaSoomro

---

# 📄 License

This project is released under the MIT License.

---

⭐ If you found this project useful, consider giving it a star!