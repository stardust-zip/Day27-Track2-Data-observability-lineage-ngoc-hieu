from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def validate_orders_task() -> dict:
    import sys
    sys.path.append('/opt/airflow')
    
    from src.config import AIRFLOW_INPUT_FILE, SUMMARY_FILE
    from src.validation import run_lab_check

    summary = run_lab_check(
        input_path=AIRFLOW_INPUT_FILE,
        output_path=SUMMARY_FILE,
        allow_failure=False,
        skip_discord=False 
    )
    return summary

with DAG(
    dag_id="sales_data_quality_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
) as dag:
    validate_orders = PythonOperator(
        task_id="validate_orders",
        python_callable=validate_orders_task,
    )
