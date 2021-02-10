import os
import time
import logging
import psycopg2
from typing import Text
from werkzeug.contrib.cache import FileSystemCache

logger = logging.getLogger()


class PostgresConnector:
def __init__(
        self,
        postgres_user: Text = "postgres",
        postgres_password: Text = "postgres",
        postgres_host: Text = "postgres",
        postgres_port: Text = "5432",
        postgres_db: Text = "postgres",
    ):
        self.postgres_user = postgres_user
        self.postgres_password = postgres_password
        self.postgres_host = postgres_host
        self.postgres_port = postgres_port
        self.postgres_db = postgres_db

        self.conn = psycopg2.connect(
            host=self.postgres_host,
            database=self.postgres_db,
            user=self.postgres_user,
            password=self.postgres_password,
        )

    @property
    def sql_alchemy_database_uri(self) -> Text:
        return f"postgresql+psycopg2://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"

    def connection_established(self, max_retries=3, default_sleep_time=120) -> bool:
        retries = 0
        connection_established = False
        while not connection_established and retries <= max_retries:
            try:
                cur = self.conn.cursor()
                cur.execute("SELECT version();")
                connection_established = True
                break
            except Exception as error:
                logger.error(
                    f"No connection avaiable yet. Waiting for {default_sleep_time} seconds. Details: {error}"
                )
                time.sleep(default_sleep_time)
                retries += 1
        if not connection_established and retries >= max_retries:
            raise Exception("Something wrong happens. Try again later. ")
        return connection_established


conn = PostgresConnector()
SQLALCHEMY_DATABASE_URI = conn.sql_alchemy_database_uri
conn.connection_established()
