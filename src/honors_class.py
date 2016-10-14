def gcd(x, y):
    """
    Question 22.1: Find the greatest common divisor
    of two numbers without using multiplication,
    division, or the modulus operator
    :return:
    """
    if x == y:
        return x
    elif not (x & 1) and not (y & 1):
        # x even, y even
        return gcd(x >> 1, y >> 1) << 1
    elif not (x & 1) and (y & 1):
        # x even, y odd
        return gcd(x >> 1, y)
    elif (x & 1) and not (y & 1):
        # x odd, y even
        return gcd(x, y >> 1)
    elif x > y:
        return gcd(x - y, y)
    else:
        # x <= y
        return gcd(x, y - x)


def find_first_missing(arr):
    """
    Question 22.2: Find the first positive
    integer not present in the input array
    """
    idx = 0

    while idx < len(arr):
        if 0 < arr[idx] <= len(arr) and arr[idx] != arr[arr[idx] - 1]:
            tmp = arr[arr[idx] - 1]
            arr[arr[idx] - 1] = arr[idx]
            arr[idx] = tmp
        else:
            idx += 1

    # iterate through array to find lowest missing
    for idx, elt in enumerate(arr):
        if elt != idx + 1:
            return idx + 1
    return len(arr) + 1


def largest_minus_one_product(nums):
    """
    Question 22.4: Find the maximum of all
    entries but one
    """

    # iterate through and count number of negatives
    # least negative entry, least positive entry
    # greatest negative idx
    number_of_negatives = 0
    least_negative_idx = -1
    least_positive_idx = -1
    greatest_negative_idx = -1

    for idx, elt in enumerate(nums):
        if elt < 0:
            number_of_negatives += 1

            if least_negative_idx == -1 or \
                    elt < nums[least_negative_idx]:
                least_negative_idx = idx

            if greatest_negative_idx == -1 or \
                    elt > nums[greatest_negative_idx]:
                greatest_negative_idx = idx

        else:
            if least_positive_idx == -1 or \
                    elt < nums[least_positive_idx]:
                least_positive_idx = idx

    if number_of_negatives % 2 == 0:
        if number_of_negatives < len(nums):
            idx_to_skip = least_positive_idx
        else:
            idx_to_skip = least_negative_idx
    else:
        idx_to_skip = greatest_negative_idx

    multiple = 1

    print('idx_to_skip is {}'.format(idx_to_skip))
    for idx, elt in enumerate(nums):
        if idx != idx_to_skip:
            multiple *= elt

    return multiple
