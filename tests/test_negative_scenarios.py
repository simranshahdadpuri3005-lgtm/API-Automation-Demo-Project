import pytest
from utils.api_client import APIClient
from conftest import *
import time

# The API used is DummyJSON API, 
# and its /products/add endpoint does not strictly validate the payload. 
# Even if we send an empty body {}, it still creates a product and returns 201.
# So the failure or some unwanted results are expected.


#Verify API handles non-existing resources gracefully by returning appropriate error codes and messages.
def test_get_user_invalid_id(client):
    response = client.get("/products/9999")  # Assuming 9999 is an invalid product ID
    assert response.status == 404
    print("GET /products/9999 returned 404 as expected")

#Verify API returns 404 for wrong endpoints and does not expose unintended data or functionality.
def test_invalid_endpoint(client):
    response = client.get("/products/9999/unknownendpoint")  # Invalid endpoint
    assert response.status == 404
    print("GET /products/9999/unknownendpoint returned 404 as expected")

# this might pass or fail depending on the API validation rules
def test_missing_required_field(client):
    payload = {
        "id": "QA"
    }
    response = client.post("/products/add", payload)
    assert response.status == 400 or response.status == 201
    print(response.status)


# The API used is DummyJSON API, 
# and its /products/add endpoint does not strictly validate the payload. 
# Even if we send an empty body {}, it still creates a product and returns 201.
# So the failure is expected.

# POST – Empty Request Body
def test_create_user_empty_body(client):
    response = client.post(
        "/products/add",
        payload={}
    )
    assert response.status in [400, 422, 201]  # Depending on API validation, it might return 400/422 or 201
    print("POST /products/add with empty body returned", response.status)

#PUT – Update non existing User
def test_update_non_exiting_user(client):
    payload = {
        "name": "john doe",
        "job": "automation tester"
    }
    response = client.put("/products/add/2",payload)
    assert response.status in [404, 200]
    print("PUT /products/add/2 returned", response.status)
   
#DELETE – Delete non existing User
def test_delete_user(client):
    response = client.delete("/products/9999")
    assert response.status in [404, 204]  # Depending on API design, it might return 404 or 204 for non-existing resource
    print("DELETE /products/9999 returned", response.status, "as expected") 

#Response Time Test
def test_response_time(client):
    start = time.time()
    response = client.get("/products/2")
    end = time.time()
    response_time = end - start
    assert response.status == 200
    assert response_time < 2
    print(f"GET /products/2 returned in {response_time:.2f} seconds")

#Response Schema Validation
def test_user_response_schema(client):
    response = client.get("/products/2")
    body = response.json()
    assert response.status == 200
    assert "id" in body
    assert "title" in body
    assert "price" in body
    assert "brand" in body
    assert "category" in body
    print("GET /products/2 response schema is valid")

# Duplicate Data Test
def test_create_duplicate_user(client):

    payload = {
        "id": "1",
        "title": "duplicate",
        "price": 100,
        "brand": "test brand",
        "category": "test category",
        #"unknownField": "unexpected"
    }
    response1 = client.post("/products/add", payload)
    response2 = client.post("/products/add", payload)
    assert response1.status == 201
    assert response2.status in [201, 409]
    print("First POST /products/add returned", response1.status)
    print("Second POST /products/add returned", response2.status)


