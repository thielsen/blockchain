import pytest
# import capsys

from sample.node import Node
from sample.node import Wallet
from sample.blockchain import BlockChain

SIMON_PUBLIC = '30819f300d06092a864886f70d010101050003818d0030818902818100a14fc6e54b8cea3e80b0b5067c1e862f618164ae2acc717dee30b1fd241a5d42b29f6d53af68898223ed11a433cf19bc98916842800c598c70a1fd59f80c1e04ea48f01ed4fb607abad8c92f4eff56d0a2e0fa781b13c6b604cb171b559ea05ac63eec8b01bed74c0212c1775d3471a531a593b57bd1dd9ba0acfc8c6b0ef26d0203010001'

def test_print_menu(capsys):
    node = Node()
    node.print_menu()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == 'Choose\n1. Add a transaction\n2. Mine a new block\n3. View blockchain\n4. Verify all transactions in queue\n5. Create wallet\n6. Load wallet\n7. Save keys\n0. Quit'

def test_print_blockchain_element(capsys):
    wallet = Wallet('./test/alice_wallet.txt')
    blockchain = BlockChain(SIMON_PUBLIC, './tests/blockchain.bin')
    node = Node(wallet, blockchain)  
    print(node.__dict__)
    node.print_blockchain_element()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert ("{'index': 0, 'previous_hash': '', 'transactions': [], 'proof': 0, 'timestamp': 0}" in captured_stdout.strip())
