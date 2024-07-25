# apis/tests/account_service_tests.py
import unittest
import requests
from rest_framework import status
import logging
import uuid

class AccountServiceTests(unittest.TestCase):

    def setUp(self):
        self.account_url = 'http://0.0.0.0:8001/v1/accounts/'
        self.token_url = 'http://0.0.0.0:8000/v1/auth/token/'
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.DEBUG)

    def authenticate(self):
        response = requests.post(self.token_url, json={
            'client_id': 'your_client_id',
            'client_secret': 'your_client_secret'
        })
        if response.status_code != status.HTTP_200_OK:
            error_message = f"URL: {self.token_url} | Failed to authenticate: {response.status_code} - {response.content}"
            self.logger.error(error_message)
            self.fail(error_message)
        token = response.json()['data']['access_token']
        self.headers = {'Authorization': f'Bearer {token}'}

    def test_create_account(self):
        self.authenticate()
        account_number = str(uuid.uuid4().int)[:10]  # Ensure a unique account number each time
        response = requests.post(self.account_url, json={
            'account_number': account_number,
            'account_holder': 'John Doe',
            'balance': 1000.0
        }, headers=self.headers)
        if response.status_code != status.HTTP_201_CREATED:
            error_message = f"URL: {self.account_url} | Failed to create account: {response.status_code} - {response.content}"
            self.logger.error(error_message)
            self.fail(error_message)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_account(self):
        self.authenticate()
        response = requests.get(self.account_url, headers=self.headers)
        if response.status_code != status.HTTP_200_OK:
            error_message = f"URL: {self.account_url} | Failed to get account: {response.status_code} - {response.content}"
            self.logger.error(error_message)
            self.fail(error_message)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

if __name__ == '__main__':
    unittest.main()
