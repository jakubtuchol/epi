from src.heaps import Heap, merge_sorted_arrays

class TestMinHeap:
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

class TestMaxHeap:
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

class TestMergeArrays:
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
