def find_first_occurrence(target, ls):
    """
    Question 12.1
    """
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


def first_larger_than_num(ls, k):
    """
    Question 12.2: Find index of first number
    greater than k in a sorted array
    """
    left = 0
    right = len(ls) - 1
    result = -1

    while left <= right:
        mid = (left + right) / 2
        if ls[mid] > k:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result


def find_entry_equal_to_index(ls):
    """
    Question 12.3: Find first entry with
    index equal to entry
    """
    left = 0
    right = len(ls) - 1
    result = -1

    while left <= right:
        mid = (left + right) / 2
        if ls[mid] == mid:
            result = mid
            right = mid - 1
        elif ls[mid] < mid:
            right = mid - 1
        else:
            left = mid + 1

    return result


def smallest_cyclically_sorted_list(ls):
    """
    Question 12.4: Find index of smallest element
    in cyclically sorted array
    """
    left = 0
    right = len(ls) - 1

    while left < right:
        mid = (left + right) // 2
        if ls[mid] > ls[right]:
            left = mid + 1
        else:
            right = mid

    return left


def square_root(num):
    """
    Question 12.5
    """
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


def search_matrix(matrix, target):
    """
    Question 12.7: A matrix is sorted if its rows
    and columns are nondecreasing. Find if a value
    is located in the matrix.
    """
    row = 0
    col = len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    return False


def find_min_max(ls):
    """
    Question 12.8: Find the min and max of
    a list simultaneously
    """
    min_num = ls[0]
    max_num = ls[0]

    for elt in ls[1:]:
        if min_num > elt:
            min_num = elt
        elif max_num < elt:
            max_num = elt

    return min_num, max_num
