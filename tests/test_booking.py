import pytest
from tests.conftest import client
from server import clubs, competitions


def test_book_too_much_places(client):
    places_to_book = 666
    error = "You cannot book more than 12 places."

    # Competition is Sping Festival, with 25 places
    competition = competitions[0]

    # Club is Simply Lift with 13 points
    club = clubs[0]

    response = client.post(
        "/purchasePlaces",
        data={
            "club": club["name"],
            "competition": competition["name"],
            "places": places_to_book
        }
    )

    assert response.status_code == 200
    assert error in response.data.decode()
    assert int(club["points"]) == 13


def test_book_less_than_one(client):
    places_to_book = -666
    error = "Please enter a number between 1 and 12 to book places."

    # Competition is Sping Festival, with 25 places
    competition = competitions[0]

    # Club is Simply Lift with 13 points
    club = clubs[0]

    response = client.post(
        "/purchasePlaces",
        data={
            "club": club["name"],
            "competition": competition["name"],
            "places": places_to_book
        }
    )

    assert response.status_code == 200
    assert error in response.data.decode()
    assert int(club["points"]) == 13


def test_book_an_ok_amount_of_place(client):
    places_to_book = 5

    # Competition is Sping Festival, with 25 places
    competition = competitions[0]
    places = competition["numberOfPlaces"]

    # Club is Simply Lift with 13 points
    club = clubs[0]

    response = client.post(
        "/purchasePlaces",
        data={
            "club": club["name"],
            "competition": competition["name"],
            "places": places_to_book
        }
    )

    assert response.status_code == 200
    assert "booking complete" in response.data.decode()
    assert int(club["points"]) == 8