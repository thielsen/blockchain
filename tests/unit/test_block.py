import pytest

from sample.block import Block

def test_repr():
    test_block = Block(0, 'b81af956031df89ac679981fc6641addd4bc4fe49641570886ec258986cc976d', 
                       ['Test_Transaction'], 99, 0)
    assert repr(test_block) == "Index: 0, Previous Hash: b81af956031df89ac679981fc6641addd4bc4fe49641570886ec258986cc976d, Transaction: ['Test_Transaction'], Proof: 99, Timestamp: 0"
