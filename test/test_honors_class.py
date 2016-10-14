from src.honors_class import find_first_missing
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


class TestFirstMissing(object):
    """
    Question 22.2
    """

    def test_book_example(self):
        arr = [3, 5, 4, -1, 5, 1, -1]
        assert 2 == find_first_missing(arr)

    def test_next_lowest_example(self):
        arr = [3, 4, 0, 2]
        assert 1 == find_first_missing(arr)

    def test_no_missing_example(self):
        arr = [5, 3, 2, 4, 1]
        assert 6 == find_first_missing(arr)
