import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection
engine = create_engine(
    "postgresql://airflow:airflow@airflow_postgres:5432/airflow"
)

# Read raw table
df = pd.read_sql(
    "SELECT * FROM job_postings",
    engine
)

# Remove duplicates
df = df.drop_duplicates()

# Remove rows with missing salaries
df = df.dropna(subset=["salary_min"])

# Standardize job titles
df["title"] = df["title"].str.strip().str.title()

# Create average salary column
df["avg_salary"] = (
    df["salary_min"] + df["salary_max"]
) / 2

# Save cleaned table
df.to_sql(
    "job_postings_cleaned",
    engine,
    if_exists="replace",
    index=False
)

print("Transformed jobs data successfully!")