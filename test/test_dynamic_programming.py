from src.dynamic_programming import calculate_levenshtein_distance
from src.dynamic_programming import count_score_combinations
from src.dynamic_programming import get_num_array_traversals
from src.dynamic_programming import KObject
from src.dynamic_programming import optimize_knapsack


class TestCountScoreCombinations(object):
    """
    Question 17.1
    """

    def test_single_combinations(self):
        assert 0 == count_score_combinations(1)
        assert 1 == count_score_combinations(2)
        assert 1 == count_score_combinations(3)

    def test_book_examples(self):
        assert 4 == count_score_combinations(12)
        assert 3 == count_score_combinations(9)


class TestLevenshteinDistance(object):
    """
    Question 17.2
    """

    def test_book_example(self):
        assert 4 == calculate_levenshtein_distance('Saturday', 'Sundays')

    def test_longer_example(self):
        assert 8 == calculate_levenshtein_distance('Carthorse', 'Orchestra')


class TestArrayTraversals(object):
    """
    Question 17.3
    """

    def test_book_example(self):
        assert 70 == get_num_array_traversals(5, 5)
        assert 35 == get_num_array_traversals(5, 4)
        assert 35 == get_num_array_traversals(4, 5)
        assert 6 == get_num_array_traversals(3, 3)


class TestOptimizeKnapsack(object):
    """
    Question 17.6
    """

    def test_book_example(self):
        knapsack = [
            KObject(id='A', price=65, weight=20),
            KObject(id='B', price=35, weight=8),
            KObject(id='C', price=245, weight=60),
            KObject(id='D', price=195, weight=55),
            KObject(id='E', price=65, weight=40),
            KObject(id='F', price=150, weight=70),
            KObject(id='G', price=275, weight=85),
            KObject(id='H', price=155, weight=25),
            KObject(id='I', price=120, weight=30),
            KObject(id='J', price=320, weight=65),
            KObject(id='K', price=75, weight=75),
            KObject(id='L', price=40, weight=10),
            KObject(id='M', price=200, weight=95),
            KObject(id='N', price=100, weight=50),
            KObject(id='O', price=220, weight=40),
            KObject(id='P', price=99, weight=10),
        ]
        assert 695 == optimize_knapsack(knapsack, 130)
