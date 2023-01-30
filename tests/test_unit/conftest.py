import pytest
import sys
sys.path.append(".")
import server


@pytest.fixture()
def client():
    server.app.config['TESTING'] = True
    client = server.app.test_client()
    return client