from src.recursion import calculate_power_set


class TestTowerOfHanoi(object):
    """
    Question 16.1
    """

    def test_small_input(self):
        pass


class TestNQueens(object):
    """
    Question 16.2
    """

    def test_four_queen_solutions(self):
        pass


class TestCalculatePowerSet(object):
    """
    Question 16.4
    """

    def test_minimal_example(self):
        expected = [
            [],
            ['x'], ['y'], ['z'],
            ['x', 'y'], ['x', 'z'], ['y', 'z'],
            ['x', 'y', 'z'],
        ]
        ls = ['x', 'y', 'z']
        powset = calculate_power_set(ls)
        assert len(expected) == len(powset)
        for elt in powset:
            assert elt in expected
