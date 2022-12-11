import unittest

from models import User


class TestUserModel(unittest.TestCase):
    def setUp(self):
        self.user = User(name="John Doe", email="john@example.com")

    def test_user_name(self):
        self.assertEqual(self.user.name, "John Doe")

    def test_user_email(self):
        self.assertEqual(self.user.email, "john@example.com")


if __name__ == "__main__":
    unittest.main()
