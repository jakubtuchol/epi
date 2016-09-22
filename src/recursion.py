"""
Chapter 16: Recursion
"""


def tower_of_hanoi():
    """
    Question 16.1: Write a program which generates a sequence
    of operations that transfers n rings from one peg to another
    """
    pass


def calculate_power_set(ls):
    """
    Question 16.4: Calculate the power
    set of a set
    """
    res = [[]]
    for elt in ls:
        res += [x + [elt] for x in res]
    return res
