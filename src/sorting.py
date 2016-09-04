def compute_intersection(arr_1, arr_2):
    '''
    Question 14.1: Compute the intersection of two sorted arrays
    '''
    idx_1 = 0
    idx_2 = 0
    intersection = []
    while idx_1 < len(arr_1) and idx_2 < len(arr_2):
        if arr_1[idx_1] == arr_2[idx_2]:
            if not len(intersection) or arr_1[idx_1] != intersection[-1]:
                intersection.append(arr_1[idx_1])
            idx_1 += 1
            idx_2 += 1
        elif arr_1[idx_1] < arr_2[idx_2]:
            idx_1 += 1
        else:
            idx_2 += 1
    return intersection
