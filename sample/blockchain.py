
blockchain = []

def add_transaction(transaction_amount, last_transaction=[1]):
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])

def get_last_blockchain_value():
    if len(blockchain) < 1:
      return None
    return blockchain[-1]

def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        print('block 0:')
        print(block[0])
        print('block -1:')
        print(blockchain[block_index -1])
        if block_index == 0:
            block_index += 1
            continue
        if block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid

