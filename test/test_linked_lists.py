import pytest

from src.linked_lists import add_list_numbers
from src.linked_lists import check_list_palindrome
from src.linked_lists import cyclic_right_shift
from src.linked_lists import delete_node
from src.linked_lists import detect_cycle
from src.linked_lists import even_odd_merge
from src.linked_lists import find_overlap
from src.linked_lists import find_overlap_cycle
from src.linked_lists import merge_sorted_lists
from src.linked_lists import Node
from src.linked_lists import pivot_list
from src.linked_lists import remove_duplicates
from src.linked_lists import remove_kth_last_element
from src.linked_lists import reverse_linked_list
from src.linked_lists import reverse_sublist


# Fixtures
@pytest.fixture
def create_list():
    dummy = Node(None)
    head = dummy

    for idx in xrange(10):
        dummy.next = Node(idx)
        dummy = dummy.next

    return head.next


# Tests
class TestMergeLinkedLists(object):
    """
    Question 8.1
    """

    def test_append_case(self):
        """
        Basic test providing two linked lists, both
        already sorted and in order
        """
        head_1 = Node(1)
        cur_1 = head_1
        for i in xrange(2, 11):
            cur_1.next = Node(i)
            cur_1 = cur_1.next

        head_2 = Node(11)
        cur_2 = head_2
        for i in xrange(12, 21):
            cur_2.next = Node(i)
            cur_2 = cur_2.next

        merge_head = merge_sorted_lists(head_2, head_1)
        for i in xrange(1, 21):
            assert merge_head.val == i
            merge_head = merge_head.next

    def test_interleaving_case(self):
        """
        Test for two linked lists with interleaving values
        """
        head_1 = Node(1)
        cur_1 = head_1
        for i in xrange(3, 21, 2):
            cur_1.next = Node(i)
            cur_1 = cur_1.next

        head_2 = Node(2)
        cur_2 = head_2
        for i in xrange(4, 21, 2):
            cur_2.next = Node(i)
            cur_2 = cur_2.next

        merge_head = merge_sorted_lists(head_1, head_2)
        for i in xrange(1, 21):
            assert merge_head.val == i
            merge_head = merge_head.next


class TestReverseLinkedList(object):
    """
    Question 8.2
    """

    def test_basic_incremental(self):
        """
        Test for basic presorted list
        """
        head = Node(1)
        cur = head
        for i in xrange(2, 11):
            cur.next = Node(i)
            cur = cur.next

        rev_head = reverse_linked_list(head)
        for i in xrange(10, 0, -1):
            assert i == rev_head.val
            rev_head = rev_head.next

        assert rev_head is None


class TestReverseSublist(object):
    """
    Question 8.3
    """

    def test_basic_case(self, create_list):
        head = create_list
        rev = reverse_sublist(head, 1, 5)

        assert 0 == rev.val
        rev = rev.next

        for idx in xrange(5, 0, -1):
            assert idx == rev.val
            rev = rev.next

        for idx in xrange(6, 10):
            assert idx == rev.val
            rev = rev.next

        assert rev is None

    def test_incorrect_cases(self, create_list):
        head = create_list
        assert head == reverse_sublist(head, 4, 2)

    def test_none_input(self):
        assert reverse_sublist(None, 1, 8) is None


class TestCyclicTest(object):
    """
    Question 8.4
    """

    def test_basic_cycle(self):
        """
        Testing very simple cycle
        """
        head = Node(1)
        cur = head
        for i in xrange(2, 11):
            cur.next = Node(i)
            cur = cur.next
        cur.next = head

        cycle = detect_cycle(head)
        assert cycle == head

        cur.next = head.next
        cycle = detect_cycle(head)
        assert cycle == head.next


class TestOverlappingLists(object):
    """
    Question 8.5
    """

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
        assert find_overlap(one, two) is None


class TestFindOverlapCycle(object):
    """
    Question 8.6
    """

    def test_book_case(self):
        head_one = Node('A')
        head_one.next = Node('B')

        head_two = Node('C')
        head_two.next = Node('D')

        cross_node = Node('E')
        cross_node.next = Node('F')
        cross_node.next.next = Node('G')
        cross_node.next.next.next = head_two.next

        head_one.next.next = cross_node
        head_two.next.next = cross_node

        assert cross_node == find_overlap_cycle(head_one, head_two)

    def test_non_cycle_overlap(self):
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


class TestDeleteNode(object):
    """
    Question 8.7
    """

    def test_basic_example(self):
        del_node = None
        dummy = Node(None)
        head = dummy

        for idx in xrange(10):
            dummy.next = Node(idx)
            dummy = dummy.next
            if idx == 5:
                del_node = dummy

        head = head.next
        delete_node(del_node)

        for idx in xrange(10):
            if idx != 5:
                assert idx == head.val
                head = head.next
            else:
                assert 6 == head.val


class TestRemoveKthElement(object):
    """
    Question 8.8
    """

    def test_remove_kth_element(self, create_list):
        remove = remove_kth_last_element(create_list, 3)

        for idx in xrange(8):
            assert idx == remove.val
            remove = remove.next

        for idx in xrange(9, 10):
            assert idx == remove.val
            remove = remove.next

        assert remove is None

    def test_remove_last_element(self, create_list):
        remove = remove_kth_last_element(create_list, 1)

        for idx in xrange(10):
            assert idx == remove.val
            remove = remove.next

        assert remove is None


class TestRemoveDuplicates(object):
    """
    Question 8.9
    """

    def test_book_example(self):
        head = Node(None)
        cur = head
        for elt in [2, 2, 3, 5, 7, 11, 11]:
            cur.next = Node(elt)
            cur = cur.next

        head = head.next
        head = remove_duplicates(head)
        for elt in [2, 3, 5, 7, 11]:
            assert elt == head.val
            head = head.next

        assert not head


class TestCyclicRightShift(object):
    """
    Question 8.10
    """

    def test_incrementing_input(self, create_list):
        head = cyclic_right_shift(create_list, 5)

        for idx in xrange(5, 10):
            assert idx == head.val
            head = head.next

        for idx in xrange(5):
            assert idx == head.val
            head = head.next

        assert head is None

    def test_none_case(self):
        assert cyclic_right_shift(None, 8) is None


class TestEvenOddMerge(object):
    """
    Question 8.11
    """

    def test_book_case(self):
        head = Node(0)
        cur_node = head

        for idx in xrange(1, 10):
            cur_node.next = Node(idx)
            cur_node = cur_node.next

        merged = even_odd_merge(head)

        for even_idx in xrange(0, 10, 2):
            assert even_idx == merged.val
            merged = merged.next

        for odd_idx in xrange(1, 10, 2):
            assert odd_idx == merged.val
            merged = merged.next

        assert merged is None


class TestCheckListPalindrome(object):
    """
    Question 8.12
    """

    def test_null_case(self):
        assert check_list_palindrome(None)

    def test_even_length_case(self):
        head = Node(None)
        cur_node = head

        for idx in xrange(5):
            cur_node.next = Node(idx)
            cur_node = cur_node.next

        for idx in xrange(5, -1, -1):
            cur_node.next = Node(idx)
            cur_node = cur_node.next

        assert check_list_palindrome(head.next)

    def test_odd_length_case(self):
        head = Node(None)
        cur_node = head

        for idx in xrange(5):
            cur_node.next = Node(idx)
            cur_node = cur_node.next

        cur_node.next = Node(6)
        cur_node = cur_node.next

        for idx in xrange(5, -1, -1):
            cur_node.next = Node(idx)
            cur_node = cur_node.next

        assert check_list_palindrome(head.next)

    def test_bad_length(self):
        head = Node(None)
        cur_node = head

        for idx in xrange(5):
            cur_node.next = Node(idx)
            cur_node = cur_node.next

        cur_node.next = Node(6)
        cur_node = cur_node.next

        cur_node.next = Node(7)
        cur_node = cur_node.next

        for idx in xrange(5, -1, -1):
            cur_node.next = Node(idx)
            cur_node = cur_node.next

        assert not check_list_palindrome(head.next)


class TestPivotList(object):
    """
    Question 8.13
    """

    def test_book_example(self):
        nodes = [3, 2, 2, 11, 7, 5, 11]
        res = [3, 2, 2, 5, 7, 11, 11]

        fake_head = Node(None)
        head = fake_head
        for idx in nodes:
            head.next = Node(idx)
            head = head.next
        head = fake_head.next

        new_head = pivot_list(head, 7)

        for idx in res:
            assert idx == new_head.val
            new_head = new_head.next

        assert new_head is None


class TestAddListNumbers(object):
    """
    Question 8.14
    """

    def test_book_example(self):
        fake_one = Node(None)
        head_one = fake_one
        for elt in [3, 1, 4]:
            head_one.next = Node(elt)
            head_one = head_one.next
        head_one = fake_one.next

        fake_two = Node(None)
        head_two = fake_two
        for elt in [7, 0, 9]:
            head_two.next = Node(elt)
            head_two = head_two.next
        head_two = fake_two.next

        add_head = add_list_numbers(head_one, head_two)

        for elt in [0, 2, 3, 1]:
            assert elt == add_head.val
            add_head = add_head.next
        assert add_head is None

    def test_nines_example(self):
        fake_head = Node(None)
        head = fake_head
        for elt in [9, 9, 9, 9]:
            head.next = Node(elt)
            head = head.next

        one = Node(1)

        added = add_list_numbers(fake_head.next, one)

        for elt in [0, 0, 0, 0, 1]:
            assert elt == added.val
            added = added.next
        assert added is None
