from time import time


class Block:

    def __init__(self,
                 index,
                 previous_hash,
                 transactions,
                 proof,
                 timestamp=time()):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.proof = proof
        self.timestamp = timestamp

    def __repr__(self):
        return str(self.__dict__)
