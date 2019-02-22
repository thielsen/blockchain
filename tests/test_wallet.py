from sample.wallet import Wallet
import pytest

@pytest.fixture
def test_wallet():
    test_wallet = Wallet()
    yield test_wallet

def test_confirm_private_key_generated(test_wallet):
    assert test_wallet.private_key == 00

def test_confirm_public_key_generated(test_wallet):
    assert test_wallet.private_key == 00