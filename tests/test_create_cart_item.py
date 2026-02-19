import pytest
from utils.api_client import APIClient
from conftest import *

def test_create_new_cart_item(client):
    payload = {
        "userId": 1,
        "products": [
            {"id": 1, "quantity": 2},
            {"id": 2, "quantity": 1}
        ]
    }

    response = client.post("/carts/add", payload)

    assert response.status == 201
    assert "products" in response.json()