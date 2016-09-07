from src.greedy_algorithms import two_sum, three_sum, find_majority_element

class TestTwoSum(object):
    '''
    Testing two sum method
    '''
    def test_book_example(self):
        in_arr = [11,2,5,7,3]
        assert two_sum(14, in_arr)
        assert two_sum(13, in_arr)
        assert two_sum(16, in_arr)
        assert not two_sum(17, in_arr)
        assert not two_sum(21, in_arr)
        assert not two_sum(11, in_arr)

class TestThreeSum(object):
    '''
    Question 18.5
    '''
    def test_book_example(self):
        in_arr = [11,2,5,7,3]
        assert three_sum(21, in_arr)
        assert not three_sum(22, in_arr)

class TestFindMajorityElement(object):
    '''
    Question 18.6
    '''
    def test_book_example(self):
        in_arr = [
            'b','a',
            'c','a',
            'a','b',
            'a','a',
            'c','a',
        ]
        assert 'a' == find_majority_element(in_arr)

    def test_int_example(self):
        in_arr = [
            3,3,4,
            2,4,4,
            2,4,4,
        ]
        assert 4 == find_majority_element(in_arr)
