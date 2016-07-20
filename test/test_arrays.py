from src.arrays import dutch_national_partition, dutch_partition_better

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

class TestDutchFlagBetter:
    def test_better_ordered(self):
        arr = [0,0,0,1,1,1,2,2,2]
        dutch_partition_better(5, arr)
        for x in xrange(9):
            if x < 3:
                assert arr[x] == 0
            elif x < 6:
                assert arr[x] == 1 
            else:
                assert arr[x] == 2 

    def test_better_repeated(self):
        '''
        should function properly on
        an array with repeating elements
        '''
        arr = [5,3,1,5,5,3,3,1,1]
        dutch_partition_better(1, arr)
        for x in xrange(9):
            if x < 3:
                assert arr[x] == 1
            elif x < 6:
                assert arr[x] == 3
            else:
                assert arr[x] == 5
