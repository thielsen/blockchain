[![Build Status](https://travis-ci.org/thielsen/blockchain.svg?branch=master)](https://travis-ci.org/thielsen/blockchain) [![Maintainability](https://api.codeclimate.com/v1/badges/69b4f8731d960968c671/maintainability)](https://codeclimate.com/github/thielsen/blockchain/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/69b4f8731d960968c671/test_coverage)](https://codeclimate.com/github/thielsen/blockchain/test_coverage)

## Summary

This project is WIP on a basic implementation of a blockchain in Python.

## Technologies

- Python (Main language)
- Flask (RESTful API for nodes)
- Pytest (TDD)
- Travis (CI)

## Design

Proof of work - Proof of work is based on locating a SHA256 hash of the current transactions, previous hash and a proof that begins with a definied sequence. In this case (to ensure non stubbed testing works in a reasonable time while development takes place) the proof is a simple 00. Over time additional digits can be required which increases the difficulty of finding the proof. Once obtained it is trivial to proof the block as confirming the hash once the proof is provided is computationally easy.

Public/Private Key encryption - Each wallet is produced with a public/private key pair. The public key is used as the wallet address whilst the private key should be kept securely. When sending a transaction the sender signs it with their private key and this can be verified with the public key for authenticity.

## API

- /, GET - Homepage
- /blockchain, GET - Returns blockchain
- /mine, POST - Mines a block
- /wallet, POST - Creates new public and private keys
- /wallet, GET - Loads existing public and private keys
- /balance, GET - Gets current balance
