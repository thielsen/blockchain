from pickle import loads
import pytest
import os

from sample.blockchain import *
from sample.hash_utilities import *
from sample.block import *
from sample.transaction import *

ALICE = '30819f300d06092a864886f70d010101050003818d0030818902818100ba60fcb9f2a151bc04a452c1c92ac5dc69b9ccb81a4baae1fa7400972b6834f2141af511827a311c739ce38c0caf521b0f3911ebb447fa3512db10d93d717831b521e131a837eaa101011671336c81cc098ef94682ba7b88f90541b39ebefb1c70b87a229b3427cc42d97ad21c814aca67860b55ebf86e3dd83e9557b8b735630203010001'
BOB = '30819f300d06092a864886f70d010101050003818d0030818902818100b15b2ed9b77aabd723e6bed475e5ec2b7b83e5be83582c32686db09e949fc046256f573f351103ff3b03ab176b05ba33180fdf83b227775b8a59380238ff21d7d4a8c9de8e3880f025769a7b660dce7a033b795b9f8c12e756cf6a4a5521e3e279d87defe981db430b7851ef4fcbf2df792e90bde18d1785746f706a664fddef0203010001'
SIMON = '30819f300d06092a864886f70d010101050003818d0030818902818100c313554034be1eaf7b8991ec41d02e249a24cee0016fbc1be95c8232fd933b6e76f0ef87038a6fc4874eb3317bfb0b6effeae1b439cadc0812a4fdcdf5ce043c46689ebee7eda6c243cc100f4945d33a9ed28ed7bce1b3f9eae402ad98b456bc087d2a7063467b4551c08c331da7ada2685e48270b25e428632f24cf8b357e010203010001'

@pytest.fixture
def test_blockchain():
    test_blockchain = BlockChain(SIMON, './tests/blockchain.bin')
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
    test_blockchain.add_transaction(BOB, '', amount=3.4)
    test_blockchain.add_transaction(ALICE, '', amount=3.6)

    assert repr(test_blockchain.view_open_transactions()[0]) == 'Sender: {}, Recipient: {}, Amount: 3.4'.format(SIMON, BOB)
    assert repr(test_blockchain.view_open_transactions()[1]) == 'Sender: {}, Recipient: {}, Amount: 3.6'.format(SIMON, ALICE)
    assert isinstance(test_blockchain.view_open_transactions()[0], Transaction) is True
    assert isinstance(test_blockchain.view_open_transactions()[1], Transaction) is True

def test_mine_block(test_blockchain):
    test_blockchain.mine_block()
    test_blockchain.add_transaction(BOB, '', amount=3.4)
    test_blockchain.add_transaction(ALICE, '', amount=3.6)
    test_blockchain.mine_block()
    assert ('Index: 0' in repr(test_blockchain.view_blockchain()[0])) is True
    assert ('Index: 1' in repr(test_blockchain.view_blockchain()[1])) is True
    assert ('Index: 2' in repr(test_blockchain.view_blockchain()[2])) is True
    assert (isinstance(test_blockchain.view_blockchain()[0], Block)) is True
    assert (isinstance(test_blockchain.view_blockchain()[1], Block)) is True
    assert (isinstance(test_blockchain.view_blockchain()[2], Block)) is True

def test_clear_open_transactions_after_mining(test_blockchain):
    assert test_blockchain.view_open_transactions() == []

def test_get_balance(test_blockchain):
    test_blockchain.mine_block()
    test_blockchain.add_transaction(BOB, '', amount=3.4)
    test_blockchain.add_transaction(ALICE, '', amount=3.6)
    test_blockchain.mine_block()
    assert test_blockchain.get_balance() == 13

def test_mining_block_adds_reward(test_blockchain):
    test_blockchain.mine_block()
    test_blockchain.mine_block()
    assert test_blockchain.get_balance() == 20

def test_cannot_send_if_no_balance(test_blockchain):
    test_blockchain.add_transaction(BOB, '', amount=3.4)
    test_blockchain.add_transaction(ALICE, '', amount=3.6)
    test_blockchain.mine_block()
    assert (BOB in repr(test_blockchain.view_blockchain())) is False
    assert (ALICE in repr(test_blockchain.view_blockchain())) is False

def test_cannot_send_if_transactions_in_queue_are_too_much(test_blockchain):
    test_blockchain.mine_block()
    test_blockchain.add_transaction(BOB, '', amount=10.0)
    test_blockchain.add_transaction(ALICE, '', amount=10.0)
    assert len(test_blockchain.view_open_transactions()) == 1


# Need to mock this test with hardcoded timestamps as time stamps are changing
# def test_proof_of_work(test_blockchain):
#     test_blockchain.add_transaction('Bob', amount=3.4)
#     test_blockchain.add_transaction('Alice', amount=3.6)
#     test_blockchain.mine_block()
#     assert test_blockchain.proof_of_work() == 348

def test_create_file(test_blockchain):
    test_blockchain.mine_block()
    with open(test_blockchain.file_location, mode='rb') as f:
        file_content = loads(f.read())
    assert file_content['ot'] == []
    assert('Index: 0' in repr(file_content['chain'][0])) == True
    assert('Index: 1' in repr(file_content['chain'][1])) == True
    assert (isinstance(file_content['chain'][0], Block)) is True
    assert (isinstance(file_content['chain'][1], Block)) is True

# def test_load_data_on_startup