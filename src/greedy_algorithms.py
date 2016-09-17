def three_sum(target, ls):
    """
    Question 18.5: Check if three numbers within input
    array sum to target
    """
    ls = sorted(ls)

    for idx, elt in enumerate(ls):
        if two_sum(target - elt, ls[:idx] + ls[idx + 1:]):
            return True
    return False


def two_sum(target, ls):
    """
    Check if two numbers within input array sum to target
    """
    complements = set()
    for num in ls:
        if num in complements:
            return True
        complements.add(target - num)

    return False


def find_majority_element(array):
    """
    Question 18.6
    """
    majority_elt = None
    count = 0
    for elt in array:
        if elt != majority_elt:
            if count == 0:
                majority_elt = elt
                count = 1
            else:
                count -= 1
        else:
            count += 1
    return majority_elt
