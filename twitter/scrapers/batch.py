from twitter import helpers
from twitter.client import TwitterCLI
from typing import NoReturn, Sequence, SupportsInt, Text

__all__ = ["Batch"]


class Batch:
    def __init__(self, client: TwitterCLI) -> NoReturn:
        self.client = client.api

    def query(self, hashtags: Sequence[Text], batch_size: SupportsInt = 15):
        search = lambda hashtag: self.client.search(q=hashtag, count=batch_size)
        yield list(
            map(
                lambda tweet: tweet._json,
                helpers.flat_map(search, hashtags),
            )
        )
