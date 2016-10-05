"""
Chapter 8: Linked Lists
"""


class Node(object):

    def __init__(self, value):
        self.val = value
        self.next = None


def merge_sorted_lists(ls_1, ls_2):
    """
    Question 8.1: merge two sorted singly-linked lists
    """
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
    """
    Question 8.2: Reverse a linked list using O(1) space and O(n) time
    """
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


def reverse_sublist(ls, begin, end):
    """
    Question 8.3: Reverse a sublist of the input
    list denoted by the beginning index and the end
    index, inclusive. The list numbering begins at 0
    """
    # don't process nonsensical inputs
    if ls is None or end <= begin:
        return ls

    rev_len = end - begin + 1
    # advance pointer to just prior to sublist head
    pre_rev_head = None
    rev_head = ls
    while begin:
        begin -= 1
        pre_rev_head = rev_head
        rev_head = rev_head.next

    prev = rev_head
    next = None
    head = None

    while rev_len:
        head = prev
        prev = prev.next
        head.next = next
        next = head
        rev_len -= 1

    rev_head.next = prev
    pre_rev_head.next = head
    return ls


def detect_cycle(head):
    """
    Question 8.4: Detect a cycle in a singly-linked list.
    Return None if there is no cycle.
    If there is, return the first node in the cycle.
    """
    slow = head
    fast = head

    cycle_length = 0
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            cycle_length = 1
            fast = fast.next

            while fast != slow:
                fast = fast.next
                cycle_length += 1

            advanced_ptr = head
            while cycle_length:
                advanced_ptr = advanced_ptr.next
                cycle_length -= 1

            iterator = head
            # advance both pointers in tandem
            while iterator != advanced_ptr:
                iterator = iterator.next
                advanced_ptr = advanced_ptr.next
            return iterator

    return None


def find_overlap(ls_one, ls_two):
    """
    Question 8.5: Find overlap in two linked lists
    without cycles
    """
    # find length of list one
    len_one = 0
    len_two = 0
    head_one = ls_one
    head_two = ls_two

    while head_one:
        head_one = head_one.next
        len_one += 1

    while head_two:
        head_two = head_two.next
        len_two += 1

    diff = abs(len_one - len_two)

    while diff:
        ls_one = ls_one.next
        ls_two = ls_two.next
        diff -= 1

    while ls_one != ls_two:
        ls_one = ls_one.next
        ls_two = ls_two.next

    return ls_one


def find_overlap_cycle(ls_one, ls_two):
    """
    Question 8.6: Find overlap in two linked lists
    with cycles
    """
    cycle_one = detect_cycle(ls_one)
    cycle_two = detect_cycle(ls_two)

    if not cycle_one and not cycle_two:
        return find_overlap(cycle_one, cycle_two)
    elif (cycle_one and not cycle_two) or (not cycle_one and cycle_two):
        return None

    temp = cycle_two

    while True:
        temp = temp.next

        if temp == cycle_one or temp == cycle_two:
            break

    if temp != cycle_one:
        return None

    # both one and two end in same cycle, so check if
    # they overlap before cycle
    stem_one = get_node_distance(ls_one, cycle_one)
    stem_two = get_node_distance(ls_two, cycle_two)

    uneven_distance = abs(stem_one - stem_two)

    if stem_one > stem_two:
        ls_one = advance_list(ls_one, uneven_distance)
    else:
        ls_two = advance_list(ls_two, uneven_distance)

    while ls_one != ls_two and ls_one != cycle_one and ls_two != cycle_two:
        ls_one = ls_one.next
        ls_two = ls_two.next

    return ls_one if ls_one == ls_two else cycle_one


def get_node_distance(a, b):
    distance = 0

    while a != b:
        a = a.next
        distance += 1
    return distance


def delete_node(node):
    """
    Question 8.7: Delete node in O(1)
    time
    """
    node.val = node.next.val
    node.next = node.next.next


def advance_list(node, k):
    while k:
        node = node.next
        k -= 1
    return node


def remove_kth_last_element(ls, k):
    """
    Question 8.8: Remove kth element from
    end of list
    """
    # first advance first pointer by k
    # then advance first and second pointer in tandem
    fast_runner = ls
    slow_runner = ls
    head = slow_runner

    while k:
        fast_runner = fast_runner.next
        k -= 1

    while fast_runner:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next

    if slow_runner and slow_runner.next:
        slow_runner.next = slow_runner.next.next

    return head


def remove_duplicates(ls):
    """
    Question 8.9: Remove duplicates from
    sorted list
    """
    head = ls
    last = ls
    cur = ls.next

    while cur:
        if last.val != cur.val:
            last.next = cur
            last = cur
        cur = cur.next
    last.next = None
    return head


def cyclic_right_shift(ls, n):
    """
    Question 8.10: Implement cyclic right shift
    for singly linked lists
    """
    if ls is None:
        return ls

    slow = ls
    runner = ls

    # increment runner by n
    for _ in xrange(n):
        runner = runner.next

    while runner.next:
        slow = slow.next
        runner = runner.next

    # slow should now point to
    # node that is n+1 away from end
    new_head = slow.next
    runner.next = ls
    slow.next = None

    return new_head


def even_odd_merge(ls):
    """
    Question 8.11: merge list such that
    even-number nodes are followed by odd-number
    nodes
    """
    even_head = Node(None)
    cur_even = even_head
    odd_head = Node(None)
    cur_odd = odd_head

    idx = 0

    while ls:
        if idx % 2 == 0:
            cur_even.next = ls
            cur_even = cur_even.next
        else:
            cur_odd.next = ls
            cur_odd = cur_odd.next
        ls = ls.next
        idx += 1
    cur_even.next = odd_head.next
    cur_odd.next = None

    return even_head.next


def check_list_palindrome(ls):
    """
    Question 8.12: Check whether singly-linked
    list is a palindrome
    """
    if ls is None:
        return True

    slow = ls
    fast = ls
    first_half = []

    while fast and fast.next:
        first_half.append(slow.val)
        slow = slow.next
        fast = fast.next.next

    slow = slow.next
    first_half.reverse()
    idx = 0 if first_half[0] == slow.val else 1

    while idx < len(first_half) and slow:
        if first_half[idx] != slow.val:
            return False
        slow = slow.next
        idx += 1

    return True


def pivot_list(ls, k):
    """
    Question 8.13: Implement list pivoting, such that all
    values less than k will appear first, then all nodes
    equal to k, then all nodes greater than k
    """
    # creating fake heads for each of nodes
    less_fake = Node(None)
    greater_fake = Node(None)
    equal_fake = Node(None)

    # creating heads for each node
    less_head = less_fake
    greater_head = greater_fake
    equal_head = equal_fake

    while ls:
        if ls.val < k:
            less_head.next = ls
            less_head = less_head.next
        elif ls.val > k:
            greater_head.next = ls
            greater_head = greater_head.next
        else:
            equal_head.next = ls
            equal_head = equal_head.next
        ls = ls.next
    less_head.next = equal_fake.next
    equal_head.next = greater_fake.next
    greater_head.next = None
    return less_fake.next
