# 🎯 HireIQ — AI-Powered Resume Screening & Candidate Ranking System
### FUTURE_ML_03 | NLP + Cosine Similarity + Weighted Scoring | HR-Tech Internship Project

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://python.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3-orange)](https://scikit-learn.org)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen)]()
[![License](https://img.shields.io/badge/License-MIT-lightgrey)]()

> **An end-to-end NLP screening system that reads resumes, compares them to a job description, scores candidates across four dimensions, and produces a ranked shortlist with matched/missing skills — turning 3–5 days of manual screening into a 2-second automated result.**

---

## 📌 Business Scenario

**Company:** NovaTech Analytics — a 200-person SaaS analytics company  
**Role:** Data Analyst (Business Intelligence Team)  
**Challenge:** The recruiting team receives 200+ applications per open role. Manual screening is inconsistent (different reviewers weight skills differently), slow (3–5 days to produce a shortlist), and costly (~40 recruiter-hours per role).  
**Solution:** HireIQ processes all resumes in under 2 seconds, applies a consistent, documented scoring formula, and outputs a ranked table with skill gap analysis for every candidate.

---

## 🗂️ Repository Structure

```
FUTURE_ML_03/
│
├── 📂 dataset/
│   ├── resumes.csv                      # 20 candidate resumes
│   ├── job_description.txt              # Target job description
│   └── README.md                        # Kaggle dataset instructions
│
├── 📂 notebook/
│   └── resume_screening.ipynb           # Full executed notebook
│
├── 📂 outputs/                          # All generated files
│   ├── candidate_rankings.csv           # Full ranked table (exportable to Excel)
│   ├── 01_top10_candidates.png
│   ├── 02_score_distribution.png
│   ├── 03_common_skills.png
│   ├── 04_missing_skills.png
│   ├── 05_skill_heatmap.png             ← ⭐ most impressive chart
│   ├── 06_fit_distribution.png
│   └── 07_score_components.png
│
├── 📂 report/
│   └── business_insights.md            # Executive summary & HR recommendations
│
├── 📂 src/
│   └── screen.py                       # Standalone screening script
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Tools & Technologies

| Category | Tools |
|---|---|
| **Language** | Python 3.10+ |
| **NLP & Vectorisation** | scikit-learn TF-IDF |
| **Similarity** | Cosine Similarity (sklearn) |
| **Data** | pandas, NumPy |
| **Visualisation** | Matplotlib, Seaborn |
| **Model Saving** | CSV export, joblib |

---

## 🔤 NLP Workflow

```
Candidate Resume Text       Job Description Text
        ↓                           ↓
    Lowercase               Lowercase
    Remove noise            Remove noise
    Remove stopwords        Remove stopwords
    Tokenise                Tokenise
        ↓                           ↓
    TF-IDF Vector    ←→    TF-IDF Vector
                    ↓
           Cosine Similarity
                    +
         Weighted Skill Match
                    +
          Experience Detection
                    +
          Education Detection
                    ↓
          Composite Score (0–100)
                    ↓
           Ranked Shortlist
```

---

## 📊 Scoring Formula

```
Composite Score = (0.40 × TF-IDF Cosine Similarity)
                + (0.35 × Weighted Skill Match)
                + (0.15 × Experience Score)
                + (0.10 × Education Score)
```

| Component | Weight | Notes |
|---|---|---|
| TF-IDF Cosine Similarity | 40% | Vocabulary overlap with JD |
| Weighted Skill Match | 35% | Skills weighted by role importance |
| Experience Score | 15% | Seniority/years keywords |
| Education Score | 10% | Degree level detected |

**Skill Weights:** Python=1.5×, SQL=1.4×, Machine Learning=1.4×, Cloud=1.2×, Power BI=1.3×, Statistics=1.2×, R=0.9×

---

## 🏆 Results — Top 5 Candidates

| Rank | Candidate | Score | Matched Skills | Fit |
|---|---|---|---|---|
| 1 | Aisha Patel | 55.0% | 13/14 | 🟢 Strong Fit |
| 2 | Ryan Kim | 51.0% | 12/14 | 🟡 Good Fit |
| 3 | Carlos Rivera | 50.8% | 12/14 | 🟡 Good Fit |
| 4 | Yuki Tanaka | 47.8% | 9/14 | 🟡 Good Fit |
| 5 | Mei-Ling Zhao | 46.9% | 10/14 | 🟡 Good Fit |

**Shortlist (Strong + Good Fit):** 10 of 20 candidates → recruiter reviews 10, not 200.

---

## 🎯 Example Predictions

```
Rank #1 — Aisha Patel
🟢 Strong Fit  |  Score: 55.0%
✅ Matched: Python, SQL, Machine Learning, Power BI, Tableau, Excel,
            Statistics, Communication, Project Management, Cloud, Git, ETL, Data Visualisation
❌ Missing: R

Rank #7 — Divya Krishnamurthy
🟡 Good Fit  |  Score: 42.3%
✅ Matched: Python, SQL, Machine Learning, Statistics, Communication,
            Project Management, Git, ETL, Data Visualisation
❌ Missing: Power BI, Tableau, Excel, Cloud, R

Rank #20 — Kevin O'Brien
🔴 Weak Fit  |  Score: 19.8%
✅ Matched: SQL, Communication, Project Management, Statistics, Git
❌ Missing: Python, Machine Learning, Power BI, Tableau, Excel, Cloud, ETL, Data Visualisation, R
```

---

## 💼 Business Value

| Metric | Before HireIQ | After HireIQ |
|---|---|---|
| Time to shortlist | 3–5 days | < 2 seconds |
| Screening consistency | Varies by recruiter | 100% consistent formula |
| Skill gap visibility | Rarely documented | Every candidate, every skill |
| Scalability | ~5 roles/month | Unlimited |
| Bias risk | Varies by reviewer | Scores computed on text only |

---

## ⚖️ Fairness & Ethics

- Candidate **names are excluded from scoring** — scores are text-only
- Skill weights are **transparent and documented** — auditable by anyone
- **Human review required** before any hiring decision
- Missing skills = **development opportunity**, not automatic disqualification
- System should be **periodically audited** for demographic patterns

---

## 🚀 Deployment Options

1. **Streamlit app** — drag-and-drop PDF upload, paste JD, instant ranked table
2. **FastAPI endpoint** — `/screen` POST for ATS integration
3. **Google Sheets add-on** — non-technical recruiters use it directly in Sheets
4. **Email parser** — auto-screen resumes sent to HR inbox

---

## 🔭 Future Improvements

- PDF/DOCX parsing with `pdfplumber` / `python-docx`
- BERT sentence embeddings for semantic (not just keyword) matching
- Multi-role screening — rank one pool against several JDs simultaneously
- Skill taxonomy expansion using LinkedIn Skills API
- Recruiter feedback loop — approved hires improve the weighting model

---

## 🚀 How to Run

```bash
git clone https://github.com/yourusername/FUTURE_ML_03.git
cd FUTURE_ML_03
pip install -r requirements.txt
jupyter notebook notebook/resume_screening.ipynb

# Or run the standalone screener:
python src/screen.py
```

---

## 👤 Author

**[Your Name]**  
ML & NLP Internship Candidate  
[LinkedIn](https://linkedin.com/in/yourprofile) | [GitHub](https://github.com/yourusername)

---
*FUTURE_ML_03 | HireIQ | Internship Portfolio Project | 2025*
