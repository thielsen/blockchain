[![Build Status](https://travis-ci.org/thielsen/blockchain.svg?branch=master)](https://travis-ci.org/thielsen/blockchain) [![Maintainability](https://api.codeclimate.com/v1/badges/69b4f8731d960968c671/maintainability)](https://codeclimate.com/github/thielsen/blockchain/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/69b4f8731d960968c671/test_coverage)](https://codeclimate.com/github/thielsen/blockchain/test_coverage)

## Summary

This project is WIP on a basic implementation of a blockchain in Python.

## Technologies

- Python (Main language)
- Flask (RESTful API for nodes)
- Pytest (TDD)
- Travis (CI)

## Design


## API

/, GET - Homepage
/blockchain, GET - Returns blockchain
/mine, POST - Mines a block
/wallet, POST - Creates new public and private keys
/wallet, GET - Loads existing public and private keys
/balance, GET - Gets current balance