from src.primitive import add
from src.primitive import check_rectangle_intersection
from src.primitive import closest_int_same_bit_count
from src.primitive import find_parity
from src.primitive import get_intersection
from src.primitive import multiply
from src.primitive import palindrome_number
from src.primitive import Rectangle
from src.primitive import reverse_bits
from src.primitive import reverse_digits
from src.primitive import swap_bits


class TestParity(object):
    """
    Question 5.1
    """

    def test_basic_parity(self):
        x = int('1011', 2)
        assert find_parity(x) == 1

    def test_basic_non_parity(self):
        x = int('10001000', 2)
        assert find_parity(x) == 0


class TestSwapBits(object):
    """
    Question 5.2
    """

    def test_basic_example(self):
        assert 11 == swap_bits(73, 1, 6)


class TestReverseBits(object):
    """
    Question 5.3
    """

    def test_basic_reversal(self):
        """
        Alternating 0s and 1s reversed
        010101... => 101010...
        """
        num_in = 6148914691236517205
        num_out = 12297829382473034410L
        assert num_out == reverse_bits(num_in)

    def test_chunk_reversal(self):
        """
        48 0s and 16 1s => 16 1s and 48 0s
        """
        num_in = int((48 * '0') + (16 * '1'), 2)
        num_out = int((16 * '1') + (48 * '0'), 2)
        assert num_out == reverse_bits(num_in)


class TestClosestIntSameBitCount(object):
    """
    Question 5.4
    """

    def test_book_example(self):
        assert 4 == closest_int_same_bit_count(8)

    def test_increasing_example(self):
        assert 7 != closest_int_same_bit_count(7)
        assert 11 == closest_int_same_bit_count(7)


class TestMultiply(object):
    """
    Question 5.5
    """

    def test_basic_example(self):
        assert 42 == multiply(6, 7)

    def test_multi_shift(self):
        assert 10000 == multiply(100, 100)


class TestAdd(object):
    """
    Tests for helper function add
    """

    def test_basic_inputs(self):
        assert 100 == add(50, 50)
        assert 23 == add(19, 4)


class TestReverseInteger(object):
    """
    Question 5.8
    """

    def test_basic_reverse(self):
        assert reverse_digits(42) == 24

    def test_negative_reverse(self):
        assert reverse_digits(-314) == -413

    def test_reverse_zeros(self):
        assert reverse_digits(100) == 1
        assert reverse_digits(-100) == -1


class TestPalindromeNumber(object):
    """
    Question 5.9
    """

    def test_true_inputs(self):
        assert palindrome_number(0)
        assert palindrome_number(1)
        assert palindrome_number(7)
        assert palindrome_number(11)
        assert palindrome_number(121)
        assert palindrome_number(333)
        assert palindrome_number(2147447412)

    def test_false_inputs(self):
        assert not palindrome_number(-1)
        assert not palindrome_number(12)
        assert not palindrome_number(100)
        assert not palindrome_number(2147483647)


class TestCheckRectangleIntersection(object):
    """
    Question 5.11
    """

    def test_basic_case(self):
        rect_left = Rectangle(0, 0, 2, 2)
        rect_right = Rectangle(1, 1, 2, 2)
        rect_intersect = Rectangle(1, 1, 1, 1)
        assert get_intersection(rect_left, rect_right)
        assert get_intersection(rect_right, rect_left)
        result = check_rectangle_intersection(rect_left, rect_right)
        assert rect_intersect.x == result.x
        assert rect_intersect.y == result.y
        assert rect_intersect.width == result.width
        assert rect_intersect.height == result.height

    def test_fully_contained_case(self):
        rect_left = Rectangle(0, 0, 4, 4)
        rect_right = Rectangle(1, 1, 2, 2)
        rect_intersect = Rectangle(1, 1, 2, 2)
        assert get_intersection(rect_left, rect_right)
        assert get_intersection(rect_right, rect_left)
        result = check_rectangle_intersection(rect_left, rect_right)
        assert rect_intersect.x == result.x
        assert rect_intersect.y == result.y
        assert rect_intersect.width == result.width
        assert rect_intersect.height == result.height

    def test_mid_intersection(self):
        rect_left = Rectangle(0, 2, 1, 4)
        rect_right = Rectangle(1, 0, 4, 4)
        rect_intersect = Rectangle(1, 2, 1, 3)
        assert get_intersection(rect_left, rect_right)
        assert get_intersection(rect_right, rect_left)
        result = check_rectangle_intersection(rect_left, rect_right)
        assert rect_intersect.x == result.x
        assert rect_intersect.y == result.y
        assert rect_intersect.width == result.width
        assert rect_intersect.height == result.height

    def test_no_intersection(self):
        rect_left = Rectangle(0, 0, 3, 3)
        rect_right = Rectangle(4, 4, 1, 1)
        assert not get_intersection(rect_left, rect_right)
        assert not get_intersection(rect_right, rect_left)
        assert check_rectangle_intersection(rect_left, rect_right) is None
