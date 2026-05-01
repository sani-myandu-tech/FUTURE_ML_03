# 📂 dataset/ — Dataset Instructions

## Files in this folder

| File | Description |
|---|---|
| `resumes.csv` | 20 synthetic candidate resumes (generated for this project) |
| `job_description.txt` | Data Analyst JD for NovaTech Analytics |
| `README.md` | This file |

---

## Using the Real Kaggle Resume Dataset

For a larger, real-world dataset upgrade your project with the **Resume Dataset** from Kaggle:

**URL:** https://www.kaggle.com/datasets/gauravduttakiit/resume-dataset

```bash
pip install kaggle
kaggle datasets download -d gauravduttakiit/resume-dataset
unzip resume-dataset.zip -d dataset/
```

### Adapting the real dataset to this project

```python
df = pd.read_csv('dataset/UpdatedResumeDataSet.csv')

# The real dataset has 'Resume' (full text) and 'Category' columns
df = df.rename(columns={'Resume': 'resume_text'})

# Generate candidate names (real dataset has none)
df['candidate_name'] = [f'Candidate_{i+1:03d}' for i in range(len(df))]

# Filter to a single category for focused screening
df = df[df['Category'] == 'Data Science'].copy()
df = df[['candidate_name', 'resume_text']].reset_index(drop=True)
df.to_csv('dataset/resumes.csv', index=False)
print(f"Saved {len(df)} real resumes")
```

---

## Dataset Details (Synthetic)

| Property | Value |
|---|---|
| Candidates | 20 |
| Skills tracked | 14 |
| Role screened for | Data Analyst |
| Score range | 19.8% – 55.0% |
| Shortlist (≥40%) | 10 of 20 candidates |
