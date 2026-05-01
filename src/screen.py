"""
screen.py — HireIQ Standalone Resume Screener
FUTURE_ML_03 | NovaTech Analytics | Data Analyst Role

Usage:
    python screen.py                          # screens dataset/resumes.csv vs dataset/job_description.txt
    python screen.py my_resumes.csv my_jd.txt # custom files
"""

import sys, re, string
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter

# ── Skill taxonomy ────────────────────────────────────────────────────────
SKILLS = {
    'Python':             {'weight': 1.5, 'keywords': ['python']},
    'SQL':                {'weight': 1.4, 'keywords': ['sql']},
    'Machine Learning':   {'weight': 1.4, 'keywords': ['machine learning','ml','scikit-learn']},
    'Power BI':           {'weight': 1.3, 'keywords': ['power bi','powerbi']},
    'Tableau':            {'weight': 1.2, 'keywords': ['tableau']},
    'Excel':              {'weight': 1.1, 'keywords': ['excel','google sheets']},
    'Statistics':         {'weight': 1.2, 'keywords': ['statistics','regression','predictive']},
    'Communication':      {'weight': 1.1, 'keywords': ['communication','presentation']},
    'Project Management': {'weight': 1.1, 'keywords': ['project management']},
    'Cloud':              {'weight': 1.2, 'keywords': ['cloud','aws','gcp','azure']},
    'Git':                {'weight': 1.1, 'keywords': ['git','github']},
    'ETL':                {'weight': 1.1, 'keywords': ['etl','pipeline','wrangling','data cleaning']},
    'Data Visualisation': {'weight': 1.1, 'keywords': ['visualization','dashboard','reporting']},
    'R':                  {'weight': 0.9, 'keywords': [' r ','r programming']},
}

STOPWORDS = set(['i','me','my','we','our','you','your','he','him','his','she','her',
'it','its','they','them','their','this','that','these','those','am','is','are','was',
'were','be','been','have','has','had','do','does','did','a','an','the','and','but',
'if','or','as','of','at','by','for','with','about','to','from','in','on','not','no',
'so','than','too','very','can','will','just','should','now','also','such','more',
'most','other','some','any','all','both'])

EXP_KW  = ['years experience','year experience','senior','lead','phd','master','bachelor']
EDU_KW  = {'phd': 4, 'master': 3, 'bachelor': 2, 'degree': 1}

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|\S+@\S+|\d+', ' ', text)
    text = text.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))
    return ' '.join(t for t in text.split() if t not in STOPWORDS and len(t) > 1)

def extract_skills(text):
    t = text.lower()
    found   = [s for s, m in SKILLS.items() if any(kw in t for kw in m['keywords'])]
    missing = [s for s in SKILLS if s not in found]
    return found, missing

def exp_score(text):
    return min(sum(1 for kw in EXP_KW if kw in text.lower()) / 3, 1.0)

def edu_score(text):
    return max((pts for kw, pts in EDU_KW.items() if kw in text.lower()), default=0) / 4

def screen(resumes_path: str, jd_path: str):
    df = pd.read_csv(resumes_path)
    with open(jd_path) as f:
        jd_raw = f.read()

    df['clean']  = df['resume_text'].apply(clean_text)
    jd_clean     = clean_text(jd_raw)
    corpus       = list(df['clean']) + [jd_clean]

    tfidf        = TfidfVectorizer(max_features=3000, ngram_range=(1,2), sublinear_tf=True)
    matrix       = tfidf.fit_transform(corpus)
    cos_scores   = cosine_similarity(matrix[:-1], matrix[-1]).flatten()
    max_wt       = sum(m['weight'] for m in SKILLS.values())

    results = []
    for i, row in df.iterrows():
        found, miss = extract_skills(row['resume_text'])
        skill_pct   = sum(SKILLS[s]['weight'] for s in found) / max_wt
        composite   = round((0.40*cos_scores[i] + 0.35*skill_pct +
                             0.15*exp_score(row['resume_text']) +
                             0.10*edu_score(row['resume_text'])) * 100, 1)
        fit = 'Strong Fit' if composite>=55 else 'Good Fit' if composite>=40 else 'Weak Fit'
        results.append({'Candidate': row['candidate_name'], 'Score': composite,
                        'Fit': fit, 'Matched': ', '.join(found), 'Missing': ', '.join(miss)})

    rdf = pd.DataFrame(results).sort_values('Score', ascending=False).reset_index(drop=True)
    rdf['Rank'] = rdf.index + 1

    print(f"\n{'='*70}")
    print(f"  🎯 HireIQ — Screening Complete")
    print(f"  {len(df)} candidates evaluated against: {jd_path}")
    print(f"{'='*70}")
    for _, row in rdf.iterrows():
        icon = '🟢' if row['Fit']=='Strong Fit' else '🟡' if row['Fit']=='Good Fit' else '🔴'
        print(f"\n  #{row['Rank']:>2}  {row['Candidate']}")
        print(f"  {icon} {row['Fit']}  |  {row['Score']}%")
        print(f"  ✅ {row['Matched'] or 'None'}")
        print(f"  ❌ {row['Missing'] or 'None'}")
    print(f"\n{'='*70}")

    out = resumes_path.replace('.csv', '_rankings.csv')
    rdf.to_csv(out, index=False)
    print(f"\n  Rankings saved to: {out}\n")

if __name__ == '__main__':
    res = sys.argv[1] if len(sys.argv) > 1 else '../dataset/resumes.csv'
    jd  = sys.argv[2] if len(sys.argv) > 2 else '../dataset/job_description.txt'
    screen(res, jd)
