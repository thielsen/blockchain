import binascii
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import Crypto.Random


class Wallet:

    def __init__(self, wallet_file='wallet.txt'):
        self.private_key = None
        self.public_key = None
        self.load_keys(wallet_file)

    def create_keys(self):
        private_key, public_key = self.generate_keys()
        self.private_key = private_key
        self.public_key = public_key

    def save_keys(self):
        if self.public_key is not None and self.private_key is not None:
            try:
                with open('wallet.txt', mode='w') as file_line:
                    file_line.write(self.private_key)
                    file_line.write('\n')
                    file_line.write(self.public_key)
                return True
            except IOError:
                print('Save error')
                return False
        else:
            print('No keys to save')

    def load_keys(self, wallet_file='wallet.txt'):
        try:
            with open(wallet_file, mode='r') as file_line:
                keys = file_line.readlines()
                self.private_key = keys[0][:-1]
                self.public_key = keys[1]
            return True
        except IOError:
            print('Keys not found..')
            return False

    def generate_keys(self):
        private_key = RSA.generate(1024, Crypto.Random.new().read)
        public_key = private_key.publickey()
        return (binascii.hexlify(private_key.exportKey(format='DER'))
                .decode('ascii'),
                binascii.hexlify(public_key.exportKey(format='DER'))
                .decode('ascii'))

    def sign_transaction(self, sender, recipient, amount):
        signer = PKCS1_v1_5.new(RSA.importKey
                                (binascii.unhexlify(self.private_key)))
        hash_to_sign = SHA256.new((str(sender) + str(recipient) + str(amount))
                                  .encode())
        signature = signer.sign(hash_to_sign)
        return binascii.hexlify(signature).decode()

    @staticmethod
    def verify_transaction(transaction):
        verifier = PKCS1_v1_5.new(RSA.importKey
                                  (binascii.unhexlify(transaction.sender)))
        hash_to_verify = SHA256.new((str(transaction.sender) +
                                     str(transaction.recipient) +
                                     str(transaction.amount)).encode())
        return verifier.verify(hash_to_verify,
                               binascii.unhexlify(transaction.signature))
