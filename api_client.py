import pytest
import requests

BASE_URL = "https://reqres.in/api"

def get_users():
    return requests.get(f"{BASE_URL}/users")
def get_user(user_id):
    return requests.get(f"{BASE_URL}/users/{user_id}")
def add(n):
    return n*n


