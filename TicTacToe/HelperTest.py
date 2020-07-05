import unittest
from Helper import Helper

class HelperTest(unittest.TestCase):
    def test_read_json(self):
        config = Helper().readConfig("config.json")
        # Assert that we are able to read a nested value
        self.assertEqual("Do you want to play the game??",config["messages"]["wantToPlay"])