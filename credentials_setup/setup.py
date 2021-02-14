import os
import yaml

credentials_path = os.environ.get("TWEETS_CREDENTIAL_PATH")


def workflow():
    access_token = input("Twitter Developer Access Token: ")
    access_token_secret = input("Twitter Developer Access Token Secret: ")
    consumer_key = input("Twitter Developer Consumer Key: ")
    consumer_secret = input("Twitter Developer Consumer Secret: ")
    with open(credentials_path, "w") as filepath:
        data = dict(
            {
                "twitter_app": {
                    "access_token": access_token,
                    "access_token_secret": access_token_secret,
                    "consumer_key": consumer_key,
                    "consumer_secret": consumer_secret,
                }
            }
        )

        yaml.dump(data, filepath)


if __name__ == "__main__":
    workflow()
