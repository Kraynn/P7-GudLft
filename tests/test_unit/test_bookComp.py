import conftest

club = 'Iron Temple'
competition = 'Spring Festival'


def test_booking_places(client):
    place = 2
    response = client.post('/purchasePlaces', data={'club': club, 'competition': competition, 'places': place})
    assert response.status_code == 200
    assert b"Great-booking complete"

def test_booking_exceeding_places(client):
    place = 10
    response = client.post('/purchasePlaces', data={'club': club, 'competition': competition, 'places': place})
    assert response.status_code == 200
    assert b"Booking incomplete !"

def test_booking_over_12_places(client):
    place = 13
    response = client.post('/purchasePlaces', data={'club': club, 'competition': competition, 'places': place})
    assert response.status_code == 200
    assert b"Booking incomplete ! 12 places maximum allowed !"