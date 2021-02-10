import unittest
from twitter.client import TwitterCLI
from twitter.client.auth import CredentialsHandler


class TwitterCliTestCase(unittest.TestCase):
    def setUp(self):
        self.credentials = CredentialsHandler.read_credentials_from_file(
            path="resources/credentials_template.yaml"
        )
        self.client = TwitterCLI(**self.credentials)

    def test_instance_of_client(self):
        self.assertIsInstance(self.client, TwitterCLI)

    def test_singleton_twitter_cli(self):
        foo_client = TwitterCLI(**self.credentials)
        self.assertEqual(self.client, foo_client)


if __name__ == "__main__":
    unittest.main()