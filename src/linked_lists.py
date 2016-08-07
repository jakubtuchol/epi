'''
Chapter 8: Linked Lists
'''

class Node(object):
    def __init__(self, value):
        self.val = value
        self.next = None

def merge_sorted_lists(ls_1, ls_2):
    '''
    Question 8.1: merge two sorted singly-linked lists
    '''
    dummy_head = Node(1000000)
    tail = dummy_head

    while ls_1 and ls_2:
        # both ls_1 and ls_2 are present
        if ls_1.val <= ls_2.val:
            tail.next = ls_1
            ls_1 = ls_1.next
        else:
            tail.next = ls_2
            ls_2 = ls_2.next
        tail = tail.next

    tail.next = ls_1 or ls_2

    return dummy_head.next

def reverse_linked_list(ls):
    '''
    Question 8.2: Reverse a linked list using O(1) space and O(n) time
    '''
    prev = ls.next
    cur = prev
    head = ls

    while prev:
        # retain pointer to current node
        cur = prev
        prev = prev.next
        cur.next = head
        head = cur

    return head
