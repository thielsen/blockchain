from sample.blockchain import *

def test_add_value_get_last_blockchain_value():
    add_value(1)
    add_value(5, get_last_blockchain_value())
    assert get_last_blockchain_value() == [[[1], 1], 5]

def test_add_default():
    add_value(6)
    assert get_last_blockchain_value() == [[1], 6]     