from sample.blockchain import *

def test_add_value_get_last_blockchain_value():
    blockchain = [[1]]
    add_value(5)
    assert get_last_blockchain_value() == [[1], 5]