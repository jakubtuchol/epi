from sys import maxint

class BST(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def check_bst(root):
    INT_MAX = maxint
    INT_MIN = -maxint - 1
    '''
    Question 15.1: Test if a binary tree satisfies the BST property
    '''
    return check_bst_helper(root, INT_MIN, INT_MAX)

def check_bst_helper(root, low, high):
    if not root:
        return True

    if root.val < low or root.val > high:
        return False

    return check_bst_helper(root.left, low, root.val-1) \
            and check_bst_helper(root.right, root.val+1, high)

def find_first_larger_key(root, key):
    '''
    Question 15.3: Find the first key larger than given
    value in bst
    '''
    return root.val
