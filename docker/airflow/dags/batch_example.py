from datetime import timedelta, datetime
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
from twitter.sink.spark.batch import Pipeline

default_args = {
    "owner": "Doctor Who",
    "depends_on_past": False,
    "start_date": datetime(2021, 2, 10),
    "email": ["dev@test.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


def run():
    Pipeline.dataset(save=True, hashtags=["COVID19"], batch_size=500).write.format(
        "parquet"
    ).mode("append").option("path", "hdfs://hdfs:9000/tweets/covid").save()


dag = DAG(
    dag_id="pipeline_batch",
    default_args=default_args,
    description="Pipeline Batch - Twitter data scraper",
    schedule_interval=timedelta(minutes=15),
)


task = PythonOperator(
    dag=dag,
    task_id="pipeline_batch_example",
    python_callable=run,
    execution_timeout=None,
)