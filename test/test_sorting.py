from src.sorting import compute_intersection

class TestComputeIntersection:
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
