import unittest
from twitter.client.auth import CredentialsHandler


class CredentialsHandlerTestCase(unittest.TestCase):
    def setUp(self):
        self.credentials = CredentialsHandler.read_credentials_from_file(
            path="resources/credentials_template.yaml"
        )

    def test_read_credentials_from_file(self):
        assert "access_token" in self.credentials
        assert "access_token_secret" in self.credentials
        assert "consumer_key" in self.credentials
        assert "consumer_secret" in self.credentials


if __name__ == "__main__":
    unittest.main()