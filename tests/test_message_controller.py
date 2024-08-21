# tests/test_message_controller.py
import unittest
from app import app

class MessageControllerTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_process_message(self):
        response = self.app.post('/process_message', json={"message": "Test message"})
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertIn("response", json_data)
        self.assertIn("audio_file", json_data)

if __name__ == "__main__":
    unittest.main()
