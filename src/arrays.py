'''
Chapter 6: Arrays
'''
import random
import sys
from datetime import datetime


def swap(arr, idx, idy):
    tmp = arr[idx]
    arr[idx] = arr[idy]
    arr[idy] = tmp


def dutch_national_partition(idx, arr):
    '''
    Problem 6.1
    Partition such that all elements less than
    arr[idx] come first, then all elements equal
    to arr[idx], then all elements greater than
    arr[idx]
    '''
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
    '''
    improved, single-pass version of
    dutch national flag algorithm
    '''
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
    '''
    Question 6.2: Implement arbitrary precision
    integer to add one
    '''
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


def buy_sell_once(stocks):
    '''
    Problem 6.7
    find the maximum profit achieved by buying
    a stock and selling it
    '''
    max_profit = 0
    lowest = sys.maxsize
    for price in stocks:
        if price < lowest:
            lowest = price
        if price - lowest > max_profit:
            max_profit = price - lowest
    return max_profit


def random_sample(inputs, size):
    '''
    Problem 6.12
    given an array of input values, return
    a random subset of inputs of size `size`
    '''
    next_pos = len(inputs) - 1
    # seed rand generator
    random.seed(datetime.now())
    for _ in xrange(size):
        idx = random.randrange(next_pos)
        swap(inputs, idx, next_pos)
        next_pos -= 1

    return inputs[next_pos:]


def check_sudoku(sudoku):
    '''
    Question 6.17: Check if 9x9 sudoku puzzle is valid
    '''
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
    '''
    Get index of associated square
    '''
    return (row // 3) * 3 + col // 3


def spiralize(arr):
    '''
    Problem 6.18
    print out spiral traversal of 2D array
    '''
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
