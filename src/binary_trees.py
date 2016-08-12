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
    return lca_helper(first_tree, second_tree, set())

def lca_helper(first_tree, second_tree, seen_nodes):
    '''
    Helper function that keeps track of seen nodes for
    tree traversal
    '''
    if first_tree == second_tree:
        return first_tree

    if first_tree in seen_nodes:
        return first_tree
    if second_tree in seen_nodes:
        return second_tree

    seen_nodes.add(first_tree)
    seen_nodes.add(second_tree)
    return lca_helper(
        first_tree.parent if first_,
        second_tree.parent,
        seen_nodes,
    )
