import pytest

from sample.node import create_app

@pytest.fixture
def test_client():
    flask_app = create_app()
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client

def test_example(test_client):
    response = test_client.get("/")
    print(response.__dict__)
    assert response.status_code == 200
    assert b"Working" in response.data