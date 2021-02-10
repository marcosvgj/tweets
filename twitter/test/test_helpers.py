import unittest
from twitter import helpers


class HelpersTestCase(unittest.TestCase):
    def test_flat_map(self):
        sequence = list(range(10))
        mock = map(lambda i: [i], sequence)
        applied_function = list(helpers.flat_map(lambda i: i, mock))
        self.assertEqual(applied_function, sequence)


if __name__ == "__main__":
    unittest.main()