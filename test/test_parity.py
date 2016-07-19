from src.primitive import find_parity

def test_basic_parity():
    x = int('1011', 2)
    assert find_parity(x) == 1

def test_basic_nonparity():
    x = int('10001000', 2)
    assert find_parity(x) == 0
