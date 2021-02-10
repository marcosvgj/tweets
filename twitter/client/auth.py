import os
import logging
import pathlib
import yaml
from typing import Optional, Text, DefaultDict

__all__ = ["CredentialsHandler"]


class CredentialsHandler:
    @staticmethod
    def read_credentials_from_file(
        path="resources/credentials.yaml", key="twitter_app"
    ):
        try:
            with open(pathlib.Path(__file__).parent.parent / path) as cfg:
                return yaml.load(cfg, Loader=yaml.FullLoader).get(key)
        except Exception as error:
            logging.error(
                f"Error in load configuration file inside resources folder. Details: {error}"
            )