from sample.blockchain import BlockChain
from sample.wallet import Wallet


class Node:

    def __init__(self, wallet=None, blockchain=None):
        if wallet is None:
            wallet = Wallet()
            wallet.create_keys()
        self.wallet = wallet
        if blockchain is None:
            blockchain = BlockChain(self.wallet.public_key)
        self.blockchain = blockchain
