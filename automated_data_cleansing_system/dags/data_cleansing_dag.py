from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from data_cleansing import fetch_data, cleanse_data, transform_data, save_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 1,
}

dag = DAG(
    'data_cleansing_dag',
    default_args=default_args,
    description='A DAG for automated data cleansing',
    schedule_interval='@daily',
)

fetch_task = PythonOperator(
    task_id='fetch_data',
    python_callable=fetch_data,
    dag=dag,
)

cleanse_task = PythonOperator(
    task_id='cleanse_data',
    python_callable=cleanse_data,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag,
)

save_task = PythonOperator(
    task_id='save_data',
    python_callable=save_data,
    dag=dag,
)

fetch_task >> cleanse_task >> transform_task >> save_task
