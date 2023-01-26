import json
import sys
sys.path.append(".")
from server import app


def test_show_summary():
    with open('competitions.json') as comps:
        competitions = json.load(comps)['competitions']
    response = app.test_client().post('/showSummary',data={'email': 'kate@shelifts.co.uk'})
    for competition in competitions:
        assert competition['name'] in str(response.get_data())
