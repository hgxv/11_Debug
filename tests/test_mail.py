import pytest
from tests.conftest import client
from server import clubs

def test_mail_exists(client):
    mail = clubs[1]["email"]
    response = client.post('/showSummary', data={'email' : mail})

    assert response.status_code == 200
    assert mail in response.data.decode()


def test_mail_doesnt_exists(client):

    # Checking a made up email, that isn't in the json file.
    # Error message should be found in HTML.
    error = "Mail was not found"
    mail = "a@irontemple.com"

    response = client.post('/showSummary', data={'email' : mail})
    assert response.status_code == 200
    assert error in response.data.decode()
