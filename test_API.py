import pytest
import requests
from utils import api_client

def test_get_users():
    response = api_client.get_users()
    assert response.status_code == 200
    assert 'data' in response.json()
def test_get_user():
    response = api_client.get_user(2)
    assert response.status_code == 200
    assert response.json()['data']['id'] == 2
def test_create_user():
    payload = {"name": "sidda","job":"QA engineer"}
    response = api_client.create_user(payload)
    assert response.status_code == 201
    assert response.json()["data"]["name"] == "sidda"
def test_update_user():
    payload = {"name": "sidda","job":"SR QA engineer"}
    response = api_client.update_user(payload)
    assert response.status_code == 201
    assert response.json()["data"]["job"] == "SR QA engineer"

