import pytest
import requests
import api_client

def test_get_users():
    response = api_client.get_users()
    assert response.status_code == 200
    assert 'data' in response.json()
def test_get_user():
    response = api_client.get_user(2)
    assert response.status_code == 200
    assert response.json()['data']['id'] == 2
def test_add_math():
    assert api_client.add(2) == 4
    


