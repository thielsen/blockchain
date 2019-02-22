from sample.blockchain import *
from sample.hash_utilities import *
from sample.block import *
from sample.transaction import *
from sample.verify import *

import pytest
import os

@pytest.fixture
def test_blockchain():
    test_blockchain = BlockChain('./tests/blockchain.bin')
    yield test_blockchain
    if os.path.isfile(test_blockchain.file_location):
        os.remove(test_blockchain.file_location)

def test_invalid_proof(test_blockchain):
    test_verify = Verify()
    assert test_verify.valid_proof([], 'b81af956031df89ac679981fc6641addd4bc4fe49641570886ec258986cc976d', 0) == False

def test_valid_proof(test_blockchain):
    test_verify = Verify()
    assert test_verify.valid_proof([], 'b81af956031df89ac679981fc6641addd4bc4fe49641570886ec258986cc976d', 87) == True

def test_verify_chain(test_blockchain):
    test_verify = Verify()
    assert test_verify.verify_chain(test_blockchain.blockchain) == True

def test_verify_bad_chain_with_false_transaction(test_blockchain):
    test_verify = Verify()
    test_blockchain.mine_block()
    test_blockchain.add_transaction('Bob', amount=3.4)
    test_blockchain.add_transaction('Alice', amount=3.6)
    test_blockchain.mine_block()
    test_block = Block(0, '', [{'sender': 'poorfool', 'recipient': 'badactor', 'amount': 1000.0}], 0)
    test_blockchain.blockchain[1] = test_block
    assert test_verify.verify_chain(test_blockchain.blockchain) == False

def test_verify_bad_chain_with_invalid_proof(test_blockchain):
    test_verify = Verify()
    test_blockchain.mine_block()
    test_blockchain.add_transaction('Bob', amount=3.4)
    test_blockchain.add_transaction('Alice', amount=3.6)
    test_blockchain.mine_block()
    test_block = Block(1, 'a93bc01ba42854e03622a737f6b84a9d43a5f0af42c5ffcb94de0007ff3e6812', [{'amount': 10, 'recipient': 'Simon', 'sender': 'MINED'}], 268)
    test_blockchain.blockchain[1] = test_block
    assert test_verify.verify_chain(test_blockchain.blockchain) == False
