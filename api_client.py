import pytest
import requests

BASE_URL = "https://reqres.in/api"

def get_users():
    return requests.get(f"{BASE_URL}/users")
def get_user(user_id):
    return requests.get(f"{BASE_URL}/users/{user_id}")
def create_user(payload):
    return requests.post(f"{BASE_URL}/users",json=payload)
def update_user(user_id,payload):
    return requests.put(f"{BASE_URL}/users/{user_id}",json=payload)
def delete_user(user_id):
    return requests.delete(f"{BASE_URL}/users{user_id}")