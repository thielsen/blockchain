import functools
from sample.blockchain import *




# test_blockchain = BlockChain()
# data = False
# x = 0
# while data != True:
#     data = test_blockchain.valid_proof([{'amount': 10.0, 'recipient': 'Bob', 'sender': 'Simon'}] , 'b2242851cf5e7216d0bbb01ad9b6659bbca55f43c9ac3e63d0fac318b579c253', x)
#     print(data)
#     # print(x)
#     x = x + 1  
# print(x)

  # def proof_of_work(self):
  #       last_block = self.blockchain[-1]
  #       last_hash = self.hash_block(last_block)
  #       proof = 0
  #       while self.valid_proof(self.open_transactions, last_hash, proof):
  #           proof += 1
  #       return proof

test_blockchain = BlockChain()
test_blockchain.add_transaction('Bob', amount=3.4)
test_blockchain.add_transaction('Alice', amount=3.6)
test_blockchain.mine_block()
print(test_blockchain.proof_of_work())

# output = test_blockchain.valid_proof({'previous_hash': 'fdcd010164e24fe2247e9c6b20e211ab96c0cb7b3ad2da9f3e5feaac47ecc4d1', 'index': 1, 'transactions': [{'sender': 'MINED', 'recipient': 'Simon', 'amount': 10}]} , 'bf8953d506d8467b96da1a2b8b335510ad16be3e45be8e36aacb19ef3bdbb277', 0)
# print(output)