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

def compute_parent_lca(first, second):
    '''
    Problem 10.4: Get least common ancestor if nodes
    have parent pointer
    '''
    first_depth = get_depth(first)
    second_depth = get_depth(second)

    # swap if second deeper than first
    if second_depth > first_depth:
        tmp = first
        first = second
        second = first

    depth_diff = abs(first_depth - second_depth)
    while depth_diff:
        first = first.parent
        depth_diff -= 1

    while first != second:
        first = first.parent
        second = second.parent

    return first

def get_depth(node):
    '''
    Helper function to get depth of node
    from root
    '''
    depth = 0
    while node.parent:
        node = node.parent
        depth += 1
    return depth
