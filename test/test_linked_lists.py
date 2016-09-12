from src.linked_lists import Node, merge_sorted_lists, reverse_linked_list, \
        detect_cycle, find_overlap

class TestMergeLinkedLists(object):
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

class TestReverseLinkedList(object):
    '''
    Question 8.2
    '''
    def test_basic_incremental(self):
        '''
        Test for basic presorted list
        '''
        head = Node(1)
        cur = head
        for i in xrange(2,11):
            cur.next = Node(i)
            cur = cur.next

        rev_head = reverse_linked_list(head)
        for i in xrange(10,0,-1):
            assert i == rev_head.val
            rev_head = rev_head.next

class TestCyclicTest(object):
    '''
    Question 8.4
    '''
    def test_basic_cycle(self):
        '''
        Testing very simple cycle
        '''
        head = Node(1)
        cur = head
        for i in xrange(2,11):
            cur.next = Node(i)
            cur = cur.next
        cur.next = head

        cycle = detect_cycle(head)
        assert cycle == head

        cur.next = head.next
        cycle = detect_cycle(head)
        assert cycle == head.next

class TestOverlappingLists(object):
    '''
    Question 8.5
    '''
    def test_book_case(self):
        head_one = Node('A')
        head_one.next = Node('B')

        head_two = Node('J')
        head_two.next = Node('K')

        cross_node = Node('C')
        cross_node.next = Node('D')
        cross_node.next.next = Node('E')
        head_one.next.next = cross_node
        head_two.next.next = cross_node

        assert cross_node == find_overlap(head_one, head_two)

    def test_non_overlapping_case(self):
        one = Node('A')
        two = Node('B')
        assert None == find_overlap(one, two)
