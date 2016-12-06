from src.heaps import almost_sorted
from src.heaps import compute_k_largest_binary_heap
from src.heaps import find_closest_stars
from src.heaps import Heap
from src.heaps import merge_sorted_arrays
from src.heaps import sort_increasing_decreasing
from src.heaps import stream_median


class TestMinHeap(object):
    """
    Testing min heap
    """

    def test_basic_heap(self):
        heap = Heap(lambda x, y: x < y)
        for i in xrange(10, 0, -1):
            heap.insert(i)

        for i in xrange(1, 11):
            assert i == heap.pop()

    def test_insert_equal(self):
        heap = Heap(lambda x, y: x < y)

        for _ in xrange(10):
            heap.insert(1)

        for _ in xrange(10):
            heap.insert(23)

        for _ in xrange(10):
            assert 1 == heap.pop()

        for _ in xrange(10):
            assert 23 == heap.pop()

    def test_tuple_insertion(self):
        heap = Heap(lambda x, y: x[0] < y[0])
        for i in xrange(10, 0, -1):
            heap.insert((i, 10 - i))

        for i in xrange(1, 11):
            assert (i, 10 - i) == heap.pop()


class TestMaxHeap(object):
    """
    Testing max heap
    """

    def test_basic_heap(self):
        heap = Heap(lambda x, y: x > y)
        for i in xrange(11):
            heap.insert(i)

        for i in xrange(10, 1, -1):
            assert i == heap.pop()

    def test_insert_equal(self):
        heap = Heap(lambda x, y: x > y)

        for _ in xrange(10):
            heap.insert(1)
        for _ in xrange(10):
            heap.insert(23)

        for _ in xrange(10):
            assert 23 == heap.pop()
        for _ in xrange(10):
            assert 1 == heap.pop()


class TestMergeArrays(object):
    """
    Question 11.1
    """

    def test_book_case(self):
        """
        Basic book case
        """
        input_arrs = [
            [3, 5, 7],
            [0, 6],
            [0, 6, 28],
        ]
        expected = [0, 0, 3, 5, 6, 6, 7, 28]
        assert expected == merge_sorted_arrays(input_arrs)

    def test_asymmetrical_case(self):
        """
        Significantly asymmetrical case
        """
        input_arrs = [
            [10, 100, 1000, 10000],
            [0, 200, 400],
            [12],
        ]
        expected = [0, 10, 12, 100, 200, 400, 1000, 10000]
        assert expected == merge_sorted_arrays(input_arrs)


class TestSortIncreasingDecreasing(object):
    """
    Question 11.2
    """

    def test_book_example(self):
        ls = [
            57, 131, 493,
            294, 221, 339,
            418, 452, 442, 190,
        ]
        expected = [
            57, 131, 190,
            221, 294, 339,
            418, 442, 452, 493,
        ]
        assert expected == sort_increasing_decreasing(ls)


class TestAlmostSorted(object):
    """
    Question 11.3
    """

    def test_book_example(self):
        arr = [3, -1, 2, 6, 4, 5, 8]
        expected = [-1, 2, 3, 4, 5, 6, 8]
        assert expected == almost_sorted(arr, 2)

    def test_closer_example(self):
        arr = [2, -1, 4, 3, 6, 5, 10, 8]
        expected = [-1, 2, 3, 4, 5, 6, 8, 10]
        assert expected == almost_sorted(arr, 2)
        assert expected == almost_sorted(arr, 1)
        assert expected == almost_sorted(expected, 0)


class TestFindClosestStars(object):
    """
    Question 11.4
    """

    def test_basic_stream(self):
        stream = [
            200, 30, 42,
            500, 80, 928,
            23, 3828, 9382,
            12, 8383, 23,
            212, 291, 6342,
            32893, 4, 1221,
        ]
        assert [4, 12, 23] == sorted(find_closest_stars(3, stream))
        assert [4, 12, 23, 23, 30] == sorted(find_closest_stars(5, stream))


class TestStreamMedian(object):
    """
    Question 11.5
    """

    def test_find_median(self):
        arr = [
            2, 3, 5,
            7, 11, 13,
            17, 19, 23,
            29, 31, 37,
            41, 43, 47,
            53, 59, 61,
            67, 71, 73,
            79, 83, 89, 97,
        ]
        assert 41 == stream_median(arr)


class TestComputeKLargestBinaryHeap(object):
    """
    Question 11.6
    """

    def test_basic_example(self):
        maxheap = Heap(lambda x, y: x > y)
        for i in xrange(11):
            maxheap.insert(i)

        expected = [10, 9, 8, 7, 6]
        assert expected == compute_k_largest_binary_heap(
            maxheap._heap_list[1:], 5)
