"""
Chapter 12: Searching
"""
from src.searching import find_entry_equal_to_index
from src.searching import find_first_occurrence
from src.searching import first_larger_than_num
from src.searching import smallest_cyclically_sorted_list
from src.searching import square_root


class TestFindFirstOccurrence(object):
    """
    Question 12.1
    """

    def test_book_example(self):
        ls = [-14, -10, 2, 108, 108, 243, 285, 285, 401]
        assert 3 == find_first_occurrence(108, ls)

    def test_repeating_example(self):
        ls = [1] * 12
        assert 0 == find_first_occurrence(1, ls)

    def test_non_existing_target(self):
        ls = [-14, -10, 2, 108, 108, 243, 285, 285, 401]
        assert -1 == find_first_occurrence(800, ls)
        assert -1 == find_first_occurrence(-200, ls)
        assert -1 == find_first_occurrence(100, ls)


class TestFirstLargerThanK(object):
    """
    Question 12.2
    """

    def test_book_example(self):
        ls = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
        assert 9 == first_larger_than_num(ls, 285)
        assert 1 == first_larger_than_num(ls, -13)
        assert -1 == first_larger_than_num(ls, 402)

    def test_repeating_example(self):
        ls = [1] * 12
        assert 0 == find_first_occurrence(1, ls)


class TestFindEntryEqualToIndex(object):
    """
    Question 12.3
    """

    def test_book_example(self):
        ls = [-2, 0, 2, 3, 6, 7, 9]
        assert find_entry_equal_to_index(ls) in {2, 3}

    def test_repeating_example(self):
        ls = [1] * 12
        assert 1 == find_entry_equal_to_index(ls)

    def test_range_input(self):
        ls = range(12)
        assert 0 == find_entry_equal_to_index(ls)


class TestSmallestCyclicallySortedArray(object):
    """
    Question 12.4
    """

    def test_book_example(self):
        in_arr = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]
        assert 4 == smallest_cyclically_sorted_list(in_arr)

    def test_tiny_example(self):
        in_arr = [2]
        assert 0 == smallest_cyclically_sorted_list(in_arr)

    def test_another_basic(self):
        in_arr = [5, 9, 13, 1, 3]
        assert 3 == smallest_cyclically_sorted_list(in_arr)


class TestSquareRoot(object):
    """
    Question 12.5
    """

    def test_equal_case(self):
        assert 16 == square_root(256)
        assert 10 == square_root(100)
        assert 6 == square_root(36)

    def test_lower_case(self):
        assert 10 == square_root(101)
        assert 16 == square_root(257)
        assert 6 == square_root(37)

    def test_book_case(self):
        assert 17 == square_root(300)
