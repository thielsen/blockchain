import functools
from sample.blockchain import *




test_blockchain = BlockChain()
data = False
x = 0
while data != True:
    data = test_blockchain.valid_proof({'index': 1, 'previous_hash': 'b2242851cf5e7216d0bbb01ad9b6659bbca55f43c9ac3e63d0fac318b579c253', 'proof': 91, 'transactions': [{'amount': 10, 'recipient': 'Simon', 'sender': 'MINED'}]}, 'bb6818b2c40aff99aced646e148ee46e8f52761863875b76f8c45bd9b48484dd', x)
    print(data)
    # print(x)
    x = x + 1  
print(x)

  # def proof_of_work(self):
  #       last_block = self.blockchain[-1]
  #       last_hash = self.hash_block(last_block)
  #       proof = 0
  #       while self.valid_proof(self.open_transactions, last_hash, proof):
  #           proof += 1
  #       return proof

# test_blockchain = BlockChain()
# test_blockchain.add_transaction('Bob', amount=3.4)
# test_blockchain.add_transaction('Alice', amount=3.6)
# test_blockchain.mine_block()
# print(test_blockchain.proof_of_work())

# # output = test_blockchain.valid_proof({'previous_hash': 'fdcd010164e24fe2247e9c6b20e211ab96c0cb7b3ad2da9f3e5feaac47ecc4d1', 'index': 1, 'transactions': [{'sender': 'MINED', 'recipient': 'Simon', 'amount': 10}]} , 'bf8953d506d8467b96da1a2b8b335510ad16be3e45be8e36aacb19ef3bdbb277', 0)
# # print(output)




  # def load_data(self):
        # with open(self.file_location, mode='r') as f:
            # file_content = f.readlines()
            # self.blockchain = loads(file_content[0][:-1])
            # updated_blockchain =[]
            # for block in blockchain:
            #     updated_block = {'previous_hash': block['previous_hash'], 'index': block['index'], 'proof': block['proof'], 'transactions': [OrderedDict([('sender', tx['sender']), ('recipient', tx['recipient']), ('amount', tx['amount'])]) for tx in block['transactions']]}
            #     updated_blockchain.append(updated_block)
            # self.blockchain = updated_blockchain
            # self.open_transactions = loads(file_content[1])