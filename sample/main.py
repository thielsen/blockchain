from blockchain import add_transaction
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

while True:
    print('Choose')
    print('1. Add a transaction')
    print('2. View blockchain')
    print('0. Quit')
    user_choice = get_user_choice()
    if user_choice == 1:
        tx_amount = get_transaction_value()
        add_transaction (tx_amount, get_last_blockchain_value())
    elif user_choice == 2:
        print_blockchain_element()
    elif user_choice == 0:
        break
    else:
        print('Input invalid')
print('Done')
