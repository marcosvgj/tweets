from datetime import timedelta, datetime
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
from pyspark.sql import SparkSession
from twitter.client import TwitterClient
from twitter.client.auth import CredentialsHandler
from twitter.scrapers.batch import Search


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
    sc = (
        SparkSession.builder.master("local[*]")
        .appName("pipeline_batch_example")
        .getOrCreate()
    )
    spark = sc.get_session()
    twd_credentials = CredentialsHandler.read_credentials_from_file()
    client = TwitterClient(**twd_credentials)
    data = Search.query(client=client, hashtags=["COVID19"])

    spark.createDataFrame(data).write.mode("append").option(
        "path", "hdfs://hdfs:9000/tweets/covid"
    ).format("parquet").saveAsTable("covid_tweets")


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