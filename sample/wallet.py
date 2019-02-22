from Crypto.PublicKey import RSA
import Crypto.Random
import binascii
import pytest

class Wallet:

    def __init__(self):
        self.private_key = None
        self.public_key = None

    def create_keys(self):
        private_key, public_key = self.generate_keys()
        self.private_key = private_key
        self.public_key = public_key
        with open('wallet.txt', mode='w') as f:
            f.write(self.private_key)
            f.write('\n')
            f.write(self.public_key)
    
    def load_keys(self):
        pass

    def generate_keys(self):
        private_key = RSA.generate(1024, Crypto.Random.new().read)
        public_key = private_key.publickey()
        return (binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii'), binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii'))