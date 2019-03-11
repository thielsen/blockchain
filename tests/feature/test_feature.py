import pytest

from sample.node import create_app


@pytest.fixture
def test_client():
    flask_app = create_app()
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client


def test_home_page(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"Working" in response.data


def test_blockchain(test_client):
    response = test_client.get("/blockchain")
    assert b"index" in response.data
    assert response.status_code == 200


def test_mine(test_client):
    response = test_client.post("/mine")
    assert b"MINED" in response.data
    assert response.status_code == 201


def test_wallet_post(test_client):
    response = test_client.post("/wallet")
    assert b"private_key" in response.data
    assert response.status_code == 201


def test_wallet_get(test_client):
    response = test_client.get("/wallet")
    print(response.data)
    assert b"private_key" in response.data
    assert response.status_code == 201


def test_balance_get(test_client):
    response = test_client.get("/balance")
    print(response.data)
    assert b"balance" in response.data
    assert response.status_code == 200


def test_transaction_post(test_client):
    response = test_client.post("/transaction")
    assert b"No data provided" in response.data
    assert response.status_code == 400


def test_transaction_get(test_client):
    response = test_client.get("/transactions")
    assert b"[]" in response.data
    assert response.status_code == 200
