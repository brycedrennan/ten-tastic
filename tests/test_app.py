import unittest

from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home_page(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TenTastic", response.data)

    def test_profile_page(self):
        response = self.app.get("/profile")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Create Profile", response.data)

    def test_share_page(self):
        response = self.app.get("/share")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Share Top Ten", response.data)

    def test_network_page(self):
        response = self.app.get("/network")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Social Network", response.data)


if __name__ == "__main__":
    unittest.main()
