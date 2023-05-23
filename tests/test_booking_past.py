import pytest
from datetime import datetime
from tests.conftest import client
from server import clubs, competitions
from flask import request

def test_booking_valid_date(client):

    # Competition is Winter Showdown with 17 places
    # It takes place on following date : 9999-01-01 13:30:00
    competitions.append(
        {
        "name": "Winter Showdown",
        "date": "9999-01-01 13:30:00",
        "numberOfPlaces": "17"
        } 
    )
    
    response = client.get("/book/Winter Showdown/Iron Temple")

    assert response.status_code == 200
    assert "You can now book !" in response.data.decode()


def test_booking_past_date(client):

    # Competition is Spring Festival with 25 places
    # It takes place on following date : 2020-03-27 10:00:00

    response = client.get("/book/Spring Festival/Iron Temple")
    
    assert response.status_code == 200
    assert "You cannot book in a past competition !" in response.data.decode()
