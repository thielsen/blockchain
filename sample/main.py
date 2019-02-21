from blockchain import add_value
from blockchain import get_last_blockchain_value
from blockchain import blockchain

def get_user_input():
    return float(input('Transaction amount:'))

tx_amount = get_user_input()
add_value (tx_amount)

tx_amount = get_user_input()
add_value (tx_amount, get_last_blockchain_value())

tx_amount = get_user_input()
add_value (tx_amount, get_last_blockchain_value())

print(blockchain)
