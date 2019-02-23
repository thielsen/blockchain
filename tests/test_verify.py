
import os
import pytest


from sample.blockchain import *
from sample.block import *
from sample.transaction import *
from sample.verify import *

ALICE = '30819f300d06092a864886f70d010101050003818d0030818902818100ba60fcb9f2a151bc04a452c1c92ac5dc69b9ccb81a4baae1fa7400972b6834f2141af511827a311c739ce38c0caf521b0f3911ebb447fa3512db10d93d717831b521e131a837eaa101011671336c81cc098ef94682ba7b88f90541b39ebefb1c70b87a229b3427cc42d97ad21c814aca67860b55ebf86e3dd83e9557b8b735630203010001'
BOB = '30819f300d06092a864886f70d010101050003818d0030818902818100b15b2ed9b77aabd723e6bed475e5ec2b7b83e5be83582c32686db09e949fc046256f573f351103ff3b03ab176b05ba33180fdf83b227775b8a59380238ff21d7d4a8c9de8e3880f025769a7b660dce7a033b795b9f8c12e756cf6a4a5521e3e279d87defe981db430b7851ef4fcbf2df792e90bde18d1785746f706a664fddef0203010001'
SIMON = '30819f300d06092a864886f70d010101050003818d0030818902818100c313554034be1eaf7b8991ec41d02e249a24cee0016fbc1be95c8232fd933b6e76f0ef87038a6fc4874eb3317bfb0b6effeae1b439cadc0812a4fdcdf5ce043c46689ebee7eda6c243cc100f4945d33a9ed28ed7bce1b3f9eae402ad98b456bc087d2a7063467b4551c08c331da7ada2685e48270b25e428632f24cf8b357e010203010001'

@pytest.fixture
def test_blockchain():
    test_blockchain = BlockChain(SIMON, './tests/blockchain.bin')
    yield test_blockchain
    if os.path.isfile(test_blockchain.file_location):
        os.remove(test_blockchain.file_location)

def test_invalid_proof(test_blockchain):
    assert Verify.valid_proof([], 'b81af956031df89ac679981fc6641addd4bc4fe49641570886ec258986cc976d', 0) == False

def test_valid_proof(test_blockchain):
    assert Verify.valid_proof([], 'b81af956031df89ac679981fc6641addd4bc4fe49641570886ec258986cc976d', 87) == True

def test_verify_chain(test_blockchain):
    assert Verify.verify_chain(test_blockchain.view_blockchain()) == True

def test_verify_bad_chain_with_false_transaction(test_blockchain):
    test_blockchain.mine_block()
    test_blockchain.add_transaction(BOB, '', amount=3.4)
    test_blockchain.add_transaction(ALICE, '', amount=3.6)
    test_blockchain.mine_block()
    test_block = Block(0, '', [{'sender': 'poorfool', 'recipient': 'badactor', 'amount': 1000.0}], 0)
    test_blockchain._BlockChain__blockchain[1] = test_block
    assert Verify.verify_chain(test_blockchain.view_blockchain()) == False

def test_verify_bad_chain_with_invalid_proof(test_blockchain):
    test_blockchain.mine_block()
    test_blockchain.add_transaction(BOB, '', amount=3.4)
    test_blockchain.add_transaction(ALICE, '', amount=3.6)
    test_blockchain.mine_block()
    test_block = Block(1, 'a93bc01ba42854e03622a737f6b84a9d43a5f0af42c5ffcb94de0007ff3e6812', [{'amount': 10, 'recipient': SIMON, 'sender': 'MINED'}], 268)
    test_blockchain._BlockChain__blockchain[1] = test_block
    assert Verify.verify_chain(test_blockchain.view_blockchain()) == False
