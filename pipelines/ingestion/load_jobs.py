import pandas as pd
from sqlalchemy import create_engine

# Sample job data
data = {
    "title": [
        "Data Engineer",
        "Senior Data Engineer",
        "Python ETL Developer"
    ],
    "company": [
        "Google",
        "Amazon",
        "Netflix"
    ],
    "location": [
        "Berlin",
        "London",
        "Amsterdam"
    ],
    "salary_min": [
        70000,
        90000,
        85000
    ],
    "salary_max": [
        100000,
        130000,
        120000
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# PostgreSQL connection
engine = create_engine(
    "postgresql://postgres:password@localhost:5432/jobs_db"
)

# Load into PostgreSQL
df.to_sql(
    "job_postings",
    engine,
    if_exists="append",
    index=False
)

print("Data loaded successfully!")