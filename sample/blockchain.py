from functools import reduce
from pickle import loads, dumps

from sample.crypto_utilities import hash_block
from sample.block import Block
from sample.transaction import Transaction
from sample.verify import Verify
from sample.wallet import Wallet
class BlockChain():

    MINING_REWARD = 10
    GENESIS_BLOCK = Block(0, '', [], 0, 0)

    def __init__(self, node_id, file_location='./blockchain.bin'):
        self.__blockchain = [BlockChain.GENESIS_BLOCK]
        self.__open_transactions = []
        self.file_location = file_location
        self.load_data()
        self.node = node_id

    def view_blockchain(self):
        return self.__blockchain[:]

    def view_open_transactions(self):
        return self.__open_transactions[:]

    def save_data(self):
        try:
            with open(self.file_location, mode='wb') as file_line:
                save_data = {'chain': self.__blockchain, 'ot': self.__open_transactions}
                file_line.write(dumps(save_data))
        except IOError:
            print('Save error')

    def load_data(self):
        try:
            with open(self.file_location, mode='rb') as file_line:
                file_content = loads(file_line.read())
                self.__blockchain = file_content['chain']
                self.__open_transactions = file_content['ot']
        except IOError:
            print('Existing blockchain not found. Initializing...')

    def add_transaction(self, recipient, signature, sender=None, amount=1.0):
        if sender is None:
            sender = self.node
        if self.node is None:
            return False
        transaction = Transaction(sender, recipient, signature, amount)
        if Verify.verify_transaction(transaction, self.get_balance):
            self.__open_transactions.append(transaction)
            self.save_data()
            return True
        return False

    def mine_block(self):
        if self.node is None:
            return None
        last_block = self.__blockchain[-1]
        hashed_block = hash_block(last_block)
        proof = self.proof_of_work()
        reward_transaction = Transaction('MINED', self.node, '', BlockChain.MINING_REWARD)
        copied_transactions = self.__open_transactions[:]
        for transaction in copied_transactions:
            if not Wallet.verify_transaction(transaction):
                return None
        copied_transactions.append(reward_transaction)
        block = Block(len(self.__blockchain), hashed_block, copied_transactions, proof)
        self.__blockchain.append(block)
        self.__open_transactions = []
        self.save_data()
        return block

    def get_balance(self):
        if self.node == None:
            return None
        tx_sender = [
            [tx.amount for tx in block.transactions if tx.sender == self.node]
            for block in self.__blockchain
            ]
        open_tx_sender = [tx.amount for tx in self.__open_transactions if tx.sender == self.node]
        tx_sender.append(open_tx_sender)
        amount_sent = reduce(lambda x, y: x+sum(y), tx_sender, 0)
        tx_recipient = [
            [tx.amount for tx in block.transactions if tx.recipient == self.node]
            for block in self.__blockchain
            ]
        amount_received = reduce(lambda x, y: x+sum(y), tx_recipient, 0)
        return amount_received - amount_sent

    def proof_of_work(self):
        last_block = self.__blockchain[-1]
        last_hash = hash_block(last_block)
        proof = 0
        while not Verify.valid_proof(self.__open_transactions, last_hash, proof):
            proof += 1
        return proof
        