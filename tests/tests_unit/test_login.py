import sys
sys.path.append(".")
from server import app


def test_login_false():
    response = app.test_client().post('/showSummary',data={'email': 'false@user.com'})
    assert response.status_code == 200


def test_login_true():
    response = app.test_client().post('/showSummary',data={'email': 'kate@shelifts.co.uk'})
    assert response.status_code == 200