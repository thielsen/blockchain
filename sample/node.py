from uuid import uuid4

from blockchain import *
from verify import Verify

class Node:

    def __init__(self):
        self.owner = str(uuid4())
        self.blockchain = BlockChain(self.owner)

    def listen_for_input(self):
        waiting_for_input = True
        while waiting_for_input:
            print('Choose')
            print('1. Add a transaction')
            print('2. Mine a new block')
            print('3. View blockchain')
            print('4. Verify all transactions in queue')
            print('0. Quit')
            user_choice = self.get_user_choice()
            if user_choice == 1:
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data
                if self.blockchain.add_transaction (recipient, self.owner, amount=amount):
                    print('Transaction added')
                else:
                    print('Transaction failed')
            elif user_choice == 2:
                self.blockchain.mine_block()
            elif user_choice == 3:
                self.print_blockchain_element()
            elif user_choice == 4:
                if Verify.verify_transactions(self.blockchain.open_transactions, self.blockchain.get_balance):
                    print('Verified')
                else:
                    print('Invalid transactions')
            elif user_choice == 0:
                waiting_for_input = False
            else:
                print('Input invalid')
            if not Verify.verify_chain(self.blockchain.blockchain):
                print('Invalid chain')
                waiting_for_input = False
            print('Balance of {}: {:6.2f}'.format(self.owner, self.blockchain.get_balance()))
        else:
            print('User left')
        print('Done')

    def get_transaction_value(self):
        tx_recipient = input('Enter recipient: ')
        tx_amount = float(input('Transaction amount: '))
        return (tx_recipient, tx_amount)

    def get_user_choice(self):
        return int(input(' Your Choice: '))

    def print_blockchain_element(self):
        for block in self.blockchain.blockchain:
            print('Outputting Block')
            print(block)
        else:
            print('-' * 20)

node = Node()
node.listen_for_input()