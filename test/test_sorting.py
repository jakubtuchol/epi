from src.sorting import compute_intersection
from src.sorting import count_occurrences
from src.sorting import find_max_simultaneous_events
from src.sorting import inplace_mergesort


class TestComputeIntersection(object):
    """
    Question 14.1
    """

    def test_basic(self):
        arr_1 = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12]
        arr_2 = [5, 5, 6, 8, 8, 9, 10, 10]

        assert [5, 6, 8] == compute_intersection(arr_1, arr_2)

    def test_repeating_intersection(self):
        assert [1] == compute_intersection([1, 1, 1, 1], [1, 1])

    def test_next_basic(self):
        arr_1 = [2, 3, 3, 5, 7, 11]
        arr_2 = [3, 3, 7, 15, 31]

        assert [3, 7] == compute_intersection(arr_1, arr_2)


class TestInplaceMergesort(object):
    """
    Question 14.2
    """

    def test_book_case(self):
        long_arr = [5, 13, 17, None, None, None, None, None]
        short_arr = [3, 7, 11, 19]
        expected = [3, 5, 7, 11, 13, 17, 19, None]
        inplace_mergesort(long_arr, 3, short_arr, 4)
        assert expected == long_arr


class TestCountOccurrences(object):
    """
    Question 14.3
    """

    def test_book_example(self):
        sentence = 'bcdacebe'
        expected = [('a', 1), ('b', 2), ('c', 2), ('d', 1), ('e', 2)]
        output = sorted(count_occurrences(sentence), key=lambda x: x[0])
        assert expected == output

    def test_mixed_case_sentence(self):
        sentence = 'Mary had a little lamb'
        expected = [
            (' ', 4), ('a', 4), ('b', 1),
            ('d', 1), ('e', 1), ('h', 1),
            ('i', 1), ('l', 3), ('m', 2),
            ('r', 1), ('t', 2), ('y', 1),
        ]
        output = sorted(count_occurrences(sentence), key=lambda x: x[0])
        assert expected == output


class TestFindMaxSimultaneousEvents(object):
    """
    Question 14.5
    """

    def test_book_example(self):
        events = [
            (1, 5), (6, 10), (11, 13),
            (14, 15), (2, 7), (8, 9),
            (12, 15), (4, 5), (9, 18),
        ]
        assert 3 == find_max_simultaneous_events(events)
