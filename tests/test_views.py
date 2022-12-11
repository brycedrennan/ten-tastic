import unittest

from app import app


class TestViews(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        result = self.app.get("/")
        self.assertEqual(result.status_code, 200)

    def test_profile_status_code(self):
        result = self.app.get("/profile")
        self.assertEqual(result.status_code, 200)

    def test_top_ten_status_code(self):
        result = self.app.get("/top-ten")
        self.assertEqual(result.status_code, 200)

    def test_social_network_status_code(self):
        result = self.app.get("/social-network")
        self.assertEqual(result.status_code, 200)


if __name__ == "__main__":
    unittest.main()
