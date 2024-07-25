# apis/tests/transaction_service_tests.py
import unittest
import requests
from rest_framework import status
import logging
import uuid

class TransactionServiceTests(unittest.TestCase):

    def setUp(self):
        self.token_url = 'http://0.0.0.0:8000/v1/auth/token/'
        self.transaction_url = 'http://0.0.0.0:8002/v1/transactions/'
        self.account_id = uuid.uuid4()
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

    def test_create_transaction(self):
        self.authenticate()

        response = requests.post(self.transaction_url, json={
            'account_id': str(self.account_id),
            'transaction_type': 'deposit',
            'amount': 100.0,
            'note': 'Test deposit'
        }, headers=self.headers)
        if response.status_code != status.HTTP_201_CREATED:  # Expecting 201 Created
            error_message = f"URL: {self.transaction_url} | Failed to create transaction: {response.status_code} - {response.content}"
            self.logger.error(error_message)
            self.fail(error_message)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Checking for 201 Created

    def test_get_transactions(self):
        self.authenticate()

        # First, create a transaction to ensure there is one to fetch
        response = requests.post(self.transaction_url, json={
            'account_id': str(self.account_id),
            'transaction_type': 'deposit',
            'amount': 100.0,
            'note': 'Test deposit'
        }, headers=self.headers)
        if response.status_code != status.HTTP_201_CREATED:  # Ensuring the transaction creation succeeds
            error_message = f"URL: {self.transaction_url} | Failed to create transaction: {response.status_code} - {response.content}"
            self.logger.error(error_message)
            self.fail(error_message)
        
        # Fetch the transactions for the account
        response = requests.get(f"{self.transaction_url}?account_id={self.account_id}", headers=self.headers)
        if response.status_code != status.HTTP_200_OK:
            error_message = f"URL: {self.transaction_url} | Failed to get transactions: {response.status_code} - {response.content}"
            self.logger.error(error_message)
            self.fail(error_message)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['data']), 1)
        self.assertEqual(response.json()['data'][0]['transaction_type'], 'deposit')

if __name__ == '__main__':
    unittest.main()
