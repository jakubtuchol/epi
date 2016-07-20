import sys

'''
Chapter 6
'''
def swap(arr, idx, idy):
    tmp = arr[idx]
    arr[idx] = arr[idy]
    arr[idy] = tmp

def dutch_national_partition(idx, arr):
    '''
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
            small += 1; equal += 1
        elif arr[equal] == pivot:
            equal += 1
        else:
            swap(arr, equal, large)
            large -= 1

def buy_sell_once(stocks):
    '''
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
