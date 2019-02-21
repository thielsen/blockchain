from blockchain import add_transaction
from blockchain import get_last_blockchain_value
from blockchain import blockchain
from blockchain import verify_chain
from blockchain import mine_block


def get_transaction_value():
    tx_recipient = input('Enter recipient: ')
    tx_amount = float(input('Transaction amount: '))
    return (tx_recipient, tx_amount)

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
    print('2. Mine a new block')
    print('3. View blockchain')
    print('4. Manipulate blockchain')
    print('0. Quit')
    user_choice = get_user_choice()
    if user_choice == 1:
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction (recipient, amount=amount)
    elif user_choice == 2:
        mine_block()
    elif user_choice == 3:
        print_blockchain_element()
    elif user_choice == 4:
        if len(blockchain) >= 1:
            blockchain[0] = {'previous_hash': '', 
                             'index': 0,
                             'transactions': [{'sender': 'poorfool', 'recipient': 'badactor', 'amount': '1000'}]
}
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
