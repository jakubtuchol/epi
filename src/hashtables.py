from collections import defaultdict

import attr
from attr.validators import instance_of

def find_anagrams(words):
    anagrams = defaultdict(set)

    for word in words:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].add(word)

    return [val for val in anagrams.values() if len(val) > 1]

@attr.s
class Node(object):
    _val = attr.ib(validator=instance_of(str))
    _prev = attr.ib()
    _next = attr.ib()

@attr.s
class IsbnCache(object):
    _capacity = attr.ib(validator=instance_of(int))
    _contents = attr.ib(default=attr.Factory(dict))
    _head_node = None
    _tail_node = None
    _cur_size = 0

    def insert(self, isbn):
        if self._cur_size == self._capacity:
            # need to least recently accessed node
            del self._contents[self._tail_node._val]
            self._tail_node = self._tail_node._prev
            self._tail_node._next = None
        new_node = Node(
            val=isbn,
            prev=None,
            next=self._head_node,
        )
        self._head_node = new_node
        self._contents[isbn] = new_node

    def lookup(self, isbn):
        pass
