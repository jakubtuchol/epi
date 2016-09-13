from src.binary_trees import TNode, is_balanced, compute_parent_lca, \
        is_symmetric, check_equal, reconstruct_tree

import pytest

@pytest.fixture(scope='module')
def create_basic_tree():
    root = TNode(1)
    root.left = TNode(2)
    root.right = TNode(3)
    root.left.left = TNode(4)
    root.left.right = TNode(5)
    root.right.left = TNode(6)
    root.right.right = TNode(7)
    return root

@pytest.fixture(scope='module')
def create_almost_equal():
    root = TNode(1)
    root.left = TNode(2)
    root.right = TNode(3)
    root.left.left = TNode(4)
    root.left.right = TNode(5)
    root.right.left = TNode(6)
    return root


class TestCheckEqual(object):
    '''
    Testing check equal helper function
    '''
    def test_equal_trees(self, create_basic_tree):
        assert check_equal(create_basic_tree, create_basic_tree)

    def test_almost_equal(self, create_basic_tree, create_almost_equal):
        assert not check_equal(create_basic_tree, create_almost_equal)


class TestIsBalanced(object):
    '''
    Question 10.1
    '''
    def test_book_case(self):
        '''
        Test balancing in book case
        '''
        root = TNode('A')
        # handle left subtree
        root.left = TNode('B')
        root.left.left = TNode('C')
        root.left.left.left = TNode('D')
        root.left.left.left.left = TNode('E')
        root.left.left.left.right = TNode('F')
        root.left.left.right = TNode('G')

        # handle left-right subtree
        root.left.right = TNode('H')
        root.left.right.left = TNode('I')
        root.left.right.right = TNode('J')

        # handle right subtree
        root.right = TNode('K')
        root.right.left = TNode('L')
        root.right.left.left = TNode('M')
        root.right.left.right = TNode('N')

        # handle right right subtree
        root.right.right = TNode('O')

        assert is_balanced(root)

    def test_degenerate_case(self):
        '''
        Test balance if root is None
        '''
        assert is_balanced(None)

    def test_basic_case(self):
        '''
        Test two basic cases of balanced trees
        '''
        root_1 = TNode(1)
        root_1.right = TNode(2)

        assert is_balanced(root_1)

        root_2 = TNode(3)
        root_2.left = TNode(4)
        root_2.right = TNode(5)

        assert is_balanced(root_2)

    def test_failure_case(self):
        '''
        Test basic failure case
        '''
        root = TNode(1)
        root.left = TNode(2)
        root.left.right = TNode(3)

        assert not is_balanced(root)


@pytest.fixture(scope='module')
def generate_symmetric_tree():
    root = TNode(314)

    # level 1
    root.left = TNode(6)
    root.right = TNode(6)

    # level 2
    root.left.right = TNode(2)
    root.right.left = TNode(2)

    # level 3
    root.left.right.right = TNode(3)
    root.right.left.left = TNode(3)

    return root

@pytest.fixture(scope='module')
def generate_asymmetric_value_tree():
    root = TNode(314)

    # level 1
    root.left = TNode(6)
    root.right = TNode(6)

    # level 2
    root.left.right = TNode(561)
    root.right.left = TNode(2)

    # level 3
    root.left.right.right = TNode(3)
    root.right.left.left = TNode(3)

    return root

@pytest.fixture(scope='module')
def generate_asymmetric_shape_tree():
    root = TNode(314)

    # level 1
    root.left = TNode(6)
    root.right = TNode(6)

    # level 2
    root.left.right = TNode(561)
    root.right.left = TNode(561)

    # level 3
    root.left.right.right = TNode(3)

    return root

class TestCheckSymmetric(object):
    '''
    Question 10.2
    '''
    def test_symmetric_case(self,):
        pass

class TestParentLCA(object):
    '''
    Question 10.4
    '''
    def test_basic_case(self):
        '''
        Right and left nodes with same parent
        '''
        root = TNode(1)
        root.left = TNode(2)
        root.right = TNode(3)
        root.left.parent = root
        root.right.parent = root

        assert root == compute_parent_lca(root.left, root.right)

    def test_deeper_case(self):
        '''
        Deeper case, with two nodes on subtree
        '''
        root = TNode(1)
        root.left = TNode(1)
        root.left.parent = root
        root.right = TNode(1)
        root.right.parent = root
        root.left.left = TNode(1)
        root.left.left.parent = root.left

        assert root == compute_parent_lca(root.left.left, root.right)


class TestCheckSymmetric(object):
    '''
    Question 10.2
    '''
    def test_symmetric_case(self, generate_symmetric_tree):
        assert is_symmetric(generate_symmetric_tree)

    def test_asymmetric_value_case(self, generate_asymmetric_value_tree):
        assert not is_symmetric(generate_asymmetric_value_tree)

    def test_asymmetric_shape_case(self, generate_asymmetric_shape_tree):
        assert not is_symmetric(generate_asymmetric_shape_tree)


class TestParentLCA(object):
    '''
    Question 10.4
    '''
    def test_basic_case(self):
        '''
        Right and left nodes with same parent
        '''
        root = TNode(1)
        root.left = TNode(2)
        root.right = TNode(3)
        root.left.parent = root
        root.right.parent = root

        assert root == compute_parent_lca(root.left, root.right)

    def test_deeper_case(self):
        '''
        Deeper case, with two nodes on subtree
        '''
        root = TNode(1)
        root.left = TNode(1)
        root.left.parent = root
        root.right = TNode(1)
        root.right.parent = root
        root.left.left = TNode(1)
        root.left.left.parent = root.left

        assert root == compute_parent_lca(root.left.left, root.right)


class TestReconstructTree(object):
    '''
    Question 10.10
    '''
    def test_basic_example(self):
        root = TNode('A')
        root.left = TNode('B')
        root.right = TNode('C')
        root.left.left = TNode('D')
        root.left.right = TNode('E')
        root.right.left = TNode('F')

        inorder = ['D','B','E','A','F','C']
        preorder = ['A','B','D','E','C','F']

        reconstruct = reconstruct_tree(preorder, inorder)
