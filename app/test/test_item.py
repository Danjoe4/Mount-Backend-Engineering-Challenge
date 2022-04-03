""" My first time using pytest. I decided not to mirror the main directory structure and instead made single test file to test the api endpoints, not the model or service layer in isolation.
"""

import pytest
import requests

TESTING_URL = 'http://127.0.0.1:5000'


class TestPostItem:
    def test_authorization(self):
        r = requests.post(f'{TESTING_URL}/item/', params={'name': 'mango', 'price': '2.00'}, headers={'authorization': 'Bearer waylongerthantwentycharacters'})
        assert r.status_code == 401
    def test_name_parameter(self):
        r = requests.post(f'{TESTING_URL}/item/', params={'na': 'mango', 'price': '2.00'}, headers={'authorization': 'Bearer twentycharacterslong'})
        assert r.status_code == 400
    def test_price_parameter(self):
        r = requests.post(f'{TESTING_URL}/item/', params={'name': 'mango', 'pr': '2.00'}, headers={'authorization': 'Bearer twentycharacterslong'})
        assert r.status_code == 400
    def test_successful_item_creation(self):
        r = requests.post(f'{TESTING_URL}/item/', params={'name': 'mango', 'price': '2.00'}, headers={'authorization': 'Bearer twentycharacterslong'})
        assert r.status_code == 201
    def test_failed_item_creation(self):
        r = requests.post(f'{TESTING_URL}/item/', params={'name': 'mango', 'price': '10.00'}, headers={'authorization': 'Bearer twentycharacterslong'})
        assert r.status_code == 409


class TestGetItem:
    def test_authorization(self):
        r = requests.get(f'{TESTING_URL}/item/', params={'name': 'mango'}, headers={'authorization': 'Bearer waylongerthantwentycharacters'})
        assert r.status_code == 401
    def test_name_parameter(self):
        r = requests.get(f'{TESTING_URL}/item/', params={'na': 'mango'}, headers={'authorization': 'Bearer twentycharacterslong'})
        assert r.status_code == 400
    def test_successful_item_retrieval(self):
        r = requests.get(f'{TESTING_URL}/item/', params={'name': 'mango'}, headers={'authorization': 'Bearer twentycharacterslong'})
        assert r.status_code == 200
    def test_failed_item_retrieval(self):
        r = requests.get(f'{TESTING_URL}/item/', params={'name': 'itemthatdoesntexist'}, headers={'authorization': 'Bearer twentycharacterslong'})
        assert r.status_code == 204


class TestDeleteItem:
    def test_authorization(self):
        r = requests.delete(f'{TESTING_URL}/item/', params={'name': 'mango'}, headers={'authorization': 'Bearer waylongerthantwentycharacters'})
        assert r.status_code == 401
    def test_name_parameter(self):
        r = requests.delete(f'{TESTING_URL}/item/', params={'na': 'mango'}, headers={'authorization': 'Bearer twentycharacterslong'})
        assert r.status_code == 400
    def test_successful_item_deletion(self):
        r = requests.delete(f'{TESTING_URL}/item/', params={'name': 'mango'}, headers={'authorization': 'Bearer twentycharacterslong'})
        assert r.status_code == 204
    def test_failed_item_deletion(self):
        r = requests.delete(f'{TESTING_URL}/item/', params={'name': 'mango'}, headers={'authorization': 'Bearer twentycharacterslong'})
        assert r.status_code == 404
