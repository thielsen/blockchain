from sample.blockchain import *

def test_add_transaction_adds_default():
    add_transaction(1, get_last_blockchain_value())
    add_transaction(5, get_last_blockchain_value())
    assert blockchain == [[[1], 1], [[[1], 1], 5]]

def test_get_last_blockchain_value():
    add_transaction(12.4, get_last_blockchain_value())
    add_transaction(5.6, get_last_blockchain_value())
    assert get_last_blockchain_value() == [[[[[1], 1], 5], 12.4], 5.6]   