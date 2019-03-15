import pytest
from flask import jsonify

from sample.node_ui import create_app


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
    assert b"private_key" in response.data
    assert response.status_code == 201


def test_balance_get(test_client):
    response = test_client.get("/balance")
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


def test_add_peer_no_data(test_client):
    response = test_client.post("/peer")
    assert response.status_code == 400
    assert b"No data" in response.data


def test_add_peer_wrong_values(test_client):
    response = test_client.post("/peer", json={"notpeer": "testpeer.com"})
    assert response.status_code == 400
    assert b"No peer" in response.data


def test_delete_peer(test_client):
    response = test_client.delete("/peer/www.test.com")
    assert b"Deleted" in response.data
    assert response.status_code == 200


def test_full_add_and_delete_peer_test(test_client):
    response = test_client.post("/peer", json={"peer": "testpeer.com"})
    assert b"Peer added" in response.data
    assert b"testpeer.com" in response.data
    assert response.status_code == 201
    response = test_client.post("/peer", json={"peer": "testpeer2.com"})
    assert b"Peer added" in response.data
    assert b"testpeer.com" in response.data
    assert b"testpeer2.com" in response.data
    assert response.status_code == 201
    response = test_client.delete("/peer/testpeer2.com")
    assert b"Deleted" in response.data
    assert b"testpeer.com" in response.data
    assert b"testpeer2.com" not in response.data
    assert response.status_code == 200

def test_get_peers(test_client):
    response = test_client.post("/peer", json={"peer": "testpeer.com"})
    response = test_client.get("/peers")
    assert b"all_peers" in response.data
    assert b"testpeer.com" in response.data
    assert response.status_code == 200
    