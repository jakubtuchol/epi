"""
Chapter 15: Binary Search Trees
"""
from sys import maxint


class BST(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def check_bst(root):
    """
    Question 15.1: Test if a binary tree satisfies the BST property
    """
    INT_MAX = maxint
    INT_MIN = -maxint - 1
    return check_bst_helper(root, INT_MIN, INT_MAX)


def check_bst_helper(root, low, high):
    if not root:
        return True

    if root.val < low or root.val > high:
        return False

    return check_bst_helper(root.left, low, root.val - 1) \
        and check_bst_helper(root.right, root.val + 1, high)


def find_first_larger_key(root, key):
    """
    Question 15.3: Find the first key larger than given
    value in bst
    """
    larger = None
    while root:
        if root.val > key:
            # check if larger defined
            larger = root.val
            root = root.left
        else:
            root = root.right
    return larger


def find_largest_keys(root, k):
    """
    Question 15.4: Find k largest keys in bst
    """
    largest = []
    stack = []
    done = False

    while not done and len(largest) < k:
        if root:
            stack.append(root)
            root = root.right
        else:
            if len(stack):
                root = stack.pop()
                largest.insert(0, root.val)
                root = root.left
            else:
                done = True
    return largest


def find_lca(root, a, b):
    """
    Question 15.5: Compute the LCA in a BST
    """
    smaller = min(a, b)
    larger = max(a, b)

    cur_node = root

    while cur_node.val > larger or cur_node.val < smaller:
        if cur_node.val > larger:
            if cur_node.left:
                cur_node = cur_node.left
            else:
                return None
        if cur_node.val < smaller:
            if cur_node.right:
                cur_node = cur_node.right
            else:
                return None
    return cur_node.val
