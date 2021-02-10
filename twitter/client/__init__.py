from tweepy import API, OAuthHandler
from typing import Text, NoReturn
from twitter.helpers import Singleton


__all__ = ["TwitterCLI"]


class TwitterCLI(metaclass=Singleton):
    """
    Interface of OAuth 1a (application-user) authentication method from Tweetpy SDK. This client is used with Singleton pattern.
    """

    def __init__(
        self,
        access_token: Text,
        access_token_secret: Text,
        consumer_key: Text,
        consumer_secret: Text,
    ):
        """
        Args:
            access_token (str): Access token provided by Twitter Developer Portal.
            access_token_secret (str): access token Secret provided by Twitter Developer Portal.
            consumer_key (str): Consumer key provided by Twitter Developer Portal.
            consumer_secret (str): Consumer secret provided by Twitter Developer Portal.
        For more information about authentication at Twitter Developer, check: https://developer.twitter.com/en/docs/authentication/overview.
        """
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
