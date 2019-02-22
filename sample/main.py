# from blockchain import add_transaction
# from blockchain import get_last_blockchain_value
# from blockchain import blockchain
# from blockchain import verify_chain
# from blockchain import mine_block
# from blockchain import participants
# from blockchain import open_transactions
from blockchain import *
from verify import Verify

my_blockchain = BlockChain()
verify = Verify()

def get_transaction_value():
    tx_recipient = input('Enter recipient: ')
    tx_amount = float(input('Transaction amount: '))
    return (tx_recipient, tx_amount)

def get_user_choice():
    return int(input(' Your Choice: '))

def print_blockchain_element():
    for block in my_blockchain.blockchain:
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
    print('5. Output participants')
    print('6. Verify all transactions in queue')
    print('0. Quit')
    user_choice = get_user_choice()
    if user_choice == 1:
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        if my_blockchain.add_transaction (recipient, amount=amount):
            print('Transaction added')
        else:
            print('Transaction failed')
    elif user_choice == 2:
        my_blockchain.mine_block()
    elif user_choice == 3:
        print_blockchain_element()
    elif user_choice == 5:
        print(my_blockchain.participants)
    elif user_choice == 6:
        if verify.verify_transactions(my_blockchain.open_transactions, my_blockchain.get_balance):
            print('Verified')
        else:
            print('Invalid transactions')
    elif user_choice == 0:
        waiting_for_input = False
    else:
        print('Input invalid')
    if not verify.verify_chain(my_blockchain.blockchain):
        print('Invalid chain')
        waiting_for_input = False
    print('Balance of {}: {:6.2f}'.format('Simon', my_blockchain.get_balance('Simon')))
else:
    print('User left')

    
print('Done')
