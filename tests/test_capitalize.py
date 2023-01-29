import os
import sys
sys.path.append("../")
from app import *
def test_capitalize_function():
    assert set_capitalize("Prakash") == "Prakash"

def test_lower_function():
    assert set_capitalize("prakash") == "Prakash"
    
def test_upper_function():
    assert set_capitalize("PRAKASH") == "Prakash"
    



