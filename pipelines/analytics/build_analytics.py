import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection
engine = create_engine(
    "postgresql://airflow:airflow@airflow_postgres:5432/airflow"
)

# Read cleaned jobs table
df = pd.read_sql(
    "SELECT * FROM job_postings_cleaned",
    engine
)

# Average salary by location
salary_by_location = (
    df.groupby("location")["avg_salary"]
    .mean()
    .reset_index()
)

salary_by_location.columns = [
    "location",
    "average_salary"
]

# Top job titles
top_job_titles = (
    df["title"]
    .value_counts()
    .reset_index()
)

top_job_titles.columns = [
    "job_title",
    "count"
]

# Save analytics tables
salary_by_location.to_sql(
    "salary_by_location",
    engine,
    if_exists="replace",
    index=False
)

top_job_titles.to_sql(
    "top_job_titles",
    engine,
    if_exists="replace",
    index=False
)

print("Analytics tables created successfully!")