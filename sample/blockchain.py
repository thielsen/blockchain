genesis_block = {'previous_hash': '', 
                 'index': 0,
                 'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Simon'

def add_transaction(recipient, sender=owner, amount=1.0):
    transaction = {'recipient': recipient,
                   'sender': sender, 
                   'amount': amount}
    open_transactions.append(transaction)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    block = {'previous_hash': 'XYZ', 
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
    is_valid = True
    for block_index in range(1, len(blockchain)):
        if blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
    return is_valid

