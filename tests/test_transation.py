
import pytest

from sample.transaction import *

ALICE = '30819f300d06092a864886f70d010101050003818d0030818902818100ba60fcb9f2a151bc04a452c1c92ac5dc69b9ccb81a4baae1fa7400972b6834f2141af511827a311c739ce38c0caf521b0f3911ebb447fa3512db10d93d717831b521e131a837eaa101011671336c81cc098ef94682ba7b88f90541b39ebefb1c70b87a229b3427cc42d97ad21c814aca67860b55ebf86e3dd83e9557b8b735630203010001'
BOB = '30819f300d06092a864886f70d010101050003818d0030818902818100b15b2ed9b77aabd723e6bed475e5ec2b7b83e5be83582c32686db09e949fc046256f573f351103ff3b03ab176b05ba33180fdf83b227775b8a59380238ff21d7d4a8c9de8e3880f025769a7b660dce7a033b795b9f8c12e756cf6a4a5521e3e279d87defe981db430b7851ef4fcbf2df792e90bde18d1785746f706a664fddef0203010001'

@pytest.fixture
def test_transaction():
    test_transaction = Transaction(ALICE, BOB, '', 99)
    return test_transaction

def test_to_ordered_dict(test_transaction):
    assert test_transaction.to_ordered_dict() == OrderedDict([('sender', ALICE), ('recipient', BOB), ('amount', 99)])

def test_repr(test_transaction):
    assert repr(test_transaction) == "Sender: {}, Recipient: {}, Amount: 99".format(ALICE, BOB)
