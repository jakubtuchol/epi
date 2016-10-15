from src.honors_class import find_first_missing
from src.honors_class import gcd
from src.honors_class import largest_minus_one_product
from src.honors_class import longest_increasing_optimized
from src.honors_class import longest_increasing_subarray


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


class TestLargestMinusOneProduct(object):
    """
    Question 22.4
    """

    def test_all_even_example(self):
        arr = [3, 2, 5, 4]
        assert 60 == largest_minus_one_product(arr)

    def test_one_negative_example(self):
        arr = [3, 2, -1, 4]
        assert 24 == largest_minus_one_product(arr)

    def test_even_negative_example(self):
        arr = [3, 2, -1, 4, -1, 6]
        assert 72 == largest_minus_one_product(arr)

    def test_all_negative_example(self):
        arr = [-3, -2, -5, -4]
        assert -24 == largest_minus_one_product(arr)


class TestLongestIncreasingSubarray(object):
    """
    Question 22.5
    """

    def test_book_example(self):
        ls = [2, 11, 3, 5, 13, 7, 19, 17, 23]
        expected = (2, 4)
        assert expected == longest_increasing_subarray(ls)
        assert expected == longest_increasing_optimized(ls)
