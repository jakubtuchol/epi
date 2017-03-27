"""
Chapter 9: Stacks and Queues
"""
from collections import deque


class MaxStack(object):
    """
    Question 9.1
    """

    def __init__(self):
        self.contents = []
        self.max_at = [0]

    def push(self, elt):
        cur_max = self.max_at[-1]
        if cur_max >= elt:
            self.max_at.append(cur_max)
        else:
            self.max_at.append(elt)
        self.contents.append(elt)

    def pop(self):
        self.max_at.pop()
        return self.contents.pop()

    def get_max(self):
        return self.max_at[-1]


def evaluate_rpn(ls):
    """
    Question 9.2
    """
    tokens = []
    for token in ls:
        if token in '+-/*':
            tk_1 = tokens.pop()
            tk_2 = tokens.pop()

            if token == '+':
                tokens.append(tk_1 + tk_2)
            elif token == '-':
                tokens.append(tk_1 - tk_2)
            elif token == '*':
                tokens.append(tk_1 * tk_2)
            elif token == '/':
                tokens.append(tk_1 / tk_2)
        else:
            tokens.append(int(token))
    return tokens.pop()


def balanced_parentheses(elts):
    """
    Question 9.3: Check whether a string
    consisting of '{,},[,],(,)' is properly
    balanced
    """
    stack = []
    open_elts = {'{', '[', '('}
    matches = {
        '}': '{',
        ']': '[',
        ')': '(',
    }
    for elt in elts:
        if elt in open_elts:
            stack.append(elt)
        if elt in matches:
            if not stack:
                return False
            if matches[elt] != stack.pop():
                return False

    if len(stack):
        return False
    return True


def shortest_equivalent_path(path):
    """
    Question 9.4: Normalize relative pathnames
    """
    elts = path.split('/')
    realpath = []
    for elt in elts:
        if not len(elt) or elt == '.':
            continue
        elif elt == '..':
            realpath.pop()
        else:
            realpath.append(elt)

    full_path = '/'.join(realpath)
    begin_slash = '/' if path[0] == '/' else ''
    end_slash = '/' if path[-1] == '/' else ''

    return '{}{}{}'.format(begin_slash, full_path, end_slash)


def bst_sorted_order(root):
    """
    Question 9.5: Given a bst node, compute all keys at that node,
    and its descendants in sorted order
    """
    stack = []
    cur_node = root
    result = []

    while stack or cur_node:
        if cur_node:
            stack.append(cur_node)
            cur_node = cur_node.left
        else:
            cur_node = stack.pop()
            result.append(cur_node.val)
            cur_node = cur_node.right
    return result


class PostingListNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None
        self.jump = None
        self.order = -1


def set_jump_order(head):
    """
    Question 9.6: Set the order of every node
    when processed in jump first order
    """
    nodes = [head]
    order = 1

    while nodes:
        cur_node = nodes.pop()
        cur_node.order = order
        order += 1
        if cur_node != cur_node.jump:
            nodes.append(cur_node.jump)


def get_buildings_with_sunset_view(buildings):
    """
    Question 9.7: Design an algorithm that processes
    buildings in east-to-west order and returns the
    set of buildings which view the sunset. Each
    building is specified by its height.
    """
    building_stack = []

    # when we get new building, we pop buildings
    # that are shorter than this building off
    # the stack
    for building in buildings:
        while len(building_stack) and building_stack[-1] <= building:
            building_stack.pop()
        building_stack.append(building)
    return building_stack


def depth_order(root):
    """
    Question 9.9: return depth order representation
    of a binary tree
    """
    traversal = []
    queue = []
    if root:
        queue.insert(0, (root, 0))

    while queue:
        (elt, depth) = queue.pop()
        if len(traversal) == depth:
            traversal.append([elt.val])
        else:
            traversal[depth].append(elt.val)

        if elt.left:
            queue.insert(0, (elt.left, depth + 1))
        if elt.right:
            queue.insert(0, (elt.right, depth + 1))

    return traversal


class CircularQueue(object):
    """
    Question 9.10: Implement a circular queue
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.head = 0
        self.tail = 0
        self.contents = [None] * capacity

    def enqueue(self, value):
        if self.size == self.capacity:
            raise Exception('queue is currently at capacity')

        self.contents[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if not self.size:
            return None

        elt = self.contents[self.head]
        self.size -= 1
        self.head = (self.head + 1) % self.capacity
        return elt


class QueueUsingStacks(object):
    """
    Question 9.11: Implement a queue using stacks
    """

    def __init__(self):
        self.to_enqueue = []
        self.to_dequeue = []

    def enqueue(self, val):
        self.to_enqueue.append(val)

    def dequeue(self):
        if not len(self.to_dequeue):
            # transfer elements in dequeue to enqueue
            while len(self.to_enqueue):
                self.to_dequeue.append(self.to_enqueue.pop())

            if not len(self.to_dequeue):
                raise Exception('No more elements in queue')
        return self.to_dequeue.pop()


class MaxQueue(object):
    """
    Question 9.12: Implement a queue with a max API
    """

    def __init__(self):
        self._entries = []
        self._candidates_for_max = deque()

    def enqueue(self, x):
        self._entries.append(x)
        # eliminate dominated entries in _candidates_for_max
        while len(self._candidates_for_max):
            if self._candidates_for_max[-1] >= x:
                break
            self._candidates_for_max.pop()
        self._candidates_for_max.append(x)

    def deque(self):
        if len(self._candidates_for_max):
            result = self._entries[0]
            if result == self._candidates_for_max[0]:
                self._candidates_for_max.popleft()
            self._entries.pop(0)
            return result
        raise Exception('empty queue')

    def max(self):
        if len(self._candidates_for_max):
            return self._candidates_for_max[0]
        raise Exception('empty queue')
