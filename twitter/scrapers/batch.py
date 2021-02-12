from twitter import helpers
from twitter.client import TwitterClient
from typing import NoReturn, Sequence, SupportsInt, Text

__all__ = ["Search"]


class Search:
    @staticmethod
    def query(
        client: TwitterClient, hashtags: Sequence[Text], batch_size: SupportsInt = 15
    ):
        search = lambda hashtag: client.api.search(q=hashtag, count=batch_size)
        return list(
            map(
                helpers.fill_na_dict,
                map(
                    lambda tweet: tweet._json,
                    helpers.flat_map(search, hashtags),
                ),
            )
        )