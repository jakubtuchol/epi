import pytest

from src.bst import BST
from src.bst import check_bst
from src.bst import find_first_larger_key
from src.bst import find_first_occurrence
from src.bst import find_largest_keys
from src.bst import find_lca


# Fixtures
@pytest.fixture(scope='module')
def create_tiny_bst():
    """
    Create tiny, correctly formatted BST
    """
    root = BST(5)
    root.left = BST(2)
    root.right = BST(7)
    return root


@pytest.fixture(scope='module')
def create_tiny_nonbst():
    """
    Create tiny incorrectly formatted BST
    """
    root = BST(30)
    root.left = BST(35)
    root.right = BST(25)
    return root


@pytest.fixture(scope='module')
def create_large_bst():
    """
    Create large properly formatted bst
    """
    root = BST(19)
    # level 1
    root.left = BST(7)
    root.right = BST(43)
    # level 2
    root.left.left = BST(3)
    root.left.right = BST(11)
    root.right.left = BST(23)
    root.right.right = BST(47)
    # level 3
    root.left.left.left = BST(2)
    root.left.left.right = BST(5)
    root.left.right.right = BST(17)
    root.right.left.right = BST(37)
    root.right.right.right = BST(53)
    # level 4
    root.left.right.right.left = BST(13)
    root.right.left.right.left = BST(29)
    root.right.left.right.right = BST(41)
    # level 5
    root.right.left.right.left.right = BST(31)

    return root


@pytest.fixture(scope='module')
def create_large_nonbst():
    """
    Create large improperly formatted bst
    """
    root = BST(10)
    root.left = BST(5)
    root.right = BST(8)
    root.left.left = BST(2)
    root.left.right = BST(20)
    return root


@pytest.fixture(scope='module')
def generate_repeated_key_bst():
    # level 0
    root = BST(108)

    # level 1
    root.left = BST(108)
    root.right = BST(285)

    # level 2
    root.left.left = BST(-10)
    root.left.right = BST(2)
    root.right.left = BST(243)
    root.right.right = BST(285)

    # level 3
    root.left.left.left = BST(-14)
    root.left.left.right = BST(2)
    root.right.right.right = BST(401)

    return root


# Tests
class TestCheckBST(object):
    """
    Question 15.1
    """

    def test_small_example(self, create_tiny_bst):
        assert check_bst(create_tiny_bst)

    def test_small_nonexample(self, create_tiny_nonbst):
        assert not check_bst(create_tiny_nonbst)

    def test_large_correct_example(self, create_large_bst):
        assert check_bst(create_large_bst)

    def test_incorrect_example(self, create_large_nonbst):
        assert not check_bst(create_large_nonbst)


class TestFindFirstOccurrence(object):
    """
    Question 15.2
    """

    def test_book_example(self, generate_repeated_key_bst):
        root = generate_repeated_key_bst
        assert root.right == find_first_occurrence(root, 285)
        assert root.left == find_first_occurrence(root, 108)


class TestFindFirstLargerKey(object):
    """
    Question 15.3
    """

    def test_book_example(self, create_large_bst):
        assert 29 == find_first_larger_key(create_large_bst, 23)

    def test_nonval(self, create_tiny_bst):
        assert find_first_larger_key(create_tiny_bst, 10) is None


class TestFindKLargestElements(object):
    """
    Question 15.4
    """

    def test_tiny_tree(self, create_tiny_bst):
        assert [7] == find_largest_keys(create_tiny_bst, 1)

    def test_larger_tree(self, create_large_bst):
        assert [
            23, 29, 31,
            37, 41, 43,
            47, 53
        ] == find_largest_keys(create_large_bst, 8)


class TestGetLCA(object):
    """
    Question 15.5
    """

    def test_large_bst_example(self, create_large_bst):
        assert 7 == find_lca(create_large_bst, 5, 13)

    def test_same_node_example(self, create_large_bst):
        assert 23 == find_lca(create_large_bst, 23, 41)

    def test_out_of_bounds_nodes(self, create_large_bst):
        assert None is find_lca(create_large_bst, 55, 65)
