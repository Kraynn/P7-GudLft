import conftest

club = 'Iron Temple'
competition = 'Spring Festival'


def test_booking_number_of_places(client):
    place = 2
    response = client.post('/purchasePlaces', data={'club': club, 'competition': competition, 'places': place})
    assert response.status_code == 200
    assert b"You have reserved 2 places." in response.data
    assert b"Points available: 2" in response.data

