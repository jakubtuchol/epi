from src.primitive import find_parity, reverse_digits

def test_basic_parity():
    x = int('1011', 2)
    assert find_parity(x) == 1

def test_basic_nonparity():
    x = int('10001000', 2)
    assert find_parity(x) == 0

def test_basic_reverse():
    assert reverse_digits(42) == 24

def test_negative_reverse():
    assert reverse_digits(-314) == -413

def test_reverse_zeros():
    assert reverse_digits(100) == 1
    assert reverse_digits(-100) == -1
