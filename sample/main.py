from blockchain import add_value
from blockchain import get_last_blockchain_value
from blockchain import blockchain

def get_transaction_value():
    return float(input('Transaction amount:'))

def get_user_choice():
    return int(input(' Your Choice: '))

def print_blockchain_element():
    for block in blockchain:
        print('Outputting Block')
        print(block)

tx_amount = get_transaction_value()
add_value (tx_amount)


while True:
    print('Choose')
    print('1. Add a transaction')
    print('2. View blockchain')
    user_choice = get_user_choice()
    if user_choice == 1:
        tx_amount = get_transaction_value()
        add_value (tx_amount, get_last_blockchain_value())
    else:
        print_blockchain_element()
print('Done')
