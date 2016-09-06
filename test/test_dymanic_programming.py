from src.dynamic_programming import count_score_combinations

class TestCountScoreCombinations(object):
    '''
    Question 17.1
    '''
    def test_single_combinations(self):
        assert 0 == count_score_combinations(1)
        assert 1 == count_score_combinations(2)
        assert 1 == count_score_combinations(3)

    def test_book_examples(self):
        assert 4 == count_score_combinations(12)
        assert 3 == count_score_combinations(9)
