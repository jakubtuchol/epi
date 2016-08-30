def find_first_occurrence(target, ls):
    '''
    Question 12.1
    '''
    left = 0
    right = len(ls) - 1
    result = -1

    while left <= right:
        mid = left + ((right - left) // 2)
        if ls[mid] > target:
            right = mid - 1
        elif ls[mid] == target:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

def square_root(num):
    '''
    Question 12.5
    '''
    last_root = 1
    root = 2
    square = 4
    while square < num:
        last_root = root
        root = square
        square *= square

    if square == num:
        return root

    # binary search for proper root
    low, high = last_root, root

    while low <= high:
        mid = low + ((high - low) // 2)
        square = mid ** 2
        if square > num:
            high = mid - 1
        elif square == num:
            return mid
        else:
            low = mid + 1
        
    return low - 1
