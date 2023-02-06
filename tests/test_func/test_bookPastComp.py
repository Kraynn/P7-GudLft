import conftest


club = 'Simply Lift'
competition = 'Fall Classic'


def test_book_past_comp(client):
    response = client.get(f'/book/{competition}/{club}')
    assert response.status_code == 200
    assert b'Competition closed' in response.data