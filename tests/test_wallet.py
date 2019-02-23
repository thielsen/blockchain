
from sample.wallet import Wallet
import pytest

@pytest.fixture
def test_wallet():
    test_wallet = Wallet()
    test_wallet.create_keys()
    yield test_wallet

def test_confirm_private_key_generated(test_wallet):
    assert ('3082' in test_wallet.private_key) is True

def test_confirm_public_key_generated(test_wallet):
    assert ('3081' in test_wallet.public_key) is True

def test_confirm_different_keys_are_produced_each_run(test_wallet):
    test_wallet2 = Wallet()
    test_wallet2.create_keys()
    assert test_wallet.private_key != test_wallet2.private_key

def test_sign_transaction(test_wallet):
    # Private key changes each time so this does - how can I mock a wallet?
    signed_transaction = test_wallet.sign_transaction('Test_Sender', 'Test_Recipient', 100)
    assert len(signed_transaction) == 256