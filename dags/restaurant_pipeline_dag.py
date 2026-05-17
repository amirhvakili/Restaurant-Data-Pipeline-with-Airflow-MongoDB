from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from scripts.extract import extract_function
from scripts.transform import transform_function
from scripts.load_mongodb import load_function
from scripts.high_density_cities import high_density_cities

with DAG(
    "restaurant_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:
    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract_function
    )
    transform_task = PythonOperator(
        task_id="transform",
        python_callable=transform_function
    )
    load_task = PythonOperator(
        task_id="load",
        python_callable=load_function
    )
    high_density_cities_task = PythonOperator(
        task_id="report",
        python_callable=high_density_cities
    )

extract_task >> transform_task >> load_task >> high_density_cities_task