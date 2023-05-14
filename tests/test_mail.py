import pytest
from tests.conftest import client

def test_mail_exists(client):
    mail = "admin@irontemple.com"
    response = client.post('/showSummary', data={'email' : mail})
    assert response.status_code == 200
    assert mail in response.data.decode()


def test_mail_doesnt_exists(client):
    error = "Mail wasn't found"
    mail = "a@irontemple.com"
    response = client.post('/showSummary', data={'email' : mail})
    assert response.status_code == 200
    assert error in response.data.decode()
