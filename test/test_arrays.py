from src.arrays import dutch_national_partition

class TestDutchNationalFlag:
    def test_arr_ordered(self):
        '''
        should pass automatically, array
        is already ordered
        '''
        arr = [0,0,0,1,1,1,2,2,2]
        dutch_national_partition(5, arr)
        for x in xrange(9):
            if x < 3:
                assert arr[x] == 0
            elif x < 6:
                assert arr[x] == 1 
            else:
                assert arr[x] == 2 

    def test_repeated_elements(self):
        '''
        should function properly on
        an array with repeating elements
        '''
        arr = [5,3,1,5,5,3,3,1,1]
        dutch_national_partition(1, arr)
        for x in xrange(9):
            if x < 3:
                assert arr[x] == 1
            elif x < 6:
                assert arr[x] == 3
            else:
                assert arr[x] == 5
