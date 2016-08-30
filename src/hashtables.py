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
class IsbnCache(object):
    _capacity = attr.ib(validator=instance_of(int))
    _contents = attr.ib(default=attr.Factory(dict)) 

    def insert(self, isbn):
        pass

    def lookup(self, isbn):
        pass
