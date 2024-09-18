from airflow import DAG
from airflow.operators.python import PythonOperator
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

# Wrappers for tasks so that they pass data between each other
def fetch_data_task(**kwargs):
    ti = kwargs['ti']
    data = fetch_data() 
    ti.xcom_push(key='raw_data', value=data) 

def cleanse_data_task(**kwargs):
    ti = kwargs['ti']
    raw_data = ti.xcom_pull(key='raw_data', task_ids='fetch_data') 
    cleaned_data = cleanse_data(raw_data) 
    ti.xcom_push(key='cleaned_data', value=cleaned_data)

def transform_data_task(**kwargs):
    ti = kwargs['ti']
    cleaned_data = ti.xcom_pull(key='cleaned_data', task_ids='cleanse_data') 
    transformed_data = transform_data(cleaned_data)
    ti.xcom_push(key='transformed_data', value=transformed_data)

def save_data_task(**kwargs):
    ti = kwargs['ti']
    transformed_data = ti.xcom_pull(key='transformed_data', task_ids='transform_data') 
    save_data(transformed_data) 

fetch_task = PythonOperator(
    task_id='fetch_data',
    python_callable=fetch_data_task,
    provide_context=True,
    dag=dag,
)

cleanse_task = PythonOperator(
    task_id='cleanse_data',
    python_callable=cleanse_data_task,
    provide_context=True,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data_task,
    provide_context=True,
    dag=dag,
)

save_task = PythonOperator(
    task_id='save_data',
    python_callable=save_data_task,
    provide_context=True,
    dag=dag,
)

fetch_task >> cleanse_task >> transform_task >> save_task
