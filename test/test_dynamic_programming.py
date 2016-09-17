from src.dynamic_programming import calculate_levenshtein_distance
from src.dynamic_programming import count_score_combinations
from src.dynamic_programming import get_num_array_traversals


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
