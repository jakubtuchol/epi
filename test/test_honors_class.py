from src.honors_class import buy_sell_stock_k_times
from src.honors_class import compute_circular_sorted_median
from src.honors_class import find_first_missing
from src.honors_class import gcd
from src.honors_class import justify_text
from src.honors_class import largest_minus_one_product
from src.honors_class import longest_increasing_optimized
from src.honors_class import longest_increasing_subarray
from src.honors_class import rook_attack
from src.honors_class import zip_linked_list
from src.linked_lists import Node


def is_close(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


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


class TestBuySellStockKTimes(object):
    """
    Question 22.3
    """

    def test_basic_example(self):
        stocks = [2, 5, 7, 1, 4, 3, 1, 3]
        assert 10 == buy_sell_stock_k_times(stocks, 3)


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


class TestRookAttack(object):
    """
    Question 22.7
    """

    def test_book_example(self):
        board = [
            [1, 0, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
        ]
        expected = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 1, 1],
            [0, 0, 1, 0, 1, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 1, 1],
        ]

        assert expected == rook_attack(board)


class TestJustifyText(object):
    """
    Question 22.8
    """

    def test_book_case(self):
        input_words = [
            'The', 'quick', 'brown',
            'fox', 'jumped', 'over',
            'the', 'lazy', 'dogs.',
        ]

        ouput_words = [
            'The   quick',
            'brown   fox',
            'jumped over',
            'the    lazy',
            'dogs.      ',
        ]

        assert ouput_words == justify_text(input_words, 11)


class TestZipLinkedList(object):
    """
    Question 22.10
    """

    def test_none_case(self):
        assert zip_linked_list(None) is None

    def test_single_case(self):
        single = Node(1)
        assert single == zip_linked_list(single)

    def test_basic_case(self):
        fake_head = Node(None)
        head = fake_head

        for x in xrange(5):
            head.next = Node(x)
            head = head.next

        zipped = zip_linked_list(fake_head.next)

        for x in [0, 4, 1, 3, 2]:
            assert x == zipped.val
            zipped = zipped.next

        assert zipped is None


class TestComputeCircularSortedMedian(object):
    """
    Question 22.12
    """

    def test_none_case(self):
        assert compute_circular_sorted_median(None) is None

    def test_single_case(self):
        single = Node(1)
        single.next = single

        assert is_close(1, compute_circular_sorted_median(single))

    def test_odd_case(self):
        fake_head = Node(None)
        head = fake_head

        for idx in xrange(5):
            head.next = Node(idx)
            head = head.next

        head.next = fake_head.next

        assert is_close(2, compute_circular_sorted_median(fake_head.next))

    def test_even_case(self):
        fake_head = Node(None)
        head = fake_head

        for idx in xrange(1, 11):
            head.next = Node(idx)
            head = head.next

        head.next = fake_head.next
        assert is_close(5.5, compute_circular_sorted_median(fake_head.next))
