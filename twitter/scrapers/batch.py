from twitter import helpers
from twitter.client import TwitterClient
from typing import NoReturn, Sequence, SupportsInt, Text

__all__ = ["Search"]


class Search:
    @staticmethod
    def query(
        client: TwitterClient, hashtags: Sequence[Text], batch_size: SupportsInt = 15
    ):
        search = lambda hashtag: client.search(q=hashtag, count=batch_size)
        yield list(
            map(
                lambda tweet: tweet._json,
                helpers.flat_map(search, hashtags),
            )
        )