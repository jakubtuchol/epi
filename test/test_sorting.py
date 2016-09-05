from src.sorting import compute_intersection, inplace_mergesort

class TestComputeIntersection(object):
    '''
    Question 14.1
    '''
    def test_basic(self):
        arr_1 = [2,3,3,5,5,6,7,7,8,12]
        arr_2 = [5,5,6,8,8,9,10,10]
        
        assert [5,6,8] == compute_intersection(arr_1, arr_2)

    def test_repeating_intersection(self):
        assert [1] == compute_intersection([1,1,1,1], [1,1])

    def test_next_basic(self):
        arr_1 = [2,3,3,5,7,11]
        arr_2 = [3,3,7,15,31]

        assert [3,7] == compute_intersection(arr_1, arr_2)

class TestInplaceMergesort(object):
    '''
    Question 14.2
    '''
    def test_book_case(self):
        long_arr = [5,13,17,None,None,None,None,None]
        short_arr = [3,7,11,19]
        expected = [3,5,7,11,13,17,19,None]
        inplace_mergesort(long_arr, 3, short_arr, 4)
        assert expected == long_arr
