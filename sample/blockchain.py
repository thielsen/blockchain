
blockchain = []

def add_transaction(transaction_amount, last_transaction=[1]):
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])

def get_last_blockchain_value():
    if len(blockchain) < 1:
      return None
    return blockchain[-1]
