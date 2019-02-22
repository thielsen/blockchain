import pytest

from sample.transaction import *

@pytest.fixture
def test_transaction():
    test_transaction = Transaction('Test_sender', 'Test_recipient', 99)
    return test_transaction

def test_to_ordered_dict(test_transaction):
    assert test_transaction.to_ordered_dict() == OrderedDict([('sender', 'Test_sender'), ('recipient', 'Test_recipient'), ('amount', 99)])

def test_repr(test_transaction):
    assert repr(test_transaction) == "Sender: Test_sender, Recipient: Test_recipient, Amount: 99"
