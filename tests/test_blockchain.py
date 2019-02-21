from sample.blockchain import *

def test_add_value_adds_default():
    add_value(1)
    add_value(5, get_last_blockchain_value())
    assert blockchain == [[[1], 1], [[[1], 1], 5]]

def test_get_last_blockchain_value():
    add_value(12.4)
    add_value(5.6, get_last_blockchain_value())
    assert get_last_blockchain_value() == [[[1], 12.4], 5.6]    