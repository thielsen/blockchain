from sample.blockchain import BlockChain
from sample.verify import Verify
from sample.wallet import Wallet


class Node:

    def __init__(self, wallet=None, blockchain=None):
        if wallet is None:
            wallet = Wallet()
            wallet.create_keys()
        self.wallet = wallet
        if blockchain is None:
            blockchain = BlockChain(self.wallet.public_key)
        self.blockchain = blockchain

    def print_menu(self):
        print('Choose')
        print('1. Add a transaction')
        print('2. Mine a new block')
        print('3. View blockchain')
        print('4. Verify all transactions in queue')
        print('5. Create wallet')
        print('6. Load wallet')
        print('7. Save keys')
        print('0. Quit')

    def listen_for_input(self):
        waiting_for_input = True
        while waiting_for_input:
            self.print_menu()
            user_choice = self.get_user_choice()
            if user_choice == 1:
                tx_data = self.get_transaction_value()
                if self.submit_transaction(tx_data):
                    print('Transaction added')
                else:
                    print('Transaction failed')
            elif user_choice == 2:
                if not self.blockchain.mine_block():
                    print('Mining failed')
            elif user_choice == 3:
                self.print_blockchain_element()
            elif user_choice == 4:
                if Verify.verify_transactions(self.blockchain.view_open_transactions(),
                                              self.blockchain.get_balance):
                    print('Verified')
                else:
                    print('Invalid transactions')
            elif user_choice == 5:
                self.wallet.create_keys()
                self.blockchain = BlockChain(self.wallet.public_key)
            elif user_choice == 6:
                self.wallet.load_keys()
                self.blockchain = BlockChain(self.wallet.public_key)
            elif user_choice == 7:
                self.wallet.save_keys()
            elif user_choice == 0:
                waiting_for_input = False
            else:
                print('Input invalid')
            if not Verify.verify_chain(self.blockchain.view_blockchain()):
                print('Invalid chain')
                waiting_for_input = False
            print('Balance of {}: {:6.2f}'.format(self.wallet.public_key,
                                                  self.blockchain.get_balance()))
            break
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
        for block in self.blockchain.view_blockchain():
            print('Outputting Block')
            print(block)
            break
        else:
            print('-' * 20)

    def submit_transaction(self, tx_data):
        recipient, amount = tx_data
        signature = self.wallet.sign_transaction(self.wallet.public_key, recipient, amount)
        return self.blockchain.add_transaction(recipient,
                                               signature,
                                               self.wallet.public_key,
                                               amount=amount)
