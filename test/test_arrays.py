from collections import defaultdict

from src.arrays import add_one
from src.arrays import apply_permutation
from src.arrays import buy_sell_once
from src.arrays import buy_sell_stock_twice
from src.arrays import can_reach_end
from src.arrays import check_sudoku
from src.arrays import delete_duplicates
from src.arrays import delete_key
from src.arrays import dutch_national_partition
from src.arrays import dutch_partition_better
from src.arrays import generate_primes
from src.arrays import get_square_idx
from src.arrays import multiply
from src.arrays import next_permutation
from src.arrays import nonuniform_random
from src.arrays import NumProbability
from src.arrays import online_sample
from src.arrays import random_permutation
from src.arrays import random_sample
from src.arrays import random_subset
from src.arrays import spiralize


class TestDutchNationalFlag(object):
    """
    Question 6.1
    """

    def test_arr_ordered(self):
        """
        should pass automatically, array
        is already ordered
        """
        arr = [0, 0, 0, 1, 1, 1, 2, 2, 2]
        dutch_national_partition(5, arr)
        for x in xrange(9):
            if x < 3:
                assert arr[x] == 0
            elif x < 6:
                assert arr[x] == 1
            else:
                assert arr[x] == 2

    def test_repeated_elements(self):
        """
        should function properly on
        an array with repeating elements
        """
        arr = [5, 3, 1, 5, 5, 3, 3, 1, 1]
        dutch_national_partition(1, arr)
        for x in xrange(9):
            if x < 3:
                assert arr[x] == 1
            elif x < 6:
                assert arr[x] == 3
            else:
                assert arr[x] == 5


class TestDutchFlagBetter(object):
    """
    Question 6.1
    """

    def test_better_ordered(self):
        arr = [0, 0, 0, 1, 1, 1, 2, 2, 2]
        dutch_partition_better(5, arr)
        for x in xrange(9):
            if x < 3:
                assert arr[x] == 0
            elif x < 6:
                assert arr[x] == 1
            else:
                assert arr[x] == 2

    def test_better_repeated(self):
        """
        should function properly on
        an array with repeating elements
        """
        arr = [5, 3, 1, 5, 5, 3, 3, 1, 1]
        dutch_partition_better(1, arr)
        for x in xrange(9):
            if x < 3:
                assert arr[x] == 1
            elif x < 6:
                assert arr[x] == 3
            else:
                assert arr[x] == 5


class TestAddOne(object):
    """
    Question 6.2
    """

    def test_book_example(self):
        assert [1, 3, 0] == add_one([1, 2, 9])

    def test_many_nines(self):
        assert [1, 0, 0, 0] == add_one([9, 9, 9])

    def test_normal_addition(self):
        assert [1] == add_one([0])
        assert [1, 2] == add_one([1, 1])


class TestMultiply(object):
    """
    Question 6.3
    """

    def test_book_example(self):
        first_num = [
            1, 9, 3,
            7, 0, 7,
            7, 2, 1
        ]
        second_num = [
            -7, 6, 1,
            8, 3, 8,
            2, 5, 7,
            2, 8, 7
        ]
        expected = [
            -1, 4, 7,
            5, 7, 3,
            9, 5, 2,
            5, 8, 9,
            6, 7, 6,
            4, 1, 2,
            9, 2, 7,
        ]
        assert expected == multiply(first_num, second_num)


class TestCanReachEnd(object):
    """
    Question 6.4
    """

    def test_successful_case(self):
        assert can_reach_end([3, 3, 1, 0, 2, 0, 1])

    def test_unsuccessful_case(self):
        assert not can_reach_end([3, 2, 0, 0, 2, 0, 1])


class TestDeleteKey(object):
    """
    Question 6.5
    """

    def test_book_example(self):
        ls = [
            5, 3, 7,
            11, 2, 3,
            13, 5, 7,
        ]
        expected = [
            5, 7, 11,
            2, 13, 5,
            7, None, None
        ]
        assert expected == delete_key(ls, 3)


class TestDeleteDuplicates(object):
    """
    Question 6.6
    """

    def test_book_example(self):
        assert 6 == delete_duplicates([2, 3, 5, 5, 7, 11, 11, 11, 13])

    def test_nonrepeating_example(self):
        assert 8 == delete_duplicates(range(8))


class TestBuySellOnce(object):
    """
    Question 6.7
    """

    def test_stock_one(self):
        stocks = [
            310, 315, 275,
            295, 260, 270,
            290, 230, 255,
            250,
        ]
        assert buy_sell_once(stocks) == 30

    def test_stock_two(self):
        stocks = [2, 3, 10, 6, 4, 8, 1]
        assert buy_sell_once(stocks) == 8

    def test_stock_three(self):
        stocks = [7, 9, 5, 6, 3, 2]
        assert buy_sell_once(stocks) == 2


class TestBuySellTwice(object):
    """
    Question 6.8
    """

    def test_book_example(self):
        stocks = [
            12, 11, 13,
            9, 12, 8,
            14, 13, 15,
        ]
        assert 10 == buy_sell_stock_twice(stocks)

    def test_regressive_input(self):
        assert 0 == buy_sell_stock_twice([])


class TestGeneratePrimes(object):
    """
    Question 6.9
    """

    def test_book_example(self):
        expected = [
            2, 3, 5,
            7, 11, 13,
            17,
        ]
        assert expected == generate_primes(18)


class TestApplyPermutation(object):
    """
    Question 6.10
    """

    def test_book_example(self):
        a = ['a', 'b', 'c', 'd']
        p = [2, 0, 1, 3]
        expected = ['b', 'c', 'a', 'd']
        assert expected == apply_permutation(a, p)


class TestNextPermutation(object):
    """
    Question 6.11
    """

    def test_book_example(self):
        assert [1, 2, 0, 3] == next_permutation([1, 0, 3, 2])

    def test_null_next(self):
        assert [] == next_permutation([3, 2, 1, 0])

    def test_larger_case(self):
        assert [4, 2, 0, 1, 3] == next_permutation([4, 1, 3, 2, 0])


class TestRandomSampling(object):
    """
    Question 6.12
    """

    def test_random_sample(self):
        population = list(range(100))
        sample_1 = random_sample(population, 5)
        sample_2 = random_sample(population, 5)
        assert sample_1 != sample_2


class TestOnlineSampling(object):
    """
    Question 6.13
    """

    def test_online_sample(self):
        population = list(range(100))
        sample_1 = online_sample(population, 5)
        sample_2 = online_sample(population, 5)
        assert sample_1 != sample_2


class TestRandomPermutation(object):
    """
    Question 6.14
    """

    def test_basic_example(self):
        sample_1 = random_permutation(10)
        sample_2 = random_permutation(10)
        assert sample_1 != sample_2

    def test_probability(self):
        seen = defaultdict(int)
        for _ in xrange(100):
            output = random_permutation(3)
            str_output = ''.join(map(lambda x: str(x), output))
            seen[str_output] += 1

        for val in seen.values():
            assert 10 < val < 30


class TestRandomSubset(object):
    """
    Question 6.15
    """

    def test_book_example(self):
        seen = defaultdict(int)
        for _ in xrange(100):
            output = random_subset(10, 1)
            seen[output[0]] += 1

        for val in seen.values():
            assert 5 < val < 20

    def test_empty_value(self):
        assert [] == random_subset(10, 0)


class TestCheckSudoku(object):
    """
    Question 6.17
    """

    def test_book_solution(self):
        sudoku = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9],
        ]
        assert check_sudoku(sudoku)

    def test_incorrect_sudoku(self):
        bad_sudoku = [
            [3, 5, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9],
        ]
        assert not check_sudoku(bad_sudoku)


class TestGetSquare(object):
    """
    Testing getting square indexes
    """

    def test_get_square(self):
        assert 0 == get_square_idx(1, 1)
        assert 1 == get_square_idx(0, 5)
        assert 2 == get_square_idx(2, 6)
        assert 3 == get_square_idx(3, 0)
        assert 5 == get_square_idx(3, 8)
        assert 6 == get_square_idx(7, 0)
        assert 7 == get_square_idx(8, 4)
        assert 8 == get_square_idx(6, 7)

    def test_get_four(self):
        assert 4 == get_square_idx(3, 3)
        assert 4 == get_square_idx(3, 4)
        assert 4 == get_square_idx(3, 5)
        assert 4 == get_square_idx(4, 3)
        assert 4 == get_square_idx(4, 4)
        assert 4 == get_square_idx(4, 5)
        assert 4 == get_square_idx(5, 3)
        assert 4 == get_square_idx(5, 4)
        assert 4 == get_square_idx(5, 5)


class TestNonuniformRandom(object):
    """
    Question 6.16
    """

    def test_basic_example(self):
        probs = [
            NumProbability(num=1, prob=1.0 / 3.0),
            NumProbability(num=3, prob=2.0 / 3.0),
        ]
        ones = 0
        threes = 0

        for _ in xrange(100):
            res = nonuniform_random(probs)
            if res == 3:
                threes += 1
            else:
                ones += 1

        assert threes > ones


class TestSpiralize(object):
    """
    Question 6.18
    """

    def test_spiralize_three(self):
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        arr = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        assert spiralize(arr) == expected

    def test_spiralize_four(self):
        expected = [
            1, 2, 3, 4,
            8, 12, 16, 15,
            14, 13, 9, 5,
            6, 7, 11, 10,
        ]
        arr = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]
        assert expected == spiralize(arr)
