from sys import maxint


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


def buy_sell_stock_k_times(stocks, k):
    """
    Question 22.3: Find maximum profit made by
    buying and sell a stock k times.
    """
    k_sum = [-maxint - 1 for _ in xrange(2 * k)]

    for i, elt in enumerate(stocks):
        pre_k_sum = list(k_sum)

        sign = -1
        j = 0

        while j < len(k_sum) and j <= i:
            add = 0 if j == 0 else pre_k_sum[j - 1]
            diff = sign * elt + add
            k_sum[j] = max(diff, pre_k_sum[j])
            j += 1
            sign *= -1

    return k_sum[-1]


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

    for idx, elt in enumerate(nums):
        if idx != idx_to_skip:
            multiple *= elt

    return multiple


def longest_increasing_subarray(ls):
    """
    Question 22.5: Find longest increasing subarray
    in an array and return the beginning and end
    indices
    """
    begin = 0
    end = 0
    cur_begin = 0
    cur_end = 0

    for idx, elt in enumerate(ls):
        if elt > ls[cur_end]:
            cur_end += 1

            if cur_end - cur_begin > end - begin:
                begin = cur_begin
                end = cur_end
        else:
            cur_begin = idx
            cur_end = idx

    return begin, end


def longest_increasing_optimized(ls):
    """
    Optimized version of subarray
    """
    max_length = 1
    begin = 0
    end = 0

    i = 0
    while i < len(ls) - max_length:
        is_skippable = False
        for j in xrange(i + max_length, i, -1):
            if ls[j - 1] >= ls[j]:
                i = j
                is_skippable = True
                break

        if not is_skippable:
            i += max_length

            while i < len(ls) and ls[i - 1] < ls[i]:
                i += 1
                max_length += 1
            begin = i - max_length
            end = i - 1
    return begin, end
