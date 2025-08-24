import pytest
from app import app
import json

@pytest.fixture
def client():
    """
    Create a test client for the app.
    :return:
    """
    return app.test_client()

class Testing:
    def test_homepage(self, client):
        response = client.get('/')
        assert response.status_code == 200
        assert b"Hello World" in response.data

    def test_add_me(self, client):
        response = client.post('/add_me', data=json.dumps(
        {
            'first_number': 10,
            'second_number': 20,
        }))
        assert response.status_code == 200
        assert b"30" in response.data

    def test_multiply_me(self, client):
        response = client.post('/multiply_me', data=json.dumps({
            'first_number': 10,
            'second_number': 20
        }))
        assert response.status_code == 200
        assert b"200" in response.data

    def test_cube_me(self, client):
        response = client.post('/cube_me', data=json.dumps({
            'first_number': 3
        }))
        assert response.status_code == 200
        assert b"27" in response.data