import pytest

from src.binary_trees import calculate_tree_exterior
from src.binary_trees import check_equal
from src.binary_trees import compute_lca
from src.binary_trees import compute_parent_lca
from src.binary_trees import create_leaf_list
from src.binary_trees import find_successor
from src.binary_trees import get_kth_inorder_record
from src.binary_trees import has_leaf_sum
from src.binary_trees import inorder_traversal
from src.binary_trees import is_balanced
from src.binary_trees import is_symmetric
from src.binary_trees import reconstruct_preorder
from src.binary_trees import reconstruct_tree
from src.binary_trees import sum_root_to_leaf
from src.binary_trees import TNode


# Fixtures
@pytest.fixture(scope='module')
def create_basic_tree():
    """
                  1
                 / \
                2   3
               /|  / \
              4  5 6  7
    """
    root = TNode(1)
    root.left = TNode(2)
    root.left.parent = root
    root.right = TNode(3)
    root.right.parent = root
    root.left.left = TNode(4)
    root.left.left.parent = root.left
    root.left.right = TNode(5)
    root.left.right.parent = root.left
    root.right.left = TNode(6)
    root.right.left.parent = root.right
    root.right.right = TNode(7)
    root.right.right.parent = root.right
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


@pytest.fixture(scope='module')
def generate_tiny_tree():
    root = TNode(1)
    root.left = TNode(2)
    root.right = TNode(3)
    root.left.parent = root
    root.right.parent = root
    return root


@pytest.fixture(scope='module')
def generate_binary_binary_tree():
    # level 0
    root = TNode(1)

    # level 1
    root.left = TNode(0)
    root.right = TNode(1)

    # level 2
    root.left.left = TNode(0)
    root.left.right = TNode(1)
    root.right.left = TNode(0)
    root.right.right = TNode(0)

    # level 2
    root.left.left.left = TNode(0)
    root.left.left.right = TNode(1)
    root.left.right.right = TNode(1)
    root.right.left.right = TNode(0)
    root.right.right.right = TNode(0)

    # level 3
    root.left.right.right.left = TNode(0)
    root.right.left.right.left = TNode(1)
    root.right.left.right.right = TNode(0)

    # level 4
    root.right.left.right.left.right = TNode(1)

    return root


@pytest.fixture(scope='module')
def generate_char_tree():
    root = TNode('A')

    root.left = TNode('B')
    root.left.parent = root

    root.right = TNode('C')
    root.right.parent = root

    root.left.left = TNode('D')
    root.left.left.parent = root.left

    root.left.right = TNode('E')
    root.left.right.parent = root.left

    root.right.left = TNode('F')
    root.right.left.parent = root.right

    return root


@pytest.fixture(scope='module')
def generate_binary_tree():
    # level 0
    root = TNode('H')

    # level 1
    root.right = TNode('C')
    root.left = TNode('B')

    # level 2
    root.right.right = TNode('D')
    root.left.left = TNode('F')
    root.left.right = TNode('E')

    # level 3
    root.right.right.right = TNode('G')
    root.left.right.left = TNode('A')

    # level 4
    root.right.right.right.left = TNode('I')

    return root


@pytest.fixture(scope='module')
def generate_sum_tree():
    # level 0
    root = TNode(314, node_id='A')

    # level 1
    root.left = TNode(6, node_id='B')
    root.right = TNode(6, node_id='I')

    # level 2
    root.left.left = TNode(271, node_id='C')
    root.left.right = TNode(561, node_id='F')
    root.right.left = TNode(2, node_id='J')
    root.right.right = TNode(271, node_id='O')

    # level 3
    root.left.left.left = TNode(28, node_id='D')
    root.left.left.right = TNode(0, node_id='E')
    root.left.right.right = TNode(3, node_id='G')
    root.right.left.right = TNode(1, node_id='K')
    root.right.right.right = TNode(28, node_id='P')

    # level 4
    root.left.right.right.left = TNode(17, node_id='H')
    root.right.left.right.left = TNode(401, node_id='L')
    root.right.left.right.right = TNode(257, node_id='N')

    # level 5
    root.right.left.right.left.right = TNode(641, node_id='M')

    return root


# Tests
class TestCheckEqual(object):
    """
    Testing check equal helper function
    """

    def test_equal_trees(self, create_basic_tree):
        assert check_equal(create_basic_tree, create_basic_tree)

    def test_almost_equal(self, create_basic_tree, create_almost_equal):
        assert not check_equal(create_basic_tree, create_almost_equal)


class TestIsBalanced(object):
    """
    Question 10.1
    """

    def test_book_case(self):
        """
        Test balancing in book case
        """
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
        """
        Test balance if root is None
        """
        assert is_balanced(None)

    def test_basic_case(self):
        """
        Test two basic cases of balanced trees
        """
        root_1 = TNode(1)
        root_1.right = TNode(2)

        assert is_balanced(root_1)

        root_2 = TNode(3)
        root_2.left = TNode(4)
        root_2.right = TNode(5)

        assert is_balanced(root_2)

    def test_failure_case(self):
        """
        Test basic failure case
        """
        root = TNode(1)
        root.left = TNode(2)
        root.left.right = TNode(3)

        assert not is_balanced(root)


class TestCheckSymmetric(object):
    """
    Question 10.2
    """

    def test_symmetric_case(self, generate_symmetric_tree):
        assert is_symmetric(generate_symmetric_tree)

    def test_asymmetric_value_case(self, generate_asymmetric_value_tree):
        assert not is_symmetric(generate_asymmetric_value_tree)

    def test_asymmetric_shape_case(self, generate_asymmetric_shape_tree):
        assert not is_symmetric(generate_asymmetric_shape_tree)


class TestFindLCA(object):
    """
    Question 10.3
    """

    def test_tiny_example(self, generate_tiny_tree):
        root = generate_tiny_tree
        assert root == compute_lca(root, root.left, root.right)

    def test_char_tree_example(self, generate_char_tree):
        root = generate_char_tree
        assert root == compute_lca(root, root.left.left, root.right.left)


class TestParentLCA(object):
    """
    Question 10.4
    """

    def test_basic_case(self, generate_tiny_tree):
        """
        Right and left nodes with same parent
        """
        root = generate_tiny_tree
        assert root == compute_parent_lca(
            root.left,
            root.right
        )

    def test_deeper_case(self):
        """
        Deeper case, with two nodes on subtree
        """
        root = TNode(1)
        root.left = TNode(1)
        root.left.parent = root
        root.right = TNode(1)
        root.right.parent = root
        root.left.left = TNode(1)
        root.left.left.parent = root.left

        assert root == compute_parent_lca(root.left.left, root.right)


class TestSumRootToLeaf(object):
    """
    Question 10.5
    """

    def test_book_example(self, generate_binary_binary_tree):
        paths = [
            int('1000', 2),
            int('1001', 2),
            int('10110', 2),
            int('110011', 2),
            int('11000', 2),
            int('1100', 2),
        ]
        total = sum(paths)
        assert total == sum_root_to_leaf(generate_binary_binary_tree)


class TestHasLeafSum(object):
    """
    Question 10.6
    """

    def test_book_example(self, generate_sum_tree):
        assert has_leaf_sum(generate_sum_tree, 591)
        assert not has_leaf_sum(generate_sum_tree, 500)


class TestGetKthNode(object):
    """
    Question 10.7
    """

    def test_basic_example(self, create_basic_tree):
        assert 4 == get_kth_inorder_record(create_basic_tree, 1)
        assert 7 == get_kth_inorder_record(create_basic_tree, 7)


class TestFindSuccessor(object):
    """
    Question 10.8
    """

    def test_basic_example(self, create_basic_tree):
        root = create_basic_tree
        assert 6 == find_successor(root).val
        assert 2 == find_successor(root.left.left).val


class TestInorderTraversal(object):
    """
    Question 10.9
    """

    def test_char_example(self, generate_char_tree):
        inorder = ['D', 'B', 'E', 'A', 'F', 'C']
        assert inorder == inorder_traversal(generate_char_tree)


class TestReconstructTree(object):
    """
    Question 10.10
    """

    def test_basic_example(self, generate_char_tree):

        inorder = ['D', 'B', 'E', 'A', 'F', 'C']
        preorder = ['A', 'B', 'D', 'E', 'C', 'F']

        reconstruct = reconstruct_tree(preorder, inorder)
        assert check_equal(generate_char_tree, reconstruct)


class TestReconstructPreorder(object):
    """
    Question 10.11
    """

    def test_book_example(self, generate_binary_tree):
        representation = [
            'H', 'B', 'F',
            None, None, 'E',
            'A', None, None,
            None, 'C', None,
            'D', None, 'G',
            'I', None, None,
            None
        ]
        assert check_equal(
            generate_binary_tree,
            reconstruct_preorder(representation)
        )


class TestCreateLeafList(object):
    """
    Question 10.12
    """

    def test_basic_tree(self, create_basic_tree):
        assert [4, 5, 6, 7] == create_leaf_list(create_basic_tree)

    def test_symmetric_tree(self, generate_symmetric_tree):
        assert [3, 3] == create_leaf_list(generate_symmetric_tree)


class TestCalculateTreeExterior(object):
    """
    Question 10.13
    """

    def test_basic_case(self, create_basic_tree):
        expected = [1, 2, 4, 5, 6, 7, 3]
        assert expected == calculate_tree_exterior(create_basic_tree)
