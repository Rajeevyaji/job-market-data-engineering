from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "Rajeev",
    "start_date": datetime(2026, 5, 12),
}

with DAG(
    dag_id="job_market_etl",
    default_args=default_args,
    schedule_interval=None,
    catchup=False
) as dag:

    ingest_jobs = BashOperator(
        task_id="ingest_jobs",
        bash_command="""
        cd /opt/airflow/project &&
        python pipelines/ingestion/load_real_jobs.py
        """
    )

    transform_jobs = BashOperator(
        task_id="transform_jobs",
        bash_command="""
        cd /opt/airflow/project &&
        python pipelines/transformation/transform_jobs.py
        """
    )

    build_analytics = BashOperator(
        task_id="build_analytics",
        bash_command="""
        cd /opt/airflow/project &&
        python pipelines/analytics/build_analytics.py
        """
    )

    ingest_jobs >> transform_jobs >> build_analytics