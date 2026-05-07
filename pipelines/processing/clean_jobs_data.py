import pandas as pd

# Read raw dataset
df = pd.read_csv("data_lake/raw/ds_salaries.csv")

print("Original rows:", len(df))

# Remove duplicates
df = df.drop_duplicates()

# Remove null job titles
df = df.dropna(subset=["job_title"])

# Keep only useful columns
df = df[
    [
        "job_title",
        "salary_in_usd",
        "employee_residence",
        "company_location"
    ]
]

# Rename columns
df.columns = [
    "title",
    "salary",
    "employee_location",
    "company_location"
]

# Filter unrealistic salaries
df = df[df["salary"] > 10000]

print("Cleaned rows:", len(df))

# Save processed dataset
df.to_csv(
    "data_lake/processed/cleaned_jobs.csv",
    index=False
)

print("Processed dataset saved successfully!")