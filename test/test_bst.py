from src.bst import BST, check_bst

def TestCheckBST:
    '''
    Question 15.1
    '''
    def test_correct_example(self):
        root = BST(19)
        # level 1
        root.left = BST(7)
        root.right = BST(43)
        # level 2
        root.left.left = BST(3)
        root.left.right = BST(11)
        root.right.left = BST(23)
        root.right.right = BST(47)
        # level 3
        root.left.left.left = BST(2)
        root.left.left.right = BST(5)
        root.left.right.right = BST(17)
        root.right.left.right = BST(37)
        root.right.right.right = BST(53)
        # level 4
        root.left.right.right.left = BST(13)
        root.right.left.right.left = BST(29)
        root.right.left.right.right = BST(41)
        # level 5
        root.right.left.right.left.right = BST(31)

        assert check_bst(root)
