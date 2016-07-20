from src.arrays import dutch_national_partition

class TestDutchNationalFlag:
    def test_arr_ordered(self):
        arr = [1,2,3,4,5,6,7,8,9,10]
        dutch_national_partition(5, arr)
        for x in range(1,11):
            assert arr[x-1] == x
