from flask import Flask, jsonify
from flask_cors import CORS
from sample.wallet import Wallet
from sample.blockchain import BlockChain

wallet = Wallet()
blockchain = BlockChain(wallet.public_key)


def create_app(config=None):
    app = Flask(__name__)
    CORS(app)

    @app.route('/wallet', methods=['POST'])
    def create_keys():
        wallet.create_keys()
        if wallet.save_keys():
            response =  {
                'public_key': wallet.public_key,
                'private_key': wallet.private_key,
                'balance': get_balance()
            }
            return jsonify(response), 201
        else:
            response = {
                'message': 'Failed'
            }
            return jsonify(response), 500

    @app.route('/wallet', methods=['GET'])
    def load_keys():
        if wallet.load_keys():
            response =  {
                'public_key': wallet.public_key,
                'private_key': wallet.private_key,
                'balance': get_balance()
            }
            return jsonify(response), 201
        else:
            response = {
                'message': 'Failed'
            }
            return jsonify(response), 500
    
    @app.route('/balance', methods=['GET'])
    def get_balance():
        balance = blockchain.get_balance()
        if balance is not None:
            response = {
                'message': 'Success',
                'balance': balance
            }
            return jsonify(response), 200
        else:
            response = {
                'message': 'failed',
                'wallet': wallet.public_key is not None
            }
            return jsonify(response), 500

    @app.route('/', methods=['GET'])
    def get_ui():
        return 'Working'

    @app.route('/blockchain', methods=['GET'])
    def get_chain():
        chain = blockchain.view_blockchain()
        dict_chain = [block.__dict__.copy() for block in chain]
        for dict_block in dict_chain:
            dict_block['transactions'] = [tx.__dict__ for tx in dict_block['transactions']]
        return jsonify(dict_chain), 200

    @app.route('/mine', methods=['POST'])
    def mine_block():
        block = blockchain.mine_block()
        if block is not None:
            dict_block = block.__dict__.copy()
            dict_block['transactions'] = [tx.__dict__ for tx in dict_block['transactions']]
            success_response = {
                'message': 'Mining succeeded',
                'block': dict_block,
                'balance': blockchain.get_balance()
            }
            return jsonify(success_response), 201
        else:
            error_response = {
                'message': 'Mining failed',
                'wallet_available': wallet.public_key is not None
            }
            return jsonify(error_response), 500

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=4000)
