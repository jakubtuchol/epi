def find_first_occurrence(target, ls):
    left = 0
    right = len(ls) - 1
    candidates = set()

    while left <= right:
        mid = (left + right) // 2
        if ls[mid] == target:
            candidates.add(mid)
            right = mid
        elif ls[mid] < target:
            if mid + 1 in candidates:
                return mid + 1
            left = mid
        else:
            right = mid
        if mid == 0 or mid == len(ls):
            break
    if len(candidates):
        return min(candidates)
    return -1
