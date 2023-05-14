import pytest
from tests.conftest import client
from server import clubs, competitions

def test_club_has_enough_points(client):
    # Choose Iron Temple with 4 points
    club = clubs[1]

    # Choose Spring Festival with 25 places
    competition = competitions[0]

    # Buy 4 place, club has enough points
    places_to_buy = 4

    response = client.post(
        '/purchasePlaces',
        data={
            'places' : places_to_buy,
            'club' : club["name"],
            'competition' : competition["name"],
        }
    )
    assert response.status_code == 200
    assert "booking complete!" in response.data.decode()
    assert club["points"] == 0
    assert competition["numberOfPlaces"] == 21


def test_club_doesnt_have_enough_points(client):
    # Choose Iron Temple with 4 points
    club = clubs[1]

    # Choose Spring Festival with 25 places
    competition = competitions[0]

    # Buy 5 places, which is too much
    places_to_buy = 5

    response = client.post(
        '/purchasePlaces',
        data={
            'places' : places_to_buy,
            'club' : club["name"],
            'competition' : competition["name"],
        }
    )

    assert response.status_code == 200
    assert "You don't have enough points" in response.data.decode()
