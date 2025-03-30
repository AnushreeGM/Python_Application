# test/test_myapp.py

import pytest
from app.myapp import hello_world  # Importing the hello_world function

def test_hello_world():
    """Test the hello_world function."""
    assert hello_world() == "Hello, World!"
