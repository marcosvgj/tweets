from datetime import timedelta, datetime
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
from twitter.sink.spark.batch import Pipeline
from pyspark.sql import SparkSession


default_args = {
    "owner": "Doctor Who",
    "depends_on_past": False,
    "start_date": datetime(2021, 2, 11),
    "email": ["dev@test.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

def run():
    spark = SparkSession.builder.master("local[*]").appName("pipeline_batch_example").getOrCreate()
    dataset = Pipeline.dataset(spark=spark, hashtags=["COVID19"], batch_size=1000)
    dataset.write.format("parquet").mode("append").option("path", "hdfs://hadoop:9000/raw/tweets_covid").save()

dag = DAG(
    dag_id="pipeline_batch",
    default_args=default_args,
    max_active_runs=1,
    description="Pipeline Batch - Twitter data scraper",
    schedule_interval=timedelta(minutes=5),
)

task = PythonOperator(
    dag=dag,
    task_id="pipeline_batch_example",
    python_callable=run,
    execution_timeout=None,
)