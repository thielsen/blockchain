genesis_block = {'previous_hash': '', 
                 'index': 0,
                 'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Simon'
participants = {owner}

def add_transaction(recipient, sender=owner, amount=1.0):
    transaction = {'recipient': recipient,
                   'sender': sender, 
                   'amount': amount}
    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)

def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    block = {'previous_hash': hashed_block, 
             'index': len(blockchain),
             'transactions': open_transactions}
    blockchain.append(block)
    
def get_last_blockchain_value():
    if len(blockchain) < 1:
      return None
    return blockchain[-1]

def hash_block(block):
    return '-'.join(str([block[key] for key in block]))

def verify_chain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index -1]):
            return False
        return True
