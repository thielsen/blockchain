import pytest

from sample.block import Block


def test_repr():
    test_block = Block(0, 'b81af956031df89ac679981fc6641addd4bc4fe49641570886ec258986cc976d',
                       ['Test_Transaction'], 99, 0)
    print(repr(test_block))
    assert repr(test_block) == "{'index': 0, 'previous_hash': 'b81af956031df89ac679981fc6641addd4bc4fe49641570886ec258986cc976d', 'transactions': ['Test_Transaction'], 'proof': 99, 'timestamp': 0}"
