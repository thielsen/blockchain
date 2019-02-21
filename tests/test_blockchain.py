from sample.blockchain import *
import pytest

@pytest.fixture
def test_blockchain():
    test_blockchain = BlockChain()
    return test_blockchain

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
    assert test_blockchain.open_transactions == [{'amount': 3.4, 'recipient': 'Bob', 'sender': 'Simon'}, {'amount': 3.6, 'recipient': 'Alice', 'sender': 'Simon'}]

def test_mine_block(test_blockchain):
    test_blockchain.mine_block()
    test_blockchain.add_transaction('Bob', amount=3.4)
    test_blockchain.add_transaction('Alice', amount=3.6)
    test_blockchain.mine_block()
    assert test_blockchain.blockchain == [{'index': 0, 'previous_hash': '', 'transactions': []}, {'index': 1, 'previous_hash': 'b2242851cf5e7216d0bbb01ad9b6659bbca55f43c9ac3e63d0fac318b579c253', 'transactions': [{'amount': 10, 'recipient': 'Simon', 'sender': 'MINED'}]}, {'index': 2, 'previous_hash': 'e25a7acdbfff55cc8d075de20429bd9c2ede0a1d5e7d54155bcee739665e6fd3', 'transactions': [{'amount': 3.4, 'recipient': 'Bob', 'sender': 'Simon'}, {'amount': 3.6, 'recipient': 'Alice', 'sender': 'Simon'}, {'amount': 10, 'recipient': 'Simon', 'sender': 'MINED'}]}]

def test_clear_open_transactions_after_mining(test_blockchain):
    assert test_blockchain.open_transactions == []

def test_verify_chain(test_blockchain):
    assert test_blockchain.verify_chain() == True

def test_verify_bad_chain(test_blockchain):
    test_blockchain.mine_block()
    test_blockchain.add_transaction('Bob', amount=3.4)
    test_blockchain.add_transaction('Alice', amount=3.6)
    test_blockchain.mine_block()
    test_blockchain.blockchain[0] = {'previous_hash': '', 
                       'index': 0,
                       'transactions': [{'sender': 'poorfool', 'recipient': 'badactor', 'amount': 1000.0}]
}
    assert test_blockchain.verify_chain() == False

def test_hash_block(test_blockchain):
    assert test_blockchain.hash_block({'previous_hash': '', 'index': 0, 'transactions': []}) == 'b2242851cf5e7216d0bbb01ad9b6659bbca55f43c9ac3e63d0fac318b579c253'

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
    print(test_blockchain.blockchain)
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
    assert test_blockchain.open_transactions ==  [{'amount': 10.0, 'recipient': 'Bob', 'sender': 'Simon'}]

def test_invalid_proof(test_blockchain):
    assert test_blockchain.valid_proof([{'amount': 10.0, 'recipient': 'Bob', 'sender': 'Simon'}] , 'b2242851cf5e7216d0bbb01ad9b6659bbca55f43c9ac3e63d0fac318b579c253', 0) == False

def test_valid_proof(test_blockchain):
    x = 0
    while x < 100:
        assert test_blockchain.valid_proof([{'amount': 10.0, 'recipient': 'Bob', 'sender': 'Simon'}] , 'b2242851cf5e7216d0bbb01ad9b6659bbca55f43c9ac3e63d0fac318b579c253', x) == True
        print (x)
        x = x + 1