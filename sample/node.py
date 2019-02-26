from flask import Flask
from flask_cors import CORS
from .wallet import Wallet

wallet = Wallet()

def create_app(config=None):
    app = Flask(__name__)
    CORS(app)

    @app.route('/', methods=['GET'])
    def get_ui():
        return 'Working'

    @app.route('/blockchain', methods=['GET'])
    def get_chain():
        pass

    return app

if __name__ == '__main__':
    app=create_app()
    app.run(host='0.0.0.0', port=4000)
