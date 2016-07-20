'''
Chapter 6
'''

def dutch_national_partition(idx, arr):
    '''
    Partition such that all elements less than
    arr[idx] come first, then all elements equal
    to arr[idx], then all elements greater than
    arr[idx]
    '''
    def swap(arr, idx, idy):
        tmp = arr[idx]
        arr[idx] = arr[idy]
        arr[idy] = tmp

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
