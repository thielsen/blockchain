import pytest

from sample.block import *
from sample.hash_utilities import *

def test_hash_block():
    # Try and get this working with a double using doubles and an initial setup       
    assert hash_block(Block(0, '', [], 0, 0)) == 'b81af956031df89ac679981fc6641addd4bc4fe49641570886ec258986cc976d'
    
def test_hash_string256():
    assert hash_string_256('teststring') == '3c8727e019a42b444667a587b6001251becadabbb36bfed8087a92c18882d111'
        
