from functools import reduce
from collections import OrderedDict
from json import dumps, loads
import os
import pickle

import hash_utilities
from block import Block
from transaction import Transaction
from verify import Verify
class BlockChain():
    
    def __init__(self, file_location='./blockchain.bin'):
        self.MINING_REWARD = 10
        self.GENESIS_BLOCK = Block(0, '', [], 0, 0)
        self.blockchain = []
        self.open_transactions = []
        self.owner = 'Simon'
        self.participants = {self.owner}
        self.file_location = file_location
        self.load_data()
        self.verify = Verify()

    def save_data(self):
        try:
            with open(self.file_location, mode='wb') as f:
                save_data = {'chain': self.blockchain, 'ot': self.open_transactions}
                f.write(pickle.dumps(save_data))
        except IOError:
            ('Save error')

    def load_data(self):
        try:
            with open(self.file_location, mode='rb') as f:
                file_content = pickle.loads(f.read())
                self.blockchain = file_content['chain']
                self.open_transactions = file_content['ot']
        except IOError:
            print('Existing blockchain not found. Initializing...')
            self.blockchain = [self.GENESIS_BLOCK]
            self.open_transactions = []

    def add_transaction(self, recipient, sender=None, amount=1.0):
        if sender is None:
            sender = self.owner
        transaction = Transaction(sender, recipient, amount)
        # transaction = OrderedDict([('sender', sender), ('recipient', recipient), ('amount', amount)])
        if self.verify.verify_transaction(transaction, self.get_balance):
            self.open_transactions.append(transaction)
            self.participants.add(sender)
            self.participants.add(recipient)
            self.save_data()
            return True
        return False

    def mine_block(self):
        last_block = self.blockchain[-1]
        hashed_block = hash_utilities.hash_block(last_block)
        proof = self.proof_of_work()
        reward_transaction = Transaction('MINED', self.owner, self.MINING_REWARD)
        # reward_transaction = OrderedDict(
            # [('sender', 'MINED'), ('recipient', self.owner), ('amount', self.MINING_REWARD)]) 
        copied_transactions = self.open_transactions[:]
        copied_transactions.append(reward_transaction)
        block = Block(len(self.blockchain), hashed_block, copied_transactions, proof)
        self.blockchain.append(block)
        self.open_transactions = []
        self.save_data()
        
    def get_last_blockchain_value(self):
        if len(self.blockchain) < 1:
            return None
        return self.blockchain[-1]

    def get_balance(self, participant):
        tx_sender = [[tx.amount for tx in block.transactions if tx.sender == participant] for block in self.blockchain]
        open_tx_sender = [tx.amount for tx in self.open_transactions if tx.sender == participant]
        tx_sender.append(open_tx_sender)
        amount_sent = reduce(lambda x, y: x+sum(y), tx_sender, 0)
        tx_recipient = [[tx.amount for tx in block.transactions if tx.recipient == participant] for block in self.blockchain]
        amount_received = reduce(lambda x, y: x+sum(y), tx_recipient, 0)
        return amount_received - amount_sent

    def proof_of_work(self):
        last_block = self.blockchain[-1]
        last_hash = hash_utilities.hash_block(last_block)
        proof = 0
        while not self.verify.valid_proof(self.open_transactions, last_hash, proof):
            proof += 1
        return proof
        