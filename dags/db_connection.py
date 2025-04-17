from airflow import DAG
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.python import PythonOperator
from datetime import datetime

def run_query():
    hook = PostgresHook(postgres_conn_id='greenplum_conn')
    conn = hook.get_conn()
    cursor= conn.cursor()
    cursor.execute("Select * from test")
    result = cursor.fetchone()
    print(f"Количество строк: {result[0]}")

with DAG(
    dag_id = 'greenplum_example',
    start_date = datetime(2025,1,1),
    schedule_interval=None,
    catchup=False
) as dag:
    task = PythonOperator(
        task_id='count_rows_greenplum',
        python_callable=run_query
    )