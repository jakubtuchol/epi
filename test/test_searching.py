from src.searching import find_first_occurrence, square_root

class TestFindFirstOccurrence:
    '''
    Question 12.1
    '''
    def test_book_example(self):
        ls = [-14,-10,2,108,108,243,285,285,401]
        assert 3 == find_first_occurrence(108, ls)

    def test_repeating_example(self):
        ls = [1] * 12
        assert 0 == find_first_occurrence(1, ls)

    def test_non_existing_target(self):
        ls = [-14,-10,2,108,108,243,285,285,401]
        assert -1 == find_first_occurrence(800, ls)
        assert -1 == find_first_occurrence(-200, ls)
        assert -1 == find_first_occurrence(100, ls)

class TestSquareRoot:
    '''
    Question 12.5
    '''
    def test_equal_case(self):
        assert 16 == square_root(256)
        assert 10 == square_root(100)
        assert 6 == square_root(36)

    def test_lower_case(self):
        assert 10 == square_root(101)
        assert 16 == square_root(257)
        assert 6 == square_root(37)

    def test_book_case(self):
        assert 17 == square_root(300)
