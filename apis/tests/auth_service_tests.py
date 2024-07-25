import unittest
import requests
from rest_framework import status
import logging

class AuthServiceTests(unittest.TestCase):

    def setUp(self):
        self.token_url = 'http://0.0.0.0:8000/v1/auth/token/'
        self.validation_url = 'http://0.0.0.0:8000/v1/auth/token/validate/'
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.DEBUG)

    def test_token_generation(self):
        response = requests.post(self.token_url, json={
            'client_id': 'your_client_id',
            'client_secret': 'your_client_secret'
        })
        if response.status_code != status.HTTP_200_OK:
            error_message = f"Failed to generate token: {response.status_code} - {response.content}"
            self.logger.error(error_message)
            self.fail(error_message)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access_token', response.json()['data'])

    def test_token_validation(self):
        response = requests.post(self.token_url, json={
            'client_id': 'your_client_id',
            'client_secret': 'your_client_secret'
        })
        token = response.json()['data']['access_token']
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(self.validation_url, headers=headers)
        if response.status_code != status.HTTP_200_OK:
            error_message = f"Failed to validate token: {response.status_code} - {response.content}"
            self.logger.error(error_message)
            self.fail(error_message)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.json()['data']['valid'])

if __name__ == '__main__':
    unittest.main()
