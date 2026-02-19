import pytest
from utils.api_client import APIClient
from conftest import *

created_product_id = None


@pytest.mark.order(1)
def test_create_product(client):
    global created_product_id

    payload = {
            "id": 1,
            "title": "Essence Mascara Lash Princess",
            "description": "The Essence Mascara Lash Princess is a popular mascara known for its volumizing and lengthening effects. Achieve dramatic lashes with this long-lasting and cruelty-free formula.",
            "category": "beauty",
            "price": 9.99,  
    }

    response = client.post("/products/add", payload)

    #assert response.status == 200 or response.status == 201
    
    assert response.status == 201
    
    body = response.json()
    created_product_id = body["id"]

    assert body["title"] == "Essence Mascara Lash Princess"
    print(f"Created Product ID: {created_product_id}")


@pytest.mark.order(2)
def test_get_created_product(client):
    #response = client.get(f"/products/{created_product_id}")
    #its a dummy json api, so we are using a static id to get the product details instead of the created_product_id
    response = client.get(f"/products/1")
    assert response.status == 200
   # assert response.json()["title"] == created_product_id


@pytest.mark.order(3)
def test_update_product(client):
    payload = {"price": 250}

    response = client.put(f"/products/1", payload)

    assert response.status == 200
    assert response.json()["price"] == 250


@pytest.mark.order(4)
def test_delete_product(client):
    response = client.delete(f"/products/1")

    assert response.status == 200
    assert response.json()["isDeleted"] is True