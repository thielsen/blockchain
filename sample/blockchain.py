from functools import reduce
from collections import OrderedDict
from json import dumps, loads
import os

import hash_utilities
class BlockChain():
    
    def __init__(self):
        self.MINING_REWARD = 10
        self.GENESIS_BLOCK = {'previous_hash': '', 
                              'index': 0,
                              'transactions': [],
                              'proof': 0
}
        self.blockchain = [self.GENESIS_BLOCK]
        self.open_transactions = []
        self.owner = 'Simon'
        self.participants = {self.owner}
        self.file_location = './blockchain.txt'
        if os.path.isfile(self.file_location):
            self.load_data()


    def save_data(self):
        with open(self.file_location, mode='w') as f:
            f.write(dumps(self.blockchain))
            f.write('\n')
            f.write(dumps(self.open_transactions))

    def load_data(self):
        with open(self.file_location, mode='r') as f:
            file_content = f.readlines()
            self.blockchain = loads(file_content[0])
            self.open_transactions = loads(file_content[1])

    def add_transaction(self, recipient, sender=None, amount=1.0):
        if sender is None:
            sender = self.owner
        transaction = OrderedDict(
            [('sender', sender), ('recipient', recipient), ('amount', amount)])
        if self.verify_transaction(transaction):
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
        reward_transaction = OrderedDict(
            [('sender', 'MINED'), ('recipient', self.owner), ('amount', self.MINING_REWARD)])
        copied_transactions = self.open_transactions[:]
        copied_transactions.append(reward_transaction)
        block = {'previous_hash': hashed_block, 
                'index': len(self.blockchain),
                'transactions': copied_transactions,
                'proof': proof}
        self.blockchain.append(block)
        self.save_data()
        self.open_transactions = []
        

    def get_last_blockchain_value():
        if len(blockchain) < 1:
            return None
        return blockchain[-1]

    def verify_chain(self):
        for (index, block) in enumerate(self.blockchain):
            if index == 0:
                continue
            if block['previous_hash'] != hash_utilities.hash_block(self.blockchain[index -1]):
                return False
            if not self.valid_proof(block['transactions'][:-1], block['previous_hash'], block['proof']):
                print('Proof of work invalid')
                return False
        return True

    def get_balance(self, participant):
        tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in self.blockchain]
        open_tx_sender = [tx['amount'] for tx in self.open_transactions if tx['sender'] == participant]
        tx_sender.append(open_tx_sender)
        amount_sent = reduce(lambda x, y: x+sum(y), tx_sender, 0)
        tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in self.blockchain]
        amount_received = reduce(lambda x, y: x+sum(y), tx_recipient, 0)
        return amount_received - amount_sent

    def verify_transaction(self, transaction):
        sender_balance = self.get_balance(transaction['sender'])
        if sender_balance >= transaction['amount']:
            return True
        else:
            return False

    def verify_transactions(self):
        return all([self.verify_transaction(tx) for tx in self.open_transactions])

    def valid_proof(self, transactions, last_hash, proof):
        guess = (str(transactions) + str(last_hash) +str(proof)).encode()
        guess_hash = hash_utilities.hash_string_256(guess)
        return guess_hash[0:2] == '00'

    def proof_of_work(self):
        last_block = self.blockchain[-1]
        last_hash = hash_utilities.hash_block(last_block)
        proof = 0
        while not self.valid_proof(self.open_transactions, last_hash, proof):
            proof += 1
        return proof
        