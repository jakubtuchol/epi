from src.honors_class import gcd


class TestGCD(object):
    """
    Question 22.1
    """

    def test_basic_example(self):
        assert 4 == gcd(20, 16)

    def test_odd_example(self):
        assert 7 == gcd(35, 21)

    def test_even_odd_example(self):
        assert 9 == gcd(81, 36)
