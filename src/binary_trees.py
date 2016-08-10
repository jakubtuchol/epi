'''
Chapter 10: Binary Trees
'''

class TNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_balanced(root):
    '''
    Problem 10.1: determine if binary tree is balanced
    '''
    return balanced_helper(root)[0]

def balanced_helper(root):
    if not root:
        return (True, 0)
    left = balanced_helper(root.left)
    right = balanced_helper(root.right)
    print('left is {}', left[1])
    print('right is {}', right[1])
    print('diff is {}', abs(left[1] - right[1]))

    return (
        left[0] and right[0] and abs(left[1] - right[1]) <= 1,
        1 + max(left[1], right[1]),
    )
