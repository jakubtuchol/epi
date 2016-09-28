"""
Chapter 6: Arrays
"""
import random
import sys
from datetime import datetime

import attr
from attr.validators import instance_of


def swap(arr, idx, idy):
    tmp = arr[idx]
    arr[idx] = arr[idy]
    arr[idy] = tmp


def dutch_national_partition(idx, arr):
    """
    Problem 6.1
    Partition such that all elements less than
    arr[idx] come first, then all elements equal
    to arr[idx], then all elements greater than
    arr[idx]
    """
    pivot = arr[idx]

    smaller = 0
    idy = smaller
    while idy < len(arr):
        # group all elements less than pivot at
        # the bottom
        if arr[idy] < pivot:
            swap(arr, smaller, idy)
            smaller += 1
        idy += 1

    larger = len(arr) - 1
    idy = larger
    while idy >= 0:
        # group all elements greater than pivot
        # at the bottom
        if arr[idy] > pivot:
            swap(arr, larger, idy)
            larger -= 1
        idy -= 1


def dutch_partition_better(idx, arr):
    """
    improved, single-pass version of
    dutch national flag algorithm
    """
    pivot = arr[idx]

    small = 0
    equal = 0
    large = len(arr) - 1

    while equal < large:
        if arr[equal] < pivot:
            swap(arr, small, equal)
            small += 1
            equal += 1
        elif arr[equal] == pivot:
            equal += 1
        else:
            swap(arr, equal, large)
            large -= 1


def add_one(num):
    """
    Question 6.2: Implement arbitrary precision
    integer to add one
    """
    num[-1] += 1
    begin = len(num) - 1

    while num[begin] == 10 and begin > 0:
        num[begin] = 0
        num[begin - 1] += 1
        begin -= 1

    if num[0] == 10:
        num[0] = 0
        return [1] + num
    return num


def multiply(first_num, second_num):
    """
    Question 6.3: Multiply two arbitrary
    precision numbers
    """
    first_num.reverse()
    second_num.reverse()

    result_len = len(first_num) + len(second_num)
    result = [0 for _ in xrange(result_len)]
    negative = False

    for idx_first, elt_first in enumerate(first_num):
        for idx_second, elt_second in enumerate(second_num):
            mult = elt_first * elt_second
            if mult < 0:
                negative = True
                mult *= -1
            result[idx_first + idx_second] += mult

    carry = 0
    for idx, elt in enumerate(result):
        elt += carry
        carry = elt // 10
        result[idx] = elt % 10

    while carry:
        rem = carry % 10
        carry //= 10
        result.append(rem)

    if negative:
        result[-1] *= -1

    result.reverse()

    return result


def can_reach_end(steps):
    """
    Question 6.4: Given an array of n integers, where
    A[i] denotes the maximum number of steps that can
    advance from i, return whether it is possible to
    advance to last index from beginning of array
    """
    last_idx = len(steps)
    furthest_reach_so_far = 0

    idx = 0
    while idx <= furthest_reach_so_far < last_idx:
        furthest_reach_so_far = max(
            furthest_reach_so_far,
            steps[idx] + idx
        )
        idx += 1

    return furthest_reach_so_far >= last_idx


def delete_key(ls, key):
    """
    Question 6.5: Given an array and an input key,
    remove the key from the array
    """
    write_idx = 0
    for idx, elt in enumerate(ls):
        if elt != key:
            ls[write_idx] = elt
            write_idx += 1

    while write_idx < len(ls):
        ls[write_idx] = None
        write_idx += 1

    return ls


def delete_duplicates(ls):
    """
    Question 6.6: Delete duplicates from sorted array,
    return number of elements remainint
    """

    if not len(ls):
        return 0

    write_idx = 0
    for idx, elt in enumerate(ls):
        if idx > write_idx and elt != ls[write_idx]:
            write_idx += 1
            ls[write_idx] = elt

    return write_idx + 1


def buy_sell_once(stocks):
    """
    Problem 6.7
    find the maximum profit achieved by buying
    a stock and selling it
    """
    max_profit = 0
    lowest = sys.maxsize
    for price in stocks:
        if price < lowest:
            lowest = price
        if price - lowest > max_profit:
            max_profit = price - lowest
    return max_profit


def buy_sell_stock_twice(stocks):
    """
    Question 6.8: Find the maximum profit that
    can be made from buying and selling a
    stock at most twice
    """
    max_profit = 0
    for idx in xrange(len(stocks)):
        profit = buy_sell_once(stocks[:idx]) + \
            buy_sell_once(stocks[idx:])
        max_profit = max(profit, max_profit)
    return max_profit


def generate_primes(n):
    """
    Question 6.9: Enumerate all primes to n
    """
    primes = []
    for idx in xrange(2, n):
        divided = False
        for prime in primes:
            if idx % prime == 0:
                divided = True
                break
        if not divided:
            primes.append(idx)
    return primes


def apply_permutation(array, permutation):
    """
    Question 6.10: Given an array and a permutation,
    apply the permutation to the array
    """
    perm_size = len(permutation)
    for idx in xrange(perm_size):
        next = idx
        while permutation[next] >= 0:
            array[idx], array[permutation[next]] = \
                array[permutation[next]], array[idx]
            temp = permutation[next]
            permutation[next] -= perm_size
            next = temp

    return array


def next_permutation(ls):
    """
    Question 6.11: Given an array, compute the
    next permutation in dictionary order
    """
    # find right-most adjacent indices with elements
    # in order
    inorder_idx = None
    cur_cand = sys.maxint
    cand_idx = None
    for idx, elt in enumerate(ls[:-1]):
        if elt < ls[idx + 1]:
            inorder_idx = idx
        if inorder_idx is not None:
            if ls[inorder_idx] < elt < cur_cand:
                cur_cand = elt
                cand_idx = idx

    if inorder_idx is not None:
        if ls[inorder_idx] < ls[-1] < cur_cand:
            cand_idx = len(ls) - 1

    if inorder_idx is None:
        return []

    # switch candidate element with first element that is in order
    ls[inorder_idx], ls[cand_idx] = ls[cand_idx], ls[inorder_idx]
    return ls[:inorder_idx + 1] + ls[inorder_idx + 1:][::-1]


def random_sample(inputs, size):
    """
    Problem 6.12
    given an array of input values, return
    a random subset of inputs of size `size`
    """
    next_pos = len(inputs) - 1
    # seed rand generator
    random.seed(datetime.now())
    for _ in xrange(size):
        idx = random.randrange(next_pos)
        swap(inputs, idx, next_pos)
        next_pos -= 1

    return inputs[next_pos:]


def online_sample(population, size):
    """
    Problem 6.13: Given a stream of packets and
    an desired target size k, maintain a uniform
    random subset of size k
    """
    results = []
    for idx, elt in enumerate(population):
        if idx < size:
            results.append(idx)
        else:
            probability = float(idx + 1) / float(size)
            if random.uniform(0, 1) < probability:
                # add number to set
                results[random.randrange(0, size)] = elt
    return results


@attr.s
class NumProbability(object):
    num = attr.ib(validator=instance_of(int))
    prob = attr.ib(validator=instance_of(float))


def nonuniform_random(nums):
    """
    Question 6.16: Generate nonuniform random numbers,
    given array of numbers and probabilities
    """
    endpts = [(0, None)]

    for num in nums:
        new_end = endpts[-1][0] + num.prob
        endpts.append((new_end, num.num))

    prob = random.uniform(0, 1)

    for idx, elt in enumerate(endpts[:-1]):
        if elt[0] < prob < endpts[idx + 1][0]:
            return endpts[idx + 1][1]
    return None


def check_sudoku(sudoku):
    """
    Question 6.17: Check if 9x9 sudoku puzzle is valid
    """
    # initialize sets
    rows = []
    cols = []
    squares = []
    for idx in xrange(9):
        rows.append(set())
        cols.append(set())
        squares.append(set())

    for row, row_elt in enumerate(sudoku):
        for col, elt in enumerate(row_elt):
            if elt in rows[row]:
                return False
            rows[row].add(elt)

            if elt in cols[col]:
                return False
            cols[col].add(elt)

            square = get_square_idx(row, col)
            if elt in squares[square]:
                return False
            squares[square].add(elt)
    return True


def get_square_idx(row, col):
    """
    Get index of associated square
    """
    return (row // 3) * 3 + col // 3


def spiralize(arr):
    """
    Problem 6.18
    print out spiral traversal of 2D array
    """
    output = []
    min_x = 0
    min_y = 0
    max_x = len(arr[0]) - 1
    max_y = len(arr) - 1

    while min_x <= max_x and min_y <= max_y:
        # iterate forward across top
        for x in xrange(min_x, max_x + 1):
            output.append(arr[min_y][x])
        min_y += 1

        # iterate down across right
        for y in xrange(min_y, max_y + 1):
            output.append(arr[y][max_x])
        max_x -= 1

        # iterate backward across bottom
        for x in xrange(max_x, min_x - 1, -1):
            output.append(arr[max_y][x])
        max_y -= 1

        # iterate upward across left
        for y in xrange(max_y, min_y - 1, -1):
            output.append(arr[y][min_x])
        min_x += 1
    return output
