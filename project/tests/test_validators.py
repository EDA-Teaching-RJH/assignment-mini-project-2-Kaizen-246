import unittest
from lablog.validators import is_valid_email

class TestValidators(unittest.TestCase):

    def test_valid_email(self):
        self.assertTrue(is_valid_email("test@email.com"))

    def test_invalid_email(self):
        self.assertFalse(is_valid_email("bademail"))

if __name__ == "__main__":
    unittest.main()