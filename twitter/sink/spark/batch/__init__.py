from twitter.client import TwitterClient
from twitter.client.auth import CredentialsHandler
from twitter.scrapers.batch import Search
from pyspark.sql import DataFrame, SparkSession
from typing import Optional, Text


class Pipeline:
    @staticmethod
    def dataset(
        spark: SparkSession,
        hashtags: list,
        batch_size: int = 1024,
    ):
        client = TwitterClient(**CredentialsHandler.read_credentials_from_file())
        data = Search.query(client=client, hashtags=hashtags, batch_size=batch_size)
        return spark.createDataFrame(data)
        