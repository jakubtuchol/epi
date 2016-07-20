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
    for idy, elt in enumerate(arr):
        # group all elements less than pivot at
        # the bottom
        if elt < pivot:
            swap(arr, smaller, idy)
            smaller += 1

    larger = len(arr) - 1
    for idy, elt in enumerate(arr):
        # group all elements greater than pivot
        # at the bottom
        if elt > pivot:
            swap(arr, larger, idy)
            larger -= 1
