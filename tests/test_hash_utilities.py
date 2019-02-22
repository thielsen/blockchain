from sample.hash_utilities import *
import pytest

def test_hash_block():
    assert hash_block({'previous_hash': '', 'index': 0, 'transactions': []}) == 'b2242851cf5e7216d0bbb01ad9b6659bbca55f43c9ac3e63d0fac318b579c253'