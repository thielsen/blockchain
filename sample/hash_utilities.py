from hashlib import sha256
from json import dumps

def hash_string_256(string):
    return sha256(string).hexdigest()

def hash_block(block):
    dictionary_block = block.__dict__.copy()
    dictionary_block['transactions'] = [tx.to_ordered_dict() for
                                        tx in dictionary_block['transactions']]
    return hash_string_256(dumps(dictionary_block, sort_keys=True).encode())
