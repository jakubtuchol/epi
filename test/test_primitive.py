from src.primitive import find_parity, reverse_bits, reverse_digits

class TestParity(object):
    '''
    Question 5.1
    '''
    def test_basic_parity(self):
        x = int('1011', 2)
        assert find_parity(x) == 1

    def test_basic_nonparity(self):
        x = int('10001000', 2)
        assert find_parity(x) == 0

class TestReverseBits(object):
    '''
    Question 5.3
    '''
    def test_basic_reversal(self):
        '''
        Alternating 0s and 1s reversed
        010101... => 101010...
        '''
        num_in = 6148914691236517205
        num_out = 12297829382473034410L
        assert num_out == reverse_bits(num_in)

    def test_chunk_reversal(self):
        '''
        48 0s and 16 1s => 16 1s and 48 0s
        '''
        num_in = int((48 * '0') + (16 * '1'), 2)
        num_out = int((16 * '1') + (48 * '0'), 2)
        assert num_out == reverse_bits(num_in)

class TestReverseInteger(object):
    '''
    Question 5.8
    '''
    def test_basic_reverse(self):
        assert reverse_digits(42) == 24

    def test_negative_reverse(self):
        assert reverse_digits(-314) == -413

    def test_reverse_zeros(self):
        assert reverse_digits(100) == 1
        assert reverse_digits(-100) == -1
