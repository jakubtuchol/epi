"""
Chapter 16: Recursion
"""


def tower_of_hanoi():
    """
    Question 16.1: Write a program which generates a sequence
    of operations that transfers n rings from one peg to another
    """
    pass


def generate_permutations(ls):
    """
    Question 16.3: Generate all permutations of a list
    """
    if len(ls) <= 1:
        return [ls]

    result = []
    for perm in generate_permutations(ls[1:]):
        for idx in xrange(len(ls)):
            result.append(perm[:idx] + ls[0:1] + perm[idx:])

    return result


def calculate_power_set(ls):
    """
    Question 16.4: Calculate the power
    set of a set
    """
    res = [[]]
    for elt in ls:
        res += [x + [elt] for x in res]
    return res


def generate_subsets(n, k):
    """
    Question 16.5: Calculate all subsets of
    {1,...,n} of size k
    """

    subsets = [[]]
    for idx in xrange(1, n + 1):
        subsets += [x + [idx] for x in subsets if len(x) < k]
    return [x for x in subsets if len(x) == k]
