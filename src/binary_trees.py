"""
Chapter 10: Binary Trees
"""


class TNode(object):

    def __init__(self, val, node_id=None):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.node_id = node_id


def check_equal(root_one, root_two):
    """
    Check that two binary trees are equal
    """
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
    """
    Problem 10.1: determine if binary tree is balanced
    """
    return balanced_helper(root)[0]


def balanced_helper(root):
    """
    Helper function to return tuple for balancing
    """
    if not root:
        return (True, 0)
    left = balanced_helper(root.left)
    right = balanced_helper(root.right)

    return (
        left[0] and right[0] and abs(left[1] - right[1]) <= 1,
        1 + max(left[1], right[1]),
    )


def is_symmetric(root):
    """
    Question 10.2: check if binary tree is symmetric
    """
    return root is None or check_symmetric(root.left, root.right)


def check_symmetric(left, right):
    """
    Helper function to recursively check symmetry of subtrees
    """
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


def compute_lca(root, first, second):
    """
    Question 10.3: Compute the lowest
    common ancestor in a binary tree
    """
    _, lca = compute_lca_helper(root, first, second)
    return lca


def compute_lca_helper(root, first, second):
    """
    Helper that returns
    """
    if root is None:
        return 0, None

    # get left subtree
    left_nodes, left_lca = compute_lca_helper(
        root.left,
        first,
        second
    )
    if left_nodes == 2:
        return left_nodes, left_lca

    right_nodes, right_lca = compute_lca_helper(
        root.right,
        first,
        second
    )

    if right_nodes == 2:
        return right_nodes, right_lca

    num_nodes = left_nodes + right_nodes + \
        (root == first) + (root == second)
    lca = root if num_nodes == 2 else None

    return num_nodes, lca


def compute_parent_lca(first, second):
    """
    Problem 10.4: Get least common ancestor if nodes
    have parent pointer
    """
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
    """
    Helper function to get depth of node
    from root
    """
    depth = 0
    while node.parent:
        node = node.parent
        depth += 1
    return depth


def sum_root_to_leaf(root):
    """
    Question 10.5: Sum all root to
    leaf paths, given that all paths
    represent binary numbers
    """
    return sum_root_helper(root, 0)


def sum_root_helper(root, partial_sum):
    """
    Helper to keep track of partial sums as
    getting remainder of root to leaf sums
    """
    if root is None:
        return 0

    partial_sum = partial_sum * 2 + root.val
    if not root.right and not root.left:
        return partial_sum

    return sum_root_helper(root.right, partial_sum) + \
        sum_root_helper(root.left, partial_sum)


def has_leaf_sum(root, target):
    """
    Question 10.6: Check that there exists a
    root-to-leaf path that sums to the target
    """
    return has_leaf_sum_helper(root, target, 0)


def has_leaf_sum_helper(root, target, partial_sum):
    """
    Helper function to keep track of partial
    sum while trying to hit target
    """
    if root is None:
        return False

    partial_sum += root.val
    if partial_sum == target:
        return True

    return has_leaf_sum_helper(root.left, target, partial_sum) or \
        has_leaf_sum_helper(root.right, target, partial_sum)


def get_kth_inorder_record(root, k):
    """
    Question 10.7
    """
    current_num = 0
    cur = root
    prev = None

    while cur:
        next_node = None
        if cur.parent == prev:
            if cur.left:
                next_node = cur.left
            else:
                current_num += 1
                if current_num == k:
                    return cur.val
                next_node = cur.right if cur.right else cur.parent
        elif cur.left == prev:
            current_num += 1
            if current_num == k:
                return cur.val
            next_node = cur.right if cur.right else cur.parent
        else:
            next_node = cur.parent
        prev = cur
        cur = next_node
    return None


def find_successor(node):
    """
    Question 10.8: Compute the successor
    of the given node in the inorder traversal
    of the tree
    """
    if node.right is not None:
        cur = node.right

        # recurse down to left-most node
        # in right subtree
        while cur.left:
            cur = cur.left
        return cur

    while node.parent and node.parent.right == node:
        node = node.parent

    return node.parent


def inorder_traversal(root):
    """
    Question 10.9: Implement an
    inorder traversal in O(1) space
    """
    elts = []
    cur = root
    prev = None

    while cur:
        next_node = None
        if cur.parent == prev:
            # came down to cur from prev
            if cur.left:
                next_node = cur.left
            else:
                elts.append(cur.val)
                # done with left, so go up if
                # right is not empty
                # otherwise go up
                next_node = cur.right if cur.right else cur.parent
        elif cur.left == prev:
            # came up to cur from left child
            elts.append(cur.val)
            next_node = cur.right if cur.right else cur.parent
        else:
            # done with both children so move up
            next_node = cur.parent
        prev = cur
        cur = next_node
    return elts


def reconstruct_tree(preorder, inorder):
    """
    Question 10.10
    """
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


def reconstruct_preorder(preorder):
    """
    Question 10.11: Reconstruct binary tree from
    a preorder representation with markers
    """

    subtree_idx = 0
    root, _ = reconstruct_preorder_helper(preorder, subtree_idx)
    return root


def reconstruct_preorder_helper(preorder, subtree_idx):
    """
    Recursive helper to construct subtree
    """
    subtree_key = TNode(preorder[subtree_idx]) if preorder[
        subtree_idx] else None
    subtree_idx += 1
    if subtree_key is None:
        return None, subtree_idx

    left_subtree, left_idx = reconstruct_preorder_helper(preorder, subtree_idx)
    right_subtree, right_idx = reconstruct_preorder_helper(preorder, left_idx)
    subtree_key.left = left_subtree
    subtree_key.right = right_subtree

    return subtree_key, right_idx


def create_leaf_list(root):
    """
    Question 10.12: Create list from leaves
    of binary tree
    """
    if root.left is None and root.right is None:
        return [root.val]

    ls = []
    if root.left is not None:
        ls.extend(create_leaf_list(root.left))
    if root.right is not None:
        ls.extend(create_leaf_list(root.right))
    return ls
