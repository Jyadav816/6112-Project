import unittest
from unittest import result
import requests


class BasicTests(unittest.TestCase):
    def test_request_response_logout(self):
        response = requests.get('http://127.0.0.1:5000/logout')
        if response.ok:
            return response
        self.assertEqual(response.status_code, 200)

    def test_request_response_login(self):
        response = requests.get('http://127.0.0.1:5000/login')
        if response.ok:
            return response
        self.assertEqual(response.status_code, 200)

    def test_request_response_register(self):
        response = requests.get('http://127.0.0.1:5000/register')
        if response.ok:
            return response
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()