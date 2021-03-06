from src.greedy_algorithms import find_ample_city
from src.greedy_algorithms import find_majority_element
from src.greedy_algorithms import GasCity
from src.greedy_algorithms import three_sum
from src.greedy_algorithms import trapped_water
from src.greedy_algorithms import two_sum


class TestTwoSum(object):
    """
    Testing two sum method
    """

    def test_book_example(self):
        in_arr = [11, 2, 5, 7, 3]
        assert two_sum(14, in_arr)
        assert two_sum(13, in_arr)
        assert two_sum(16, in_arr)
        assert not two_sum(17, in_arr)
        assert not two_sum(21, in_arr)
        assert not two_sum(11, in_arr)


class TestThreeSum(object):
    """
    Question 18.5
    """

    def test_book_example(self):
        in_arr = [11, 2, 5, 7, 3]
        assert three_sum(21, in_arr)
        assert not three_sum(22, in_arr)


class TestFindMajorityElement(object):
    """
    Question 18.6
    """

    def test_book_example(self):
        in_arr = [
            'b', 'a',
            'c', 'a',
            'a', 'b',
            'a', 'a',
            'c', 'a',
        ]
        assert 'a' == find_majority_element(in_arr)

    def test_int_example(self):
        in_arr = [
            3, 3, 4,
            2, 4, 4,
            2, 4, 4,
        ]
        assert 4 == find_majority_element(in_arr)


class TestFindAmpleCity(object):
    """
    Question 18.7
    """

    def test_book_example(self):
        cities = [
            GasCity(id='A', gas=50, to_next=900),
            GasCity(id='B', gas=20, to_next=600),
            GasCity(id='C', gas=5, to_next=200),
            GasCity(id='D', gas=30, to_next=400),
            GasCity(id='E', gas=25, to_next=600),
            GasCity(id='F', gas=10, to_next=200),
            GasCity(id='G', gas=10, to_next=100),
        ]

        assert 'D' == find_ample_city(cities)


class TestMaxTrappedWater(object):
    """
    Question 18.8
    """

    def test_book_example(self):
        heights = [
            1, 2, 1,
            3, 4, 4,
            5, 6, 2,
            1, 3, 1,
            3, 2, 1,
            2, 4, 1,
        ]
        assert 48 == trapped_water(heights)
