from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from sample.wallet import Wallet
from sample.blockchain import BlockChain

wallet = Wallet()
wallet.create_keys()
blockchain = BlockChain(wallet.public_key)


def create_app(config=None):
    app = Flask(__name__)
    CORS(app)

    def keys_file_response():
        response = {
            'public_key': wallet.public_key,
            'private_key': wallet.private_key,
            'balance': blockchain.get_balance()
            }
        return response

    @app.route('/peer', methods=['POST'])
    def add_peer():
        values = request.get_json()
        print(values)
        if not values:
            response = {
                'message': 'No data'
            }
            return jsonify(response), 400
        if 'peer' not in values:
            response = {
                'message': 'No peer'
            }
            return jsonify(response), 400
        peer = values['peer']
        blockchain.add_peer(peer)
        response = {
            'message': 'Peer added',
            'peers': blockchain.get_peers()
        }
        return jsonify(response), 201

    @app.route('/peer/<url>', methods=['DELETE'])
    def delete_peer(url):
        if url == '' or url is None:
            response = {
                'message': 'Peer not found'
            }
            return jsonify(response), 400
        blockchain.delete_peer(url)
        response = {
            'message': 'Deleted',
            'all_peers': blockchain.get_peers()
        }
        return jsonify(response), 200

    @app.route('/wallet', methods=['POST'])
    def create_keys():
        wallet.create_keys()
        if wallet.save_keys():
            return jsonify(keys_file_response()), 201
        else:
            response = {
                'message': 'Failed'
            }
            return jsonify(response), 500

    @app.route('/wallet', methods=['GET'])
    def load_keys():
        if wallet.load_keys():
            return jsonify(keys_file_response()), 201
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

    @app.route('/transaction', methods=['POST'])
    def add_transaction():
        if wallet.public_key is None:
            response = {
                'message': 'No wallet'
            }
            return jsonify(response), 400
        params = request.get_json()
        if not params:
            response = {
                'message': 'No data provided'
            }
            return jsonify(response), 400
        required_params = ['recipient', 'amount']
        if not all(params in params for params in required_params):
            response = {
                'message': 'Data missing'
            }
            return jsonify(response), 400
        signature = wallet.sign_transaction(wallet.public_key,
                                            params['recipient'],
                                            params['amount'])
        if blockchain.add_transaction(params['recipient'],
                                      signature,
                                      wallet.public_key,
                                      params['amount']):
            response = {
                'message': 'Transaction added',
                'transaction': {
                    'sender': wallet.public_key,
                    'recipient': params['recipient'],
                    'amount': params['amount'],
                    'signature': signature
                },
                'balance': blockchain.get_balance()
            }
            return jsonify(response), 201
        else:
            response = {
                'message': 'Transaction failed'
            }
            return jsonify(response), 500

    @app.route('/', methods=['GET'])
    def get_ui():
        return send_from_directory('../web', 'node.html')

    @app.route('/transactions', methods=['GET'])
    def view_open_transactions():
        transactions = blockchain.view_open_transactions()
        dict_transactions = [transaction.__dict__ for
                             transaction in transactions]
        return jsonify(dict_transactions), 200

    @app.route('/blockchain', methods=['GET'])
    def get_chain():
        chain = blockchain.view_blockchain()
        dict_chain = [block.__dict__.copy() for block in chain]
        for dict_block in dict_chain:
            dict_block['transactions'] = [tx.__dict__ for tx in
                                          dict_block['transactions']]
        return jsonify(dict_chain), 200

    @app.route('/mine', methods=['POST'])
    def mine_block():
        block = blockchain.mine_block()
        if block is not None:
            dict_block = block.__dict__.copy()
            dict_block['transactions'] = [tx.__dict__ for tx in
                                          dict_block['transactions']]
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
