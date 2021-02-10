import unittest
from twitter.client.auth import CredentialsHandler


class CredentialsHandlerTestCase(unittest.TestCase):
    def setUp(self):
        self.credentials = CredentialsHandler.read_credentials_from_file(
            path="resources/credentials_template.yaml"
        )

    def test_read_credentials_from_file(self):
        """
        Check for each key if value == <key> given credentials dict.
        """
        check_constraint = {
            value == f"<{key}>" for key, value in self.credentials.items()
        }
        self.assertEqual(check_constraint, {True})


if __name__ == "__main__":
    unittest.main()