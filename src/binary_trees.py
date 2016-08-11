'''
Chapter 10: Binary Trees
'''

class TNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

def is_balanced(root):
    '''
    Problem 10.1: determine if binary tree is balanced
    '''
    return balanced_helper(root)[0]

def balanced_helper(root):
    '''
    Helper function to return tuple for balancing
    '''
    if not root:
        return (True, 0)
    left = balanced_helper(root.left)
    right = balanced_helper(root.right)

    return (
        left[0] and right[0] and abs(left[1] - right[1]) <= 1,
        1 + max(left[1], right[1]),
    )

def compute_parent_lca(first_tree, second_tree):
    '''
    Problem 10.4: Get least common ancestor if nodes
    have parent pointer
    '''
    if first_tree.parent == second_tree.parent:
        return first_tree.parent
    return None
