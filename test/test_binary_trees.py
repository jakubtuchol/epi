from src.binary_trees import TNode, is_balanced, compute_parent_lca

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
