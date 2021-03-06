from src.recursion import calculate_power_set
from src.recursion import generate_permutations
from src.recursion import generate_subsets


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


class TestGeneratePermutations(object):
    """
    Question 16.3
    """

    def test_book_example(self):
        ls = [2, 3, 5, 7]
        expected = [
            [2, 3, 5, 7], [2, 3, 7, 5], [2, 5, 3, 7],
            [2, 5, 7, 3], [2, 7, 3, 5], [2, 7, 5, 3],
            [3, 2, 5, 7], [3, 2, 7, 5], [3, 5, 2, 7],
            [3, 5, 7, 2], [3, 7, 2, 5], [3, 7, 5, 2],
            [5, 2, 3, 7], [5, 2, 7, 3], [5, 3, 2, 7],
            [5, 3, 7, 2], [5, 7, 2, 3], [5, 7, 3, 2],
            [7, 2, 3, 5], [7, 2, 5, 3], [7, 3, 2, 5],
            [7, 3, 5, 2], [7, 5, 2, 3], [7, 5, 3, 2]
        ]
        perms = generate_permutations(ls)
        print('got result {}'.format(perms))
        print('got result of length {}'.format(len(perms)))
        for p in expected:
            assert p in perms
        assert len(expected) == len(perms)


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


class TestGenerateSubsets(object):
    """
    Question 16.5
    """

    def test_book_example(self):
        subsets = generate_subsets(5, 2)
        expected = [
            [1, 2], [1, 3], [1, 4],
            [1, 5], [2, 3], [2, 4],
            [2, 5], [3, 4], [3, 5],
            [4, 5],
        ]

        for sub in expected:
            assert sub in subsets
        assert len(expected) == len(subsets)

    def test_larger_example(self):
        expected = [
            [1, 2, 3], [1, 2, 4], [1, 2, 5],
            [1, 3, 4], [1, 3, 5], [1, 4, 5],
            [2, 3, 4], [2, 3, 5], [2, 4, 5],
            [3, 4, 5],
        ]
        subsets = generate_subsets(5, 3)

        for sub in expected:
            assert sub in subsets
        assert len(expected) == len(subsets)

    def test_singular_example(self):
        expected = [
            [1], [2], [3],
            [4], [5], [6],
            [7], [8], [9],
        ]
        subsets = generate_subsets(9, 1)

        for sub in expected:
            assert sub in subsets
        assert len(expected) == len(subsets)
