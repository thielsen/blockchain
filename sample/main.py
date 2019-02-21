from blockchain import add_transaction
from blockchain import get_last_blockchain_value
from blockchain import blockchain
from blockchain import verify_chain

def get_transaction_value():
    return float(input('Transaction amount:'))

def get_user_choice():
    return int(input(' Your Choice: '))

def print_blockchain_element():
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-' * 20)

waiting_for_input = True

while waiting_for_input:
    print('Choose')
    print('1. Add a transaction')
    print('2. View blockchain')
    print('3. Manipulate blockchain')
    print('0. Quit')
    user_choice = get_user_choice()
    if user_choice == 1:
        tx_amount = get_transaction_value()
        add_transaction (tx_amount, get_last_blockchain_value())
    elif user_choice == 2:
        print_blockchain_element()
    elif user_choice == 3:
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 0:
        waiting_for_input = False
    else:
        print('Input invalid')
    if not verify_chain():
        print('Invalid chain')
        waiting_for_input = False
else:
    print('User left')

    
print('Done')
