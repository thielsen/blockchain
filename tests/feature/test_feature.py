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
    assert response.status_code == 200


def test_mine(test_client):
    response = test_client.post("/mine")
    # add assert for json with test data
    assert response.status_code == 201


def test_wallet_post(test_client):
    response = test_client.post("/wallet")
    # add assert for json with test data
    assert response.status_code == 201


def test_wallet_get(test_client):
    response = test_client.get("/wallet")
    # add assert for json with test data
    assert response.status_code == 201


def test_balance_get(test_client):
    response = test_client.get("/balance")
    # add assert for json with test data
    assert response.status_code == 200


def test_transaction_post(test_client):
    response = test_client.post("/transaction")
    # add assert for json with test data
    assert response.status_code == 400


def test_transaction_get(test_client):
    response = test_client.get("/transactions")
    # add assert for json with test data
    assert response.status_code == 200