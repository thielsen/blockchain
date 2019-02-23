from collections import OrderedDict

class Transaction:

    def __init__(self, sender, recipient, signature, amount):
        self.sender = sender
        self.recipient = recipient
        self.signature = signature
        self.amount = amount

    def __repr__(self):
        return 'Sender: {}, Recipient: {}, Amount: {}'.format(self.sender, self.recipient, self.amount)

    def to_ordered_dict(self):
        return OrderedDict([('sender', self.sender), ('recipient', self.recipient), ('amount', self.amount)])
        