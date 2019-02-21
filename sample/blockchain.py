
blockchain = []

def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])

def get_last_blockchain_value():
    return blockchain[-1]
