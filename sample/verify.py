
import hash_utilities

class Verify:
    
    @classmethod
    def verify_chain(cls, blockchain):
        for (index, block) in enumerate(blockchain):
            if index == 0:
                continue
            if block.previous_hash != hash_utilities.hash_block(blockchain[index -1]):
                return False
            if not cls.valid_proof(block.transactions[:-1], block.previous_hash, block.proof):
                print('Proof of work invalid')
                return False
        return True

    @staticmethod
    def verify_transaction(transaction, get_balance):
        sender_balance = get_balance()
    # Make return sender_balance >= trasaction.amount?
        if sender_balance >= transaction.amount:
            return True
        else:
            return False

    @classmethod   
    def verify_transactions(cls, open_transactions, get_balance):
        return all([cls.verify_transaction(tx, get_balance) for tx in open_transactions])

    @staticmethod
    def valid_proof(transactions, last_hash, proof):
        guess = (str([tx.to_ordered_dict() for tx in transactions]) + str(last_hash) +str(proof)).encode()
        guess_hash = hash_utilities.hash_string_256(guess)
        return guess_hash[0:2] == '00'
