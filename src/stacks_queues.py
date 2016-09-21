"""
Chapter 9: Stacks and Queues
"""


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
