class BlockChain():
    
    def __init__(self):
        self.    genesis_block = {'previous_hash': '', 
                 'index': 0,
                 'transactions': []
}
        self.blockchain = [self.genesis_block]
        self.open_transactions = []
        self.owner = 'Simon'
        self.participants = {self.owner}

    def add_transaction(self, recipient, sender=None, amount=1.0):
        if sender is None:
            sender = self.owner
        transaction = {'recipient': recipient,
                    'sender': sender, 
                    'amount': amount}
        self.open_transactions.append(transaction)
        self.participants.add(sender)
        self.participants.add(recipient)

    def mine_block(self):
        last_block = self.blockchain[-1]
        hashed_block = self.hash_block(last_block)
        block = {'previous_hash': hashed_block, 
                'index': len(self.blockchain),
                'transactions': self.open_transactions}
        self.blockchain.append(block)
        self.open_transactions = []


    def get_last_blockchain_value():
        if len(blockchain) < 1:
            return None
        return blockchain[-1]

    def hash_block(self, block):
        return '-'.join(str([block[key] for key in block]))

    def verify_chain(self):
        for (index, block) in enumerate(self.blockchain):
            if index == 0:
                continue
            if block['previous_hash'] != self.hash_block(self.blockchain[index -1]):
                return False
        return True
