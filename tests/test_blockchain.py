from sample.blockchain import *

test_blockchain = BlockChain()

# def test_add_transaction_adds_default():
#     add_transaction(1, get_last_blockchain_value())
#     add_transaction(5, get_last_blockchain_value())
#     assert blockchain == [[[1], 1], [[[1], 1], 5]]

# def test_get_last_blockchain_value():
#     add_transaction(12.4, get_last_blockchain_value())
#     add_transaction(5.6, get_last_blockchain_value())
#     assert get_last_blockchain_value() == [[[[[1], 1], 5], 12.4], 5.6] 

def test_add_transaction_to_open():
    test_blockchain.add_transaction('Bob', amount=3.4)
    test_blockchain.add_transaction('Alice', amount=3.6)
    assert test_blockchain.open_transactions == [{'amount': 3.4, 'recipient': 'Bob', 'sender': 'Simon'}, {'amount': 3.6, 'recipient': 'Alice', 'sender': 'Simon'}]

def test_mine_block():
    test_blockchain.mine_block()
    assert test_blockchain.blockchain == [{'index': 0, 'previous_hash': '', 'transactions': []}, {'index': 1, 'previous_hash': "[-0-,- -'-'-,- -[-]-]", 'transactions': [{'amount': 3.4, 'recipient': 'Bob', 'sender': 'Simon'}, {'amount': 3.6, 'recipient': 'Alice', 'sender': 'Simon'}]}]

def test_clear_open_transactions_after_mining():
    assert test_blockchain.open_transactions == []

def test_verify_chain():
    assert test_blockchain.verify_chain() == True

def test_verify_bad_chain():
    test_blockchain.blockchain[0] = {'previous_hash': '', 
                       'index': 0,
                       'transactions': [{'sender': 'poorfool', 'recipient': 'badactor', 'amount': 1000.0}]
}
    assert test_blockchain.verify_chain() == False

def test_hash_block():
    assert test_blockchain.hash_block({'previous_hash': '', 'index': 0, 'transactions': []}) == "[-0-,- -'-'-,- -[-]-]"

def test_check_participants_are_added():
    assert test_blockchain.participants == set(['Alice', 'Bob', 'Simon'])