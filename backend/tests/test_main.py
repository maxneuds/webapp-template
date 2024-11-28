import pytest
from httpx import AsyncClient
from app import app


@pytest.mark.asyncio
async def test_root():
    """
    Test the root endpoint
    """
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI MongoDB app!"}


@pytest.mark.asyncio
async def test_create_item():
    """
    Test creating an item
    """
    async with AsyncClient(app=app, base_url="http://test") as client:
        payload = {
            "name": "Test Item",
            "description": "This is a test item",
            "price": 9.99
        }
        response = await client.post("/items/", json=payload)
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["item"] == payload


@pytest.mark.asyncio
async def test_list_items():
    """
    Test listing items
    """
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/items/")
    assert response.status_code == 200
    assert "items" in response.json()
    assert isinstance(response.json()["items"], list)
