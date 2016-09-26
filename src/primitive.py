"""
Chapter 5: Primitives
"""
from math import ceil


def find_parity(x):
    """
    Problem 5.1: Computing the parity of a word
    """
    parity = 0

    while x:
        parity += x & 1
        x >>= 1

    return parity % 2


def swap_bits(x, j, k):
    """
    Question 5.2: Swap bits in a number
    """
    if (x >> j) & 1 != (x >> k) & 1:
        mask = (1 << j) | (1 << k)
        x ^= mask
    return x


def reverse_bits(x):
    """
    Question 5.3: Reverse the bits in a number
    """
    MAX_LEN = 64
    bin_str = '{:08b}'.format(x)
    remaining = MAX_LEN - len(bin_str)
    full_str = bin_str[::-1] + ('0' * remaining)
    return int(full_str, 2)


def closest_int_same_bit_count(x):
    """
    Question 5.4: Find an int that is closest to
    the input integer and has the same number of
    bits set
    """
    # find two right-most bits that differ and swap them
    num_bits = x.bit_length()

    for bit in xrange(num_bits):
        if (x >> bit) & 1 != (x >> (bit + 1)) & 1:
            x ^= (1 << bit) | (1 << (bit + 1))
    return x


def multiply(x, y):
    """
    Question 5.5: Compute X x Y without using
    arithmetic operators
    """
    cur_sum = 0
    while x:
        if x & 1 == 1:
            cur_sum = add(cur_sum, y)
        x >>= 1
        y <<= 1
    return cur_sum


def add(x, y):
    """
    Helper function to implement
    adding for binary nums
    """
    cur_sum = 0
    carry_in = 0
    temp_x = x
    temp_y = y
    k = 1

    while temp_x or temp_y:
        xk = x & k
        yk = y & k
        carry_out = (xk & yk) | (xk & carry_in) | (yk & carry_in)
        cur_sum |= (xk ^ yk ^ carry_in)
        carry_in = carry_out << 1
        k <<= 1
        temp_x >>= 1
        temp_y >>= 1
    return cur_sum | carry_in


def reverse_digits(num):
    """
    Problem 5.8: Reverse digits of a number
    """
    negative = False
    if num < 0:
        negative = True
        num *= -1

    reversal = list(str(num))
    upper = len(reversal) - 1
    max_loc = int(ceil(len(reversal) / 2))
    for idx in xrange(max_loc):
        tmp = reversal[idx]
        reversal[idx] = reversal[upper - idx]
        reversal[upper - idx] = tmp

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


def palindrome_number(x):
    """
    Problem 5.9: Check if decimal integer
    is palindrome
    """
    if x < 0:
        return False
    elif x == 0:
        return True

    x_rep = str(x)

    if len(x_rep) == 1:
        return True

    left = 0
    right = len(x_rep) - 1
    while left < right:
        if x_rep[left] != x_rep[right]:
            return False
        left += 1
        right -= 1
    return True


def check_rectangle_intersection(rect1, rect2):
    """
    Problem 5.11: Check intersection of two rectangles
    """
    if get_intersection(rect1, rect2):
        x = max(rect1.x, rect2.x)
        y = max(rect1.y, rect2.y)
        height = min(rect1.y + rect1.height, rect2.y + rect2.height) - y
        width = min(rect1.x + rect1.width, rect2.x + rect2.width) - x
        return Rectangle(x, y, height, width)

    return None


def get_intersection(one, two):
    # intersection of widths
    width_intersect = one.x < two.x + two.width \
        and one.x + one.width > two.x
    # intersection of heights
    height_intersect = one.y < two.y + two.height \
        and one.y + one.height > two.y
    return width_intersect and height_intersect
