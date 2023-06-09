import pytest

import server

server.competitions = [
    {
        "name": "Spring Festival",
        "date": "2020-03-27 10:00:00",
        "numberOfPlaces": "25"
    },
    {
        "name": "Fall Classic",
        "date": "2020-10-22 13:30:00",
        "numberOfPlaces": "13"
    },
    {
    "name": "Winter Showdown",
    "date": "9999-01-01 13:30:00",
    "numberOfPlaces": "17"
    },
    {
    "name": "Little Event",
    "date": "9999-01-01 13:30:00",
    "numberOfPlaces": "2"
    }    
]

server.clubs = [
    {
        "name":"Simply Lift",
        "email":"john@simplylift.co",
        "points":"13"
    },
    {
        "name":"Iron Temple",
        "email": "admin@irontemple.com",
        "points":"4"
    },
    {   "name":"She Lifts",
        "email": "kate@shelifts.co.uk",
        "points":"12"
    }
]


@pytest.fixture
def client():
    with server.app.test_client() as client:
        yield client