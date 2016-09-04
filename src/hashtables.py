from collections import defaultdict

import attr
from attr.validators import instance_of

def find_anagrams(words):
    anagrams = defaultdict(set)

    for word in words:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].add(word)

    return [val for val in anagrams.values() if len(val) > 1]

@attr.s(repr_ns='node')
class Node(object):
    _val = attr.ib(validator=instance_of(str))
    _price = attr.ib(validator=instance_of(float))
    _prev = attr.ib(default=None)
    _next = attr.ib(default=None)

@attr.s(repr_ns='cache')
class IsbnCache(object):
    _capacity = attr.ib(validator=instance_of(int))
    _contents = attr.ib(default=attr.Factory(dict))
    _head_node = attr.ib(default=None)
    _tail_node = attr.ib(default=None)
    _cur_size = attr.ib(default=0)

    def insert(self, isbn, price):
        if self._cur_size == self._capacity:
            # need to least recently accessed node
            last_val = self._tail_node._val
            self._contents.pop(last_val)
            # self._contents[self._tail_node._val]
            self._tail_node = self._tail_node._prev
            self._tail_node._next = None
        else:
            self._cur_size += 1
        new_node = Node(
            val=isbn,
            price=price,
            next=self._head_node,
            prev=None,
        )

        # check if have single node
        if self._cur_size == 1:
            self._tail_node = new_node
        self._head_node = new_node
        self._contents[isbn] = new_node

    def lookup(self, code):
        if code in self._contents:
            node = self._contents[code]
            # move node to head node
            prev = node._prev
            next = node._next
            if prev:
                prev._next = next
            if next:
                next._prev = prev
            if self._cur_size > 1:
            # if is last node, then make prev last
                if self._tail_node == node:
                    self._tail_node = node._prev
                node._next = self._head_node
                self._head_node._prev = node
            node._prev = None
            self._head_node = node
            assert len(self._contents.keys()) == self._cur_size
            return node._price
        return None

    def get_tail(self):
        if self._cur_size > 0:
            assert self._tail_node != None
        return self._tail_node

    def get_head(self):
        return self._head_node

    def get_contents(self):
        return self._contents
