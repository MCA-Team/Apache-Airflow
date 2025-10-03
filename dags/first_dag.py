from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


with DAG(
    dag_id = "DAG_v1",
    description = "Test dag",
    start_date = datetime(2025, 10, 3, 14),
    schedule = "@daily"
) as dag:
    task1 = BashOperator(
        task_id = "task1",
        bash_command = "echo 'hello it's task 1'"
    )

    task2 = BashOperator(
        task_id = "task2",
        bash_command = "echo 'hello it's task 2'"
    )

    task3 = BashOperator(
        task_id = "task3",
        bash_command = "echo 'hello it's task 3'"
    )

    task1 >> [task2, task3]