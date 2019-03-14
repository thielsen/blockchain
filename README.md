[![Build Status](https://travis-ci.org/thielsen/blockchain.svg?branch=master)](https://travis-ci.org/thielsen/blockchain) [![Maintainability](https://api.codeclimate.com/v1/badges/69b4f8731d960968c671/maintainability)](https://codeclimate.com/github/thielsen/blockchain/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/69b4f8731d960968c671/test_coverage)](https://codeclimate.com/github/thielsen/blockchain/test_coverage)

## Summary

This project is work in progress on a fully TDD basic implementation of blockchain in Python. 

## Technologies

- Python (Main language)
- Flask (RESTful API for nodes)
- Pytest (TDD)
- Travis (CI)
- Docker (Container)

## Design

### Proof of work
Proof of work is based on locating a SHA256 hash of the current transactions, previous hash and a proof that begins with a definied sequence. In this case (to ensure non stubbed testing works in a reasonable time while development takes place) the proof is a simple 00. Over time additional digits can be required which increases the difficulty of finding the proof. Once obtained it is trivial to proof the block as confirming the hash once the proof is provided is computationally easy.

### Public/Private Key encryption
Each wallet is produced with a public/private key pair. The public key is used as the wallet address whilst the private key should be kept securely. When sending a transaction the sender signs it with their private key and this can be verified with the public key for authenticity.

## API

- /             GET - Homepage (TODO - build out SPA for managing local node)
- /blockchain   GET - Returns a json response of the entire blockchain
- /mine         POST - Mines a block
- /wallet       POST - Creates new public and private keys
- /wallet       GET - Loads existing public and private keys
- /balance      GET - Gets current balance
- /peer         POST - Adds a remote peer to this nodes peer list
- /peer/<url>   DELETE - Removes a peer from this nodes peer list
- /peers        GET - Returns the list of this nodes peers
  
## Running a single node
 
To fire up a single node there is a lightweight Dockerfile based on Alpine linux which runs a node. To build clone the repo and run this locally:
 
 ```
 docker build -t blockchain_node:latest . 
 docker run -d -p 4000:4000 blockchain_node
 ```
You can then connect to http://localhost:4000 using postman and the APIs detailed above.

## TODOS

- Detail the APIs in more detail and add documentation of the backend design
- Create docker-compose to automatically fire up multiple nodes
- Add functionality to allow nodes to share created blocks with other nodes
- Add functionality to allow a new node to sync to other nodes
- Add SPA front end to control nodes locally and eliminate the need to use Postman
- Setup serverspec to test docker development process
- Add node autodiscovery so other nodes don't need to be added manually

## Credits

- https://davenash.com/2017/10/build-a-blockchain-with-c/ - this was very useful, in C++ but the principles convert when you get stuck..
- https://medium.com/@lhartikk/a-blockchain-in-200-lines-of-code-963cc1cc0e54 - a simple blockchain in JavaScript and also helpfully readable.
