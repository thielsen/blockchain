from sample.blockchain import *
from sample.hash_utilities import *
from sample.block import *
from sample.transaction import *

import pytest
import os

@pytest.fixture
def test_blockchain():
    test_blockchain = BlockChain('./tests/blockchain.bin')
    yield test_blockchain
    if os.path.isfile(test_blockchain.file_location):
        os.remove(test_blockchain.file_location)

# def test_add_transaction_adds_default():
#     add_transaction(1, get_last_blockchain_value())
#     add_transaction(5, get_last_blockchain_value())
#     assert blockchain == [[[1], 1], [[[1], 1], 5]]

# def test_get_last_blockchain_value():
#     add_transaction(12.4, get_last_blockchain_value())
#     add_transaction(5.6, get_last_blockchain_value())
#     assert get_last_blockchain_value() == [[[[[1], 1], 5], 12.4], 5.6] 

def test_add_transaction_to_open(test_blockchain):
    test_blockchain.mine_block()
    test_blockchain.add_transaction('Bob', amount=3.4)
    test_blockchain.add_transaction('Alice', amount=3.6)
    print(test_blockchain.open_transactions[0])
    assert repr(test_blockchain.open_transactions[0]) == 'Sender: Simon, Recipient: Bob, Amount: 3.4'
    assert repr(test_blockchain.open_transactions[1]) == 'Sender: Simon, Recipient: Alice, Amount: 3.6'
    assert isinstance(test_blockchain.open_transactions[0], Transaction) is True
    assert isinstance(test_blockchain.open_transactions[1], Transaction) is True

def test_mine_block(test_blockchain):
    test_blockchain.mine_block()
    test_blockchain.add_transaction('Bob', amount=3.4)
    test_blockchain.add_transaction('Alice', amount=3.6)
    test_blockchain.mine_block()
    assert ('Index: 0' in repr(test_blockchain.blockchain[0])) is True
    assert ('Index: 1' in repr(test_blockchain.blockchain[1])) is True
    assert ('Index: 2' in repr(test_blockchain.blockchain[2])) is True
    assert (isinstance(test_blockchain.blockchain[0], Block)) is True
    assert (isinstance(test_blockchain.blockchain[1], Block)) is True
    assert (isinstance(test_blockchain.blockchain[2], Block)) is True

def test_clear_open_transactions_after_mining(test_blockchain):
    assert test_blockchain.open_transactions == []

def test_verify_chain(test_blockchain):
    assert test_blockchain.verify_chain() == True

def test_verify_bad_chain_with_false_transaction(test_blockchain):
    test_blockchain.mine_block()
    test_blockchain.add_transaction('Bob', amount=3.4)
    test_blockchain.add_transaction('Alice', amount=3.6)
    test_blockchain.mine_block()
    test_block = Block(0, '', [{'sender': 'poorfool', 'recipient': 'badactor', 'amount': 1000.0}], 0)
    test_blockchain.blockchain[1] = test_block
    assert test_blockchain.verify_chain() == False

def test_verify_bad_chain_with_invalid_proof(test_blockchain):
    test_blockchain.mine_block()
    test_blockchain.add_transaction('Bob', amount=3.4)
    test_blockchain.add_transaction('Alice', amount=3.6)
    test_blockchain.mine_block()
    test_block = Block(1, 'a93bc01ba42854e03622a737f6b84a9d43a5f0af42c5ffcb94de0007ff3e6812', [{'amount': 10, 'recipient': 'Simon', 'sender': 'MINED'}], 268)
    test_blockchain.blockchain[1] = test_block
    assert test_blockchain.verify_chain() == False

def test_check_participants_are_added(test_blockchain):
    test_blockchain.mine_block()
    test_blockchain.add_transaction('Bob', amount=3.4)
    test_blockchain.add_transaction('Alice', amount=3.6)
    test_blockchain.mine_block()
    assert test_blockchain.participants == set(['Alice', 'Bob', 'Simon'])

def test_get_balance(test_blockchain):
    test_blockchain.mine_block()
    test_blockchain.add_transaction('Bob', amount=3.4)
    test_blockchain.add_transaction('Alice', amount=3.6)
    test_blockchain.mine_block()
    assert test_blockchain.get_balance('Simon') == 13
    assert test_blockchain.get_balance('Bob') == 3.4
    assert test_blockchain.get_balance('Alice') == 3.6

def test_mining_block_adds_reward(test_blockchain):
    test_blockchain.mine_block()
    test_blockchain.mine_block()
    assert test_blockchain.get_balance('Simon') == 20

def test_cannot_send_if_no_balance(test_blockchain):
    test_blockchain.add_transaction('Bob', amount=3.4)
    test_blockchain.add_transaction('Alice', amount=3.6)
    test_blockchain.mine_block()
    assert test_blockchain.get_balance('Bob') == 0
    assert test_blockchain.get_balance('Alice') == 0

def test_cannot_send_if_transactions_in_queue_are_too_much(test_blockchain):
    test_blockchain.mine_block()
    test_blockchain.add_transaction('Bob', amount=10.0)
    test_blockchain.add_transaction('Alice', amount=10.0)
    assert len(test_blockchain.open_transactions) == 1

def test_invalid_proof(test_blockchain):
    assert test_blockchain.valid_proof([], 'b81af956031df89ac679981fc6641addd4bc4fe49641570886ec258986cc976d', 0) == False

def test_valid_proof(test_blockchain):
    assert test_blockchain.valid_proof([], 'b81af956031df89ac679981fc6641addd4bc4fe49641570886ec258986cc976d', 87) == True

# Need to mock this test with hardcoded timestamps as time stamps are changing
# def test_proof_of_work(test_blockchain):
#     test_blockchain.add_transaction('Bob', amount=3.4)
#     test_blockchain.add_transaction('Alice', amount=3.6)
#     test_blockchain.mine_block()
#     assert test_blockchain.proof_of_work() == 348

def test_create_file(test_blockchain):
    test_blockchain.mine_block()
    with open(test_blockchain.file_location, mode='rb') as f:
            file_content = pickle.loads(f.read())
    assert file_content['ot'] == []
    print(file_content['chain'][0])
    assert('Index: 0' in repr(file_content['chain'][0])) == True
    assert('Index: 1' in repr(file_content['chain'][1])) == True
    assert (isinstance(file_content['chain'][0], Block)) is True
    assert (isinstance(file_content['chain'][1], Block)) is True

# def test_load_data_on_startup