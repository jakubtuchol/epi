from src.heaps import Heap, merge_sorted_arrays, find_closest_stars

class TestMinHeap(object):
    '''
    Testing min heap
    '''
    def test_basic_heap(self):
        heap = Heap(lambda x,y: x < y)
        for i in xrange(10,0,-1):
            heap.insert(i)

        for i in xrange(1,11):
            assert i == heap.pop()

    def test_insert_equal(self):
        heap = Heap(lambda x,y: x < y)

        for _ in xrange(10):
            heap.insert(1)

        for _ in xrange(10):
            heap.insert(23)

        for _ in xrange(10):
            assert 1 == heap.pop()

        for _ in xrange(10):
            assert 23 == heap.pop()

    def test_tuple_insertion(self):
        heap = Heap(lambda x,y: x[0] < y[0])
        for i in xrange(10,0,-1):
            heap.insert((i, 10-i))

        for i in xrange(1,11):
            assert (i, 10-i) == heap.pop()

class TestMaxHeap(object):
    '''
    Testing max heap
    '''
    def test_basic_heap(self):
        heap = Heap(lambda x,y: x > y)
        for i in xrange(11):
            heap.insert(i)

        for i in xrange(10,1,-1):
            assert i == heap.pop()

    def test_insert_equal(self):
        heap = Heap(lambda x,y: x > y)

        for _ in xrange(10):
            heap.insert(1)
        for _ in xrange(10):
            heap.insert(23)

        for _ in xrange(10):
            assert 23 == heap.pop()
        for _ in xrange(10):
            assert 1 == heap.pop()

class TestMergeArrays(object):
    '''
    Question 11.1
    '''
    def test_book_case(self):
        '''
        Basic book case
        '''
        input_arrs = [
            [3,5,7],
            [0,6],
            [0,6,28],
        ]
        expected = [0,0,3,5,6,6,7,28]
        assert expected == merge_sorted_arrays(input_arrs)

    def test_asymmetrical_case(self):
        '''
        Significantly asymmetrical case
        '''
        input_arrs = [
            [10,100,1000, 10000],
            [0,200,400],
            [12],
        ]
        expected = [0,10,12,100,200,400,1000,10000]
        assert expected == merge_sorted_arrays(input_arrs)

class TestFindClosestStars(object):
    '''
    Question 11.4
    '''
    def test_basic_stream(self):
        stream = [
            200,30,42,
            500,80,928,
            23,3828,9382,
            12,8383,23,
            212,291,6342,
            32893,4,1221,
        ]
        assert [4,12,23] == sorted(find_closest_stars(3, stream))
        assert [4,12,23,23,30] == sorted(find_closest_stars(5, stream))
