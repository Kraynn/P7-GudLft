import conftest
import json

def test_show_summary(client):
    with open('competitions.json') as comps:
        competitions = json.load(comps)['competitions']
    response = client.post('/showSummary',data={'email': 'kate@shelifts.co.uk'})
    for competition in competitions:
        assert competition['name'] in str(response.get_data())