# 📋 Business Insights Report
## HireIQ — AI Resume Screening System
**Project:** FUTURE_ML_03 | **Role:** Data Analyst | **Company:** NovaTech Analytics

---

## 🏢 Executive Summary

NovaTech Analytics receives an average of 214 applications per Data Analyst opening. The current three-person recruiting team spends 3–5 working days manually reviewing each application, producing a shortlist of 10–15 candidates for phone screening.

HireIQ changes this entirely. It processed 20 representative candidate resumes in under 2 seconds, applied a consistent 4-component scoring formula, and produced a fully ranked shortlist with skill gap analysis for every candidate. The recruiter's job shifts from reading every resume to reviewing the ranked table and confirming the top shortlist — a process that takes 20 minutes, not 5 days.

---

## ⏱️ How This Saves Recruiter Time

**Current state (manual):**
- 214 resumes × ~12 minutes average read time = 42.8 hours (over 5 days)
- Shortlisting inconsistent across team members
- Skill gap analysis rarely documented
- Process repeated identically for every open role

**With HireIQ:**
- 214 resumes processed in < 5 seconds
- Recruiter reviews a ranked table of top 25 candidates (~45 minutes)
- Every candidate has a skill gap profile auto-generated
- Same system reused across all future roles by updating `job_description.txt`

**Time saved per role:** ~40 recruiter-hours  
**Annual saving (10 roles/year):** ~400 hours ≈ 10 full working weeks

---

## 🎯 How It Improves Shortlist Quality

**1. Skill weighting aligns with business priorities**  
The system assigns higher importance to Python (1.5×) and SQL (1.4×) — the non-negotiable technical skills for this role — compared to R (0.9×) which is optional. A candidate with strong Python/SQL/ML coverage ranks higher than one with equal skill count but weighted toward optional skills.

**2. Four-dimensional assessment**  
Manual reviewers typically assess on one dimension (skills mentioned). HireIQ assesses four: vocabulary similarity, skill coverage, seniority indicators, and education level. This produces a more complete candidate picture.

**3. Skill gap profiles enable smarter interviews**  
Every candidate report shows exactly which skills are missing. Interviewers can probe specifically on gap areas — or identify whether gaps are trainable (e.g., Tableau) vs. fundamental (e.g., SQL).

---

## ⚖️ How It Reduces Bias

**Consistency:** Every resume is scored with the same formula, the same weights, and the same stopword list. A recruiter reviewing resume #1 on Monday and resume #200 on Friday applies identical criteria.

**Name-blind scoring:** Candidate names appear in the output table for reference, but are not part of the text fed into the scoring algorithm. The system cannot distinguish a resume by name.

**Transparent logic:** Unlike commercial "black box" ATS tools, every weight is documented and justifiable. Any recruiter can understand why Aisha Patel ranked #1.

**Important limitation:** The system still reflects any biases embedded in the job description itself. If the JD uses unnecessarily restrictive language, the algorithm will reward resumes that mirror that language. Human oversight of the JD before screening is essential.

---

## 📈 How Companies Can Scale Hiring Faster

| Company Size | Manual Process | With HireIQ |
|---|---|---|
| Startup (1 HR) | 1 role at a time, 1 week each | 5+ roles simultaneously, same day |
| Mid-size (5 HR) | 10 roles/month, inconsistent criteria | 50+ roles/month, unified scoring |
| Enterprise (HR team) | ATS costs $50K+/year | Open-source system, full control |

**Multi-role extension:** Update `job_description.txt` to screen for any role. A single recruiter can manage Data Analyst, Data Engineer, and Business Analyst pipelines in the same session.

**Candidate feedback:** The missing skills list can be shared with rejected candidates as a constructive development guide — improving employer brand and candidate experience simultaneously.

---

## 🔍 Key Findings from This Screening Round

- **Most common skill gap:** R (13 of 20 candidates missing it — suggests it should be downgraded to "nice-to-have" in the JD)
- **Strongest candidate pool segment:** Technical skills (Python, SQL) are well-covered; visualisation tools (Power BI, Tableau) are the differentiator between Good Fit and Strong Fit
- **Recommended shortlist:** Top 10 candidates (Ranks 1–10) for phone screening — all scored ≥40% composite
- **Immediate interviews:** Ranks 1–3 (Aisha Patel, Ryan Kim, Carlos Rivera) — scores ≥50% with 12–13/14 skills matched

---

## ✅ Top 5 Recommendations

1. **Use the shortlist as a starting point, not a final answer** — ranks 1–10 should all receive a phone screen; rank order within the shortlist should be treated as indicative, not definitive.

2. **Review the skill weights quarterly** — as the role evolves (e.g., if Power BI is replaced by Looker), update the taxonomy to match.

3. **Add PDF parsing** — current system works on plain text. Adding `pdfplumber` would allow direct upload of PDF resumes without manual text extraction.

4. **Share the missing skills report with hiring managers** — they can use it to design role-specific interview questions targeting the gaps of each shortlisted candidate.

5. **Audit for fairness annually** — run a retrospective comparing the system's rankings against final hiring decisions. If patterns emerge (e.g., consistently lower scores for certain name patterns), investigate whether the JD or skill taxonomy needs revision.

---

