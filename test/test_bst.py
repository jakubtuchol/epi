from src.bst import BST, check_bst, find_first_larger_key

import pytest

@pytest.fixture(scope='module')
def create_tiny_bst():
    '''
    Create tiny, correctly formatted BST
    '''
    root = BST(5)
    root.left = BST(2)
    root.right = BST(7)
    return root

@pytest.fixture(scope='module')
def create_large_bst():
    '''
    Create large properly formatted bst
    '''
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

@pytest.fixture
def create_large_nonbst():
    '''
    Create large improperly formatted bst
    '''
    root = BST(10)
    root.left = BST(5)
    root.right = BST(8)
    root.left.left = BST(2)
    root.left.right = BST(20)
    return root

class TestCheckBST:
    '''
    Question 15.1
    '''
    def test_small_example(self, create_tiny_bst):
        assert check_bst(create_tiny_bst)

    def test_large_correct_example(self, create_large_bst):
        assert check_bst(create_large_bst)

    def test_incorrect_example(self, create_large_nonbst):
        assert not check_bst(create_large_nonbst)

class TestFindFirstLargerKey:
    '''
    Question 15.3
    '''
    def test_book_example(self):
        pass