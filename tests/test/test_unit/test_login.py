import conftest


def test_login_false(client):
    response = client.post('/showSummary',data={'email': 'false@user.com'})
    assert not response.status_code == 200


def test_login_true(client):
    response = client.post('/showSummary',data={'email': 'kate@shelifts.co.uk'})
    assert response.status_code == 200