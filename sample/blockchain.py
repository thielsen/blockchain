
blockchain = [[1]]

def add_value(transaction_amount):
    blockchain.append([get_last_blockchain_value(), transaction_amount])

def get_last_blockchain_value():
    return blockchain[-1]
