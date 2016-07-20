from src.arrays import dutch_national_partition

class TestDutchNationalFlag:
    def test_arr_ordered(self):
        '''
        should pass automatically, array
        is already ordered
        '''
        arr = [1,2,3,4,5,6,7,8,9,10]
        dutch_national_partition(5, arr)
        for x in xrange(1,11):
            if x < 5:
                assert arr[x-1] < 5
            else:
                assert arr[x-1] >= 5

    def test_arry_reversed(self):
        '''
        should properly reverse array
        '''
        arr = [10,9,8,7,6,5,4,3,2,1]
        dutch_national_partition(5, arr)
        for x in xrange(1,11):
            if x < 5:
                assert arr[x-1] < 5
            else:
                assert arr[x-1] >= 5

    def test_repeated_elements(self):
        '''
        should function properly on
        an array with repeating elements
        '''
        arr = [5,3,1,5,5,3,3,1,1]
        dutch_national_partition(1, arr)
        for x in xrange(9):
            if x <= 2:
                assert arr[x] == 1
            elif x <= 5:
                assert arr[x] == 3
            else:
                assert arr[x] == 5
