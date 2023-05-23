import pytest
from tests.conftest import client

def test_board(client):

    response = client.get("/pointsBoard")

    welcome_message = "Welcome to the points board"

    assert response.status_code == 200
    assert welcome_message in response.data.decode()