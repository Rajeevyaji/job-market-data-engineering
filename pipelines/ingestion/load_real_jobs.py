import pandas as pd
from sqlalchemy import create_engine

# Read CSV from raw data lake
df = pd.read_csv("data_lake/raw/ds_salaries.csv")

# Select important columns
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
    "salary_min",
    "location",
    "company"
]

# Create salary_max column
df["salary_max"] = df["salary_min"] + 20000

# PostgreSQL connection
engine = create_engine(
    "postgresql://airflow:airflow@airflow_postgres:5432/airflow"
)

# Load into PostgreSQL
df.to_sql(
    "job_postings",
    engine,
    if_exists="append",
    index=False
)

print("Real job data loaded successfully!")