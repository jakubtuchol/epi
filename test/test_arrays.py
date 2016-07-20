from src.arrays import dutch_national_partition, dutch_partition_better, buy_sell_once, random_sample

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

class TestBuySellOnce:
    def test_stock_one(self):
        stocks = [
            310, 315, 275,
            295, 260, 270,
            290, 230, 255,
            250,
        ]
        assert buy_sell_once(stocks) == 30

    def test_stock_two(self):
        stocks = [2,3,10,6,4,8,1]
        assert buy_sell_once(stocks) == 8

    def test_stock_three(self):
        stocks = [7,9,5,6,3,2]
        assert buy_sell_once(stocks) == 2

class TestRandomSampling:
    def test_random_sample(self):
        population = list(range(100))
        sample_1 = random_sample(population, 5)
        sample_2 = random_sample(population, 5)
        assert sample_1 != sample_2
