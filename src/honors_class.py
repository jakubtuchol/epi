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
