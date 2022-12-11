import unittest

from config import app


class TestConfig(unittest.TestCase):
    def test_app_config(self):
        self.assertEqual(app.config["DEBUG"], False)
        self.assertEqual(app.config["TESTING"], True)
        self.assertEqual(app.config["SQLALCHEMY_DATABASE_URI"], "sqlite:///:memory:")


if __name__ == "__main__":
    unittest.main()
