import sys
sys.path.append(".")
from server import app


def test_logout():
    response = app.test_client().post('/showSummary', data=dict(email='kate@shelifts.co.uk'), follow_redirects=True)
    assert response.status_code == 200
    response = app.test_client().get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Please enter your secretary email to continue' in response.data