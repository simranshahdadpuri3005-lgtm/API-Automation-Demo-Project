import pytest
from utils.api_client import APIClient
from conftest import *

# Test Case 1: GET all products
def test_get_all_products(client):
    response = client.get("/products")
    assert response.status == 200
    assert len(response.json()) > 0
    print("GET /products passed successfully")
    
# Test Case 2: GET single product
def test_get_single_product(client):
    response = client.get("/products/1")
    assert response.status == 200
    data = response.json()
    assert data["id"] == 1
    print("GET /products/1 passed successfully")

# Test Case 3: POST a new product
def test_create_product(client):
    payload = {"title": "Gaming Chair", "price": "22.45", "brand": "new_brand_added"}
    response = client.post("/products/add", payload)
    assert response.status == 201
    data = response.json()
    assert data["title"] == "Gaming Chair"
    assert data["price"] == "22.45"
    assert data["brand"] == "new_brand_added"
    print("POST product added successfully")
    
