import pytest
from tests.conftest import client

def test_board(client):

    # Request on the new feature
    response = client.get("/pointsBoard")

    # Checking for a specific paragraph in the webpage.
    welcome_message = "Welcome to the points board"

    assert response.status_code == 200
    assert welcome_message in response.data.decode()