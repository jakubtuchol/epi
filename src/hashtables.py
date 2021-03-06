from collections import defaultdict
from sys import maxint


def find_anagrams(words):
    """
    Question 13.1: Take in set of words and returns
    list of these words grouped into anagrams
    """
    anagrams = defaultdict(set)

    for word in words:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].add(word)

    return [val for val in anagrams.values() if len(val) > 1]


def palindromic_permutation(string):
    """
    Question 13.2: Test whether the letters
    forming a string to form a palindrome
    """
    seen = set()
    for char in string:
        if char in seen:
            seen.remove(char)
        else:
            seen.add(char)
    return len(seen) <= 1


class IsbnNode(object):

    def __init__(self, val, price):
        self.val = val
        self.price = price
        self.prev = None
        self.next = None


class IsbnCache(object):
    """
    Question 13.4
    """

    def __init__(self, max_size):
        self.capacity = max_size
        self.cur_size = 0
        self.contents = dict()
        self.head = None
        self.tail = None

    def insert(self, val, price):
        node = IsbnNode(val, price)
        if self.cur_size == 0:
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
        self.head = node

        # need to vacate node
        if self.cur_size == self.capacity:
            cur_tail = self.tail
            self.tail = cur_tail.prev
            cur_tail.next = None
            self.contents.pop(cur_tail.val)
            self.cur_size -= 1
        self.contents[val] = node
        self.cur_size += 1

    def lookup(self, val):
        if val in self.contents:
            res_node = self.contents[val]
            prev_node = res_node.prev
            next_node = res_node.next

            if res_node != self.head:
                if self.cur_size > 1 and self.tail == res_node:
                    self.tail = prev_node
                if prev_node:
                    prev_node.next = next_node
                if next_node:
                    next_node.prev = prev_node
                res_node.prev = None
                res_node.next = self.head
                self.head = res_node
            return res_node.price
        return None


def find_nearest_repetition(words):
    """
    Question 13.7: Given array of words, find
    distance of closest pair identical words
    """
    past_idx = {}
    lowest_distance = maxint

    for idx, word in enumerate(words):
        if word in past_idx:
            if idx - past_idx[word] < lowest_distance:
                lowest_distance = idx - past_idx[word]
        past_idx[word] = idx

    if lowest_distance == maxint:
        return None
    return lowest_distance


def find_longest_distinct_subarray(ls):
    """
    Question 13.10: Find longest subarray
    with distinct entries
    """
    # maximum trackers
    max_begin = 0
    max_len = 0

    # current trackers
    cur_begin = 0
    cur_len = 0

    seen = {}

    for idx, elt in enumerate(ls):
        if elt not in seen or seen[elt] < cur_begin:
            cur_len += 1
        else:
            if cur_len >= max_len:
                max_len = cur_len
                max_begin = cur_begin
            cur_begin = seen[elt] + 1
            cur_len = idx - seen[elt]
        seen[elt] = idx

    if cur_len > max_len:
        max_len = cur_len
        max_begin = cur_begin

    return ls[max_begin:max_begin + max_len]
