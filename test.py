import functools

testblock = [{'index': 0, 'previous_hash': '', 'transactions': []}, {'index': 1, 'previous_hash': '0--[]', 'transactions': [{'amount': 10, 'recipient': 'Simon', 'sender': 'MINED'}]}, {'index': 2, 'previous_hash': "1-0--[]-[{'amount': 10, 'recipient': 'Simon', 'sender': 'MINED'}]", 'transactions': [{'amount': 3.4, 'recipient': 'Bob', 'sender': 'Simon'}, {'amount': 3.6, 'recipient': 'Alice', 'sender': 'Simon'}, {'amount': 10, 'recipient': 'Simon', 'sender': 'MINED'}]}]
tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == 'Simon'] for block in testblock]

output = functools.reduce(lambda x, y: x+y, functools.reduce(lambda x, y: x+y, tx_sender), 0)
# output = functools.reduce(lambda x, y: x+y, tx_sender)
# amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + reduce(lambda x, y: x+y, tx_amt) if len(tx_amt) > 0 else 0, tx_sender, 0)

# print(tx_sender)
print(output)
