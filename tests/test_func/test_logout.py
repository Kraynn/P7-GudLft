import conftest

def test_logout(client):
    response = client.post('/showSummary', data=dict(email='kate@shelifts.co.uk'), follow_redirects=True)
    assert response.status_code == 200
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Please enter your secretary email to continue' in response.data