import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def headers():
    return {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }