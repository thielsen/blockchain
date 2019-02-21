import functools
from sample.blockchain import *




test_blockchain = BlockChain()
data = False
x = 0
while data != True:
    data = test_blockchain.valid_proof([{'amount': 10.0, 'recipient': 'Bob', 'sender': 'Simon'}] , 'b2242851cf5e7216d0bbb01ad9b6659bbca55f43c9ac3e63d0fac318b579c253', x)
    print(data)
    # print(x)
    x = x + 1  
print(x)



