from src.stacks_queues import MaxStack, evaluate_rpn, depth_order
from src.binary_trees import TNode

import pytest

'''
Chapter 9: Stacks and Queues
'''
class TestMaxStack(object):
    '''
    Question 9.1
    '''
    def test_basic_configuration(self):
        '''
        Test basic incrementing list
        '''
        stack = MaxStack()
        for idx in xrange(1,11):
            stack.push(idx)
            assert idx == stack.get_max()

        for idx in xrange(10,0,-1):
            assert idx == stack.get_max()
            assert idx == stack.pop()

    def test_reverse_config(self):
        '''
        Reverse configuration
        '''
        stack = MaxStack()
        for idx in xrange(10,0,-1):
            stack.push(idx)
            assert 10 == stack.get_max()

        for _ in xrange(0,10):
            assert 10 == stack.get_max()
            stack.pop()

class TestRpnEvaluation(object):
    '''
    Question 9.2
    '''
    def test_singleton(self):
        '''
        Test singleton evaluation
        '''
        assert 1729 == evaluate_rpn(['1729'])

    def test_operation(self):
        '''
        Test simple operation
        '''
        assert 738 == evaluate_rpn(['6','123','*'])

    def test_complex_operation(self):
        '''
        Test complex operation
        '''
        assert 15 == evaluate_rpn(['3','4','+','2','*','1','+'])

    def test_division_operation(self):
        '''
        Test complex division operation
        '''
        assert 80 == evaluate_rpn(['8','64','/','640','/'])


@pytest.fixture(scope='module')
def get_book_tree():
    # level 0
    root = TNode(314)

    # level 1
    root.left = TNode(6)
    root.right = TNode(6)

    # level 2
    root.left.left = TNode(271)
    root.left.right = TNode(561)
    root.right.left = TNode(2)
    root.right.right = TNode(271)

    # level 3
    root.left.left.left = TNode(28)
    root.left.left.right = TNode(0)
    root.left.right.right = TNode(3)
    root.right.left.right = TNode(1)
    root.right.right.right = TNode(28)

    # level 4
    root.left.right.right.left = TNode(17)
    root.right.left.right.left = TNode(401)
    root.right.left.right.right = TNode(257)

    # level 5
    root.right.left.right.left.right = TNode(641)
    return root


@pytest.fixture(scope='module')
def get_tiny_tree():
    return Node(23)

class TestDepthOrder(object):
    '''
    Question 9.9
    '''
    def test_book_example(self, get_book_tree):
        expected = [
            [314],           # level 0
            [6,6],           # level 1
            [271,561,2,271], # level 2
            [28,0,3,1,28],   # level 3
            [17,401,257],    # level 4
            [641],           # level 5
        ]

        assert expected == depth_order(get_book_tree)

    def test_tiny_tree(self, get_tiny_tree):
        assert [23] == depth_order(get_tiny_tree)

    def test_tiny_tree(self):
        assert [] == depth_order(None)
