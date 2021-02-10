from twitter.client import TwitterClient
from twitter.client.auth import CredentialsHandler
from twitter.scrapers.batch import Search
from pyspark.sql import DataFrame


def main():
    client = TwitterClient(**CredentialsHandler.read_credentials_from_file())
    sink = "covid19"
    path = f"hdfs://hdfs:9000/tweets/{sink}"
    data = Search.query(client=client, hashtags=["COVID19"])
    spark.createDataFrame(data).write.mode("overwrite").option("path", path).format(
        "parquet"
    ).saveAsTable(sink)


if __name__ == "__main__":
    main()