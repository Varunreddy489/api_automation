import pytest
from utils.api_client import APIClient


@pytest.fixture
def client():
    return APIClient()


def test_single_user(client):
    response = client.get("users/2")
    assert response.status_code == 200


def test_list_users(client):
    response = client.get("users?page=2")
    assert response.status_code == 200


def test_create_users(client):
    payload={"name": "morpheus", "job": "leader"}
    response = client.post("users", data=payload)
    assert response.status_code == 201

def test_update_users(client):
    payload={"name": "morpheus", "job": "leader"}
    response = client.put("users/2", data=payload)
    assert response.status_code == 200
    
def test_update_users_patch(client):
    payload={"name": "morpheus", "job": "leader"}
    response = client.patch("users/2", data=payload)
    assert response.status_code == 200
    
def test_update_users_patch(client):
    payload={"name": "morpheus", "job": "leader"}
    response = client.patch("users/2", data=payload)
    assert response.status_code == 200
