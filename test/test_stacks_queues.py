"""
Chapter 9: Stacks and Queues
"""
import pytest

from src.binary_trees import TNode
from src.stacks_queues import balanced_parentheses
from src.stacks_queues import CircularQueue
from src.stacks_queues import depth_order
from src.stacks_queues import evaluate_rpn
from src.stacks_queues import MaxStack


class TestMaxStack(object):
    """
    Question 9.1
    """

    def test_basic_configuration(self):
        """
        Test basic incrementing list
        """
        stack = MaxStack()
        for idx in xrange(1, 11):
            stack.push(idx)
            assert idx == stack.get_max()

        for idx in xrange(10, 0, -1):
            assert idx == stack.get_max()
            assert idx == stack.pop()

    def test_reverse_config(self):
        """
        Reverse configuration
        """
        stack = MaxStack()
        for idx in xrange(10, 0, -1):
            stack.push(idx)
            assert 10 == stack.get_max()

        for _ in xrange(0, 10):
            assert 10 == stack.get_max()
            stack.pop()


class TestRpnEvaluation(object):
    """
    Question 9.2
    """

    def test_singleton(self):
        """
        Test singleton evaluation
        """
        assert 1729 == evaluate_rpn(['1729'])

    def test_operation(self):
        """
        Test simple operation
        """
        assert 738 == evaluate_rpn(['6', '123', '*'])

    def test_complex_operation(self):
        """
        Test complex operation
        """
        assert 15 == evaluate_rpn(['3', '4', '+', '2', '*', '1', '+'])

    def test_division_operation(self):
        """
        Test complex division operation
        """
        assert 80 == evaluate_rpn(['8', '64', '/', '640', '/'])


class TestBalancedParentheses(object):
    """
    Question 9.3
    """

    def test_well_formed_strings(self):
        assert balanced_parentheses('([]){()}')
        assert balanced_parentheses('[()[]{()()}]')

    def test_ill_formed_strings(self):
        assert not balanced_parentheses('{)')
        assert not balanced_parentheses('[()[]{()()')


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
    return TNode(23)


class TestDepthOrder(object):
    """
    Question 9.9
    """

    def test_book_example(self, get_book_tree):
        expected = [
            [314],           # level 0
            [6, 6],           # level 1
            [271, 561, 2, 271],  # level 2
            [28, 0, 3, 1, 28],   # level 3
            [17, 401, 257],    # level 4
            [641],           # level 5
        ]

        assert expected == depth_order(get_book_tree)

    def test_tiny_tree(self, get_tiny_tree):
        assert [[23]] == depth_order(get_tiny_tree)

    def test_nullary_tree(self):
        assert [] == depth_order(None)


class TestCircularQueue(object):
    """
    Question 9.10
    """

    def test_basic_case(self):
        cqueue = CircularQueue(10)

        for idx in xrange(10):
            assert idx == cqueue.size
            cqueue.enqueue(idx)
            assert idx + 1 == cqueue.size

        for idx in xrange(10):
            assert 10 - idx == cqueue.size
            assert idx == cqueue.dequeue()
            assert 10 - idx - 1 == cqueue.size

    def test_overflow_case(self):
        cqueue = CircularQueue(10)

        with pytest.raises(
            Exception,
            message='queue is currently at capacity'
        ):
            for idx in xrange(11):
                cqueue.enqueue(idx)

    def test_overwrite_case(self):
        cqueue = CircularQueue(10)
        for idx in xrange(10):
            cqueue.enqueue(idx)

        assert 0 == cqueue.tail
        assert 0 == cqueue.head
        assert 0 == cqueue.dequeue()
        assert 0 == cqueue.tail
        assert 1 == cqueue.head
        cqueue.enqueue(11)
        assert 1 == cqueue.tail
        assert 1 == cqueue.head
        assert 11 == cqueue.contents[0]
