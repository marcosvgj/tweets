from tweepy import API, OAuthHandler
from typing import Text, NoReturn
from twitter.helpers import Singleton


__all__ = ["TwitterClient"]


class TwitterClient(metaclass=Singleton):
    def __init__(
        self,
        access_token: Text,
        access_token_secret: Text,
        consumer_key: Text,
        consumer_secret: Text,
    ):
        authorization = OAuthHandler(
            consumer_key=consumer_key, consumer_secret=consumer_secret
        )
        authorization.set_access_token(key=access_token, secret=access_token_secret)
        self.api = API(authorization)

    @property
    def api(self) -> API:
        """tweepy.api.API: Provides api interface of tweepy SDK."""
        return self.__api

    @api.setter
    def api(self, api) -> NoReturn:
        self.__api = api
