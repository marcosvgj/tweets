from twitter.client import TwitterCLI
from typing import NoReturn, SupportsInt

# https://www.geeksforgeeks.org/extracting-tweets-containing-a-particular-hashtag-using-python/

__all__ = ["Streaming"]


class Streaming:
    def __init__(self, client: TwitterCLI) -> NoReturn:
        self.client = client.api