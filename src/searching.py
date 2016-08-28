def find_first_occurrence(target, ls):
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
