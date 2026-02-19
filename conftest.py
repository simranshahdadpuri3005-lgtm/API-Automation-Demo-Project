import pytest
from playwright.sync_api import sync_playwright
from utils.api_client import APIClient

# Base URL for testing (using https://dummyjson.com/))
BASE_URL = "https://dummyjson.com"

@pytest.fixture(scope="module")
def client(playwright):
    request_context = playwright.request.new_context()
    client = APIClient(BASE_URL, request_context)
    yield client
    request_context.dispose()