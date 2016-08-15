from src.heaps import Heap, merge_sorted_arrays

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
