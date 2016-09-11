from math import ceil


def find_parity(x):
    '''
    Problem 5.1: Computing the parity of a word
    '''
    parity = 0

    while x:
        parity += x & 1
        x >>= 1

    return parity % 2


def reverse_bits(x):
    '''
    Question 5.3: Reverse the bits in a number
    '''
    MAX_LEN = 64
    bin_str = '{:08b}'.format(x)
    remaining = MAX_LEN - len(bin_str)
    full_str = bin_str[::-1] + ('0' * remaining)
    return int(full_str, 2)


def reverse_digits(num):
    '''
    Problem 5.8: Reverse digits of a number
    '''
    negative = False
    if num < 0:
        negative = True
        num *= -1

    reversal = list(str(num))
    upper = len(reversal) - 1
    max_loc = int(ceil(len(reversal) / 2))
    for idx in xrange(max_loc):
        tmp = reversal[idx]
        reversal[idx] = reversal[upper-idx]
        reversal[upper-idx] = tmp

    rev_num = int(''.join(reversal))
    if negative:
        return -1 * rev_num
    return rev_num


class Rectangle(object):
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width


def check_rectangle_intersection(rect1, rect2):
    '''
    Problem 5.11: Check intersection of two rectangles
    '''
    left = rect1 if rect1.x <= rect2.x else rect2
    right = rect1 if rect1.x > rect2.x else rect2
    # check if left 
    return False
