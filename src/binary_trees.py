'''
Chapter 10: Binary Trees
'''


class TNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


def check_equal(root_one, root_two):
    '''
    Check that two binary trees are equal
    '''
    if root_one is None and root_two is None:
        return True
    elif (root_one is None and root_two is not None) \
            or (root_one is not None and root_two is None):
        return False
    elif root_one.val != root_two.val:
        return False
    else:
        return check_equal(root_one.left, root_two.left) and \
            check_equal(root_one.right, root_two.right)


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


def is_symmetric(root):
    '''
    Question 10.2: check if binary tree is symmetric
    '''
    return root is None or check_symmetric(root.left, root.right)


def check_symmetric(left, right):
    '''
    Helper function to recursively check symmetry of subtrees
    '''
    if left is None and right is None:
        return True
    elif (left is None and right is not None) or \
            (left is not None and right is None):
        return False
    elif left.val != right.val:
        return False
    else:
        return check_symmetric(left.left, right.right) and \
            check_symmetric(left.right, right.left)


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
        second = tmp

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


def reconstruct_tree(preorder, inorder):
    '''
    Question 10.10
    '''
    node_to_inorder_idx = {}
    for idx, elt in enumerate(inorder):
        node_to_inorder_idx[elt] = idx

    return reconstruct_helper(
        preorder, 0, len(preorder),
        0, len(inorder), node_to_inorder_idx,
    )


def reconstruct_helper(
    preorder, preorder_start, preorder_end,
    inorder_start, inorder_end, node_to_inorder_idx,
):
    if preorder_end <= preorder_start or inorder_end <= inorder_start:
        return None

    # first element in preorder is root
    root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
    left_subtree_size = root_inorder_idx - inorder_start

    root = TNode(preorder[preorder_start])
    root.left = reconstruct_helper(
        preorder, preorder_start + 1, preorder_start + 1 + left_subtree_size,
        inorder_start, root_inorder_idx, node_to_inorder_idx,
    )
    root.right = reconstruct_helper(
        preorder, preorder_start + 1 + left_subtree_size, preorder_end,
        root_inorder_idx + 1, inorder_end, node_to_inorder_idx,
    )
    return root
