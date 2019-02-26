from pickle import loads
import os
import pytest

from sample.blockchain import BlockChain
from sample.block import Block
from sample.transaction import Transaction

BOB_PRIVATE = '3082025d02010002818100b91c16d15e43750fda241ffc51d770b90cba48aa4594ad9ded911970df3f95044a9404407c637b38bbe21f802502b2307f2d62a69657365c86c5cc9c915b2a9e27e1ee3951d18ec8201cb48362d25536d70919ee219a118ad3c9c683f340db28dd39bfcad00939f2d39c566bd0e7417aab85463f89ef4c2d2816789a35e1998302030100010281801998db44e7728f90fa1acdbb7ffbb93035a4dae084cfaaf4704204d11965faeec57b535d3176363761afc2a85f35d0bb2912f715cf2b4f2e9b4a65e16eae3b25b7d9235361c702807c96aa23f4c9862685b2ca77105d4c6ded54b12940c8a3e64ef669cb8be77dd8547e8c315b6a72a072bc88b258cdbef01dc0434cce36d559024100bd94bfbfe5659aa607b3b55d5928ae6d4af60b05736e6c4894dfb6f1b048783e45d55be8563dd12592fa8cfabaa327a730bf4f7733195763126c01a6b6b53b19024100f9f6502c875fa4c50e9e2ae6d930709eb2e492326627c806a9ace012caf5e198e31afad0fc049e8559dc740928938fe488021405dd2af66ae58ffe9c8ff2e8fb0240395f1f9c3a16c27346576b2661c9fee7524d1d4ebbfd09c5f94fae747bcda29dedd240ab12164909deedf5e616bf334bd463c0efa8c61d7cfce134aab8162659024100bcfaa82ac23e61484a80f2568da5bdbf7de8a94f49449249d74648326d17f073b25fd778e0d06d38cc738b96d1029f2b5c5895e2c90f8e35cb514e61f7c2e2b9024100ab4b0152c95ccd2492c60457699df27f35aa7183245d737bc6bb7d5e0731cd9c6cb7ba965cd8d4778ced651b13eae5532b89194ac7041863a8475769136271e5'
BOB_PUBLIC = '30819f300d06092a864886f70d010101050003818d0030818902818100b91c16d15e43750fda241ffc51d770b90cba48aa4594ad9ded911970df3f95044a9404407c637b38bbe21f802502b2307f2d62a69657365c86c5cc9c915b2a9e27e1ee3951d18ec8201cb48362d25536d70919ee219a118ad3c9c683f340db28dd39bfcad00939f2d39c566bd0e7417aab85463f89ef4c2d2816789a35e199830203010001'

ALICE_PRIVATE = '3082025c02010002818100d91cc6d91afa9841b1dedd78956b07c47b90c93da6d4a89b9cc669073da486059909086b7aa843ad9ba1d91ab0275c31c7fa0e2d17d9fd02cd7966e5c44d28b05a2f580154ba320d66d511037dcd8ddcb7f6d9111643a8175c787fcf4c990655ac1518710742fdd52a5df3addc7f90df62784310f3b6a3b93a6ba613a8f577fb020301000102818015e24a81755b34aaa130fb7632956465dfd09dc0359c878191415c87cacfabb9f7b820884e323f5ec9ea5140593e211306d0591fc9762daf06780a064c8d91caae85b59dc49b033ed3a6b4bb4d13efec533fd4bb005c0968d806d2611f570aec0cc4df182744b394a7674ad23e3723417c9d6efb95b5a88ecfc47b5a763453bd024100dd736d21bd61bba49aff12c4cfd74fb13857b4a3482d2f84ad4b0ca9b68bd2d3f9814adae0e8d5de16643ca3ba07e8bd13c7ce5ae661be6c1bc52cd119544d7f024100fafc133fc4e3babea3b7da940c599b6b9c162b1b85690b66f5b23e23f680c11d816d8a066afd8f67787a85f9e394d3926edeec969be5941675427db8070b4b85024010ff18f32bfbe25101ec6dde592d675a6cbe9e88a1b3862022c4cdd600c2be8db26aaffa18a506352376d208a6f09076629c454448c65bbd246c7fc214b599b502406f399482370bc0af493869da201af9c0577c8f7ff3c05878393bd343f6b29a622c00522183fa78399f6f94bde7f80546a8718c213657282847b0beabf61b304d024100afffef7881c9dfca8a3039ee5c96560752db3ddc854e18204f688ffcbcc9d9c990461bff385e2f46c44f5039ac2b5b6624f56fa0266173214da5150d4398a645'
ALICE_PUBLIC = '30819f300d06092a864886f70d010101050003818d0030818902818100d91cc6d91afa9841b1dedd78956b07c47b90c93da6d4a89b9cc669073da486059909086b7aa843ad9ba1d91ab0275c31c7fa0e2d17d9fd02cd7966e5c44d28b05a2f580154ba320d66d511037dcd8ddcb7f6d9111643a8175c787fcf4c990655ac1518710742fdd52a5df3addc7f90df62784310f3b6a3b93a6ba613a8f577fb0203010001'

SIMON_PRIVATE = '3082025c02010002818100a14fc6e54b8cea3e80b0b5067c1e862f618164ae2acc717dee30b1fd241a5d42b29f6d53af68898223ed11a433cf19bc98916842800c598c70a1fd59f80c1e04ea48f01ed4fb607abad8c92f4eff56d0a2e0fa781b13c6b604cb171b559ea05ac63eec8b01bed74c0212c1775d3471a531a593b57bd1dd9ba0acfc8c6b0ef26d0203010001028180195756881bfbc9aac2fdbf9a82b22ae3539e87aa02c8364611bead9f7665fbe3a7fafaaa4c62904395103f96bb9adbd0b0691b6763054da60de5accecef45c5caa6afb4c98bae763784863f26e386233638ec21e85b901d98a6349d337069c1388b45c56c5ae070f1a79d9febe161851ec920070950dc2e6cca695a114aeddd3024100c3c8a5f96bd23c65b7a8552709f5b3ea5dadea527aa8a1ff6db8b3d262dc2eee8fa5601acd3b55eb5e0adafb7cff86e5720b3ee416e7e706354ae99bc6aa09c3024100d2ece872dd814f63556c0cac072717562b7c332347e2981c91a7cc3755c09ce88eacd16c70056b97a11c3da589153db2eee2cd008064d5fbdce8803b24a0200f0240325e0034f684137da78deaba2c59c57b59b6503dffc83a44d81958499b9d4185a5f6c98e9b95d438c4ecce013cdb0ffd1f25bd7c3858589ac4430d6e41e1a4b9024100a3871d2880e7121f9748b00267813d2c8786413767321c7079d4b815669c708a34a373b2389f5b2d31b16d71fb77c66005a93cfad89054fe71e4a816326d1aad0240411a54e3da17375ff25d9ff7f1fb4a69af6fec8af216be2927b54b998b08c0d97c5a92610535176594d033e495b72de3a449285c3d47a7e89ca71b0c19c1c15b'
SIMON_PUBLIC = '30819f300d06092a864886f70d010101050003818d0030818902818100a14fc6e54b8cea3e80b0b5067c1e862f618164ae2acc717dee30b1fd241a5d42b29f6d53af68898223ed11a433cf19bc98916842800c598c70a1fd59f80c1e04ea48f01ed4fb607abad8c92f4eff56d0a2e0fa781b13c6b604cb171b559ea05ac63eec8b01bed74c0212c1775d3471a531a593b57bd1dd9ba0acfc8c6b0ef26d0203010001'

@pytest.fixture
def test_blockchain():
    test_blockchain = BlockChain(SIMON_PUBLIC, './tests/blockchain.bin')
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

def test_mine_block(test_blockchain):
    test_blockchain.mine_block()
    test_blockchain.add_transaction(BOB_PUBLIC, SIMON_PUBLIC, amount=3.4)
    test_blockchain.add_transaction(ALICE_PUBLIC, SIMON_PUBLIC, amount=3.6)
    test_blockchain.mine_block()
    assert "{'index': 0" in repr(test_blockchain.view_blockchain()[0])
    assert "{'index': 1" in repr(test_blockchain.view_blockchain()[1])
    assert "{'index': 2" in repr(test_blockchain.view_blockchain()[2])
    assert isinstance(test_blockchain.view_blockchain()[0], Block)
    assert isinstance(test_blockchain.view_blockchain()[1], Block)
    assert isinstance(test_blockchain.view_blockchain()[2], Block)

def test_clear_open_transactions_after_mining(test_blockchain):
    assert test_blockchain.view_open_transactions() == []

def test_mining_block_adds_reward(test_blockchain):
    test_blockchain.mine_block()
    test_blockchain.mine_block()
    assert test_blockchain.get_balance() == 20

def test_cannot_send_if_no_balance(test_blockchain):
    test_blockchain.add_transaction(BOB_PUBLIC, SIMON_PUBLIC, amount=3.4)
    test_blockchain.add_transaction(ALICE_PUBLIC, SIMON_PUBLIC, amount=3.6)
    test_blockchain.mine_block()
    assert not BOB_PUBLIC in repr(test_blockchain.view_blockchain())
    assert not ALICE_PUBLIC in repr(test_blockchain.view_blockchain())




# Need to mock this test with hardcoded timestamps as time stamps are changing
# def test_proof_of_work(test_blockchain):
#     test_blockchain.add_transaction('Bob', amount=3.4)
#     test_blockchain.add_transaction('Alice', amount=3.6)
#     test_blockchain.mine_block()
#     assert test_blockchain.proof_of_work() == 348

def test_create_file(test_blockchain):
    test_blockchain.mine_block()
    with open(test_blockchain.file_location, mode='rb') as file_line:
        file_content = loads(file_line.read())
    assert file_content['ot'] == []
    assert "{'index': 0" in repr(file_content['chain'][0])
    assert "{'index': 1" in repr(file_content['chain'][1])
    assert isinstance(file_content['chain'][0], Block)
    assert isinstance(file_content['chain'][1], Block)

# def test_load_data_on_startup
