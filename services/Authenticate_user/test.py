# для app.py аунтификация
import unittest
from unittest.mock import patch
from services.Authenticate_user.app import app, get_db, send_request


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()


    def test_register(self):
        with patch('app.get_db') as mock_get_db:
            response = self.app.post('/register', data={'username': 'testuser', 'password': 'testpass', 'number': '123456'})
            self.assertEqual(response.status_code, 500)
            # Add further assertions to ensure user is registered correctly in the database

    @patch('app.requests.get')
    def test_send_request(self, mock_requests_get):
        mock_response = mock_requests_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {'data': 'test_data'}
        response = send_request()
        self.assertEqual(response, {'data': 'test_data'})

if __name__ == '__main__':
    unittest.main()


