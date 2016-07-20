from src.primitive import find_parity, reverse_digits

class TestParity:
    def test_basic_parity(self):
        x = int('1011', 2)
        assert find_parity(x) == 1

    def test_basic_nonparity(self):
        x = int('10001000', 2)
        assert find_parity(x) == 0

class TestReverseInteger:
    def test_basic_reverse(self):
        assert reverse_digits(42) == 24

    def test_negative_reverse(self):
        assert reverse_digits(-314) == -413

    def test_reverse_zeros(self):
        assert reverse_digits(100) == 1
        assert reverse_digits(-100) == -1
