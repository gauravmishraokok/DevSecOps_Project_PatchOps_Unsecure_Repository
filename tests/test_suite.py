import unittest
import sys
import os

# Add parent directory to path to import app and neighbors
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import app
import auth
import db_utils

class TestTargetApp(unittest.TestCase):
    def setUp(self):
        # Ensure database is initialized
        import init_db
        init_db.init()

    def test_user_endpoint_exists(self):
        # Basic smoke test for the user endpoint
        with app.app.test_client() as client:
            # We don't care about the result, just that it doesn't 500
            response = client.get('/user?id=1')
            self.assertIn(response.status_code, [200, 404])

    def test_auth_profile(self):
        # Check that auth integration works
        profile = auth.get_profile("1")
        if profile:
            self.assertEqual(profile['id'], "1")

    def test_db_connection(self):
        conn = db_utils.get_connection()
        self.assertIsNotNone(conn)
        conn.close()

if __name__ == '__main__':
    unittest.main()