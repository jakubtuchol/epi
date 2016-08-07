from src.linked_lists import Node, merge_sorted_lists

class TestMergeLinkedLists:
    '''
    Question 8.1
    '''
    def test_append_case(self):
        '''
        Basic test providing two linked lists, both
        already sorted and in order
        '''
        head_1 = Node(1)
        cur_1 = head_1
        for i in xrange(2,11):
            cur_1.next = Node(i)
            cur_1 = cur_1.next

        head_2 = Node(11)
        cur_2 = head_2
        for i in xrange(12,21):
            cur_2.next = Node(i)
            cur_2 = cur_2.next

        merge_head = merge_sorted_lists(head_2, head_1)
        for i in xrange(1,21):
            assert merge_head.val == i
            merge_head = merge_head.next

    def test_interleaving_case(self):
        '''
        Test for two linked lists with interleaving values
        '''
        head_1 = Node(1)
        cur_1 = head_1
        for i in xrange(3,21,2):
            cur_1.next = Node(i)
            cur_1 = cur_1.next

        head_2 = Node(2)
        cur_2 = head_2
        for i in xrange(4,21,2):
            cur_2.next = Node(i)
            cur_2 = cur_2.next

        merge_head = merge_sorted_lists(head_1, head_2)
        for i in xrange(1,21):
            assert merge_head.val == i
            merge_head = merge_head.next
