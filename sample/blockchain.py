from functools import reduce
from hashlib import sha256
from json import dumps
class BlockChain():
    
    def __init__(self):
        self.MINING_REWARD = 10
        self.GENESIS_BLOCK = {'previous_hash': '', 
                              'index': 0,
                              'transactions': []
}
        self.blockchain = [self.GENESIS_BLOCK]
        self.open_transactions = []
        self.owner = 'Simon'
        self.participants = {self.owner}

    def add_transaction(self, recipient, sender=None, amount=1.0):
        if sender is None:
            sender = self.owner
        transaction = {'recipient': recipient,
                    'sender': sender, 
                    'amount': amount}
        if self.verify_transaction(transaction):
            self.open_transactions.append(transaction)
            self.participants.add(sender)
            self.participants.add(recipient)
            return True
        return False


    def mine_block(self):
        last_block = self.blockchain[-1]
        hashed_block = self.hash_block(last_block)
        reward_transaction = {'sender': 'MINED',
                              'recipient': self.owner,
                              'amount': self.MINING_REWARD
        }
        copied_transactions = self.open_transactions[:]
        copied_transactions.append(reward_transaction)
        block = {'previous_hash': hashed_block, 
                'index': len(self.blockchain),
                'transactions': copied_transactions}
        self.blockchain.append(block)
        self.open_transactions = []


    def get_last_blockchain_value():
        if len(blockchain) < 1:
            return None
        return blockchain[-1]

    def hash_block(self, block):
        return sha256(dumps(block).encode()).hexdigest()

    def verify_chain(self):
        for (index, block) in enumerate(self.blockchain):
            if index == 0:
                continue
            if block['previous_hash'] != self.hash_block(self.blockchain[index -1]):
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
