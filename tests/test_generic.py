import pytest
from tests.conftest import client

def test_index(client):

    # Checking for a specific paragraph in the webpage.
    welcome_title = "Welcome to the GUDLFT Registration Portal!"
    response = client.get("/")

    assert response.status_code == 200
    assert welcome_title in response.data.decode()


def test_logout(client):

    # Checking for a specific paragraph in the webpage.
    welcome_title = "Welcome to the GUDLFT Registration "
    response = client.get("/logout", follow_redirects=True)

    assert response.status_code == 200
    assert welcome_title in response.data.decode()
