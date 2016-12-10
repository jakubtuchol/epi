from sys import maxint

from src.linked_lists import reverse_linked_list


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


def rook_attack(board):
    """
    Question 22.7: Given 2D array of 1s and 0s, where
    0s encode positions of rooks on n x m chessboard,
    update array to contain 0s at all positions which
    can be attacked by rooks
    """

    num_rows = len(board)
    num_cols = len(board[0])
    first_row_attacked = False
    first_col_attacked = False

    # checking if anything on first row is rook
    for j in xrange(num_cols):
        if board[0][j] == 0:
            first_row_attacked = True
            break

    # checking if anything on first column is rook
    for i in xrange(num_rows):
        if board[i][0] == 0:
            first_col_attacked = True
            break

    # set first element of row and col to 0 if
    # row or col can be attacked by rook
    for i in xrange(1, num_rows):
        for j in xrange(1, num_cols):
            if board[i][j] == 0:
                board[i][0] = 0
                board[0][j] = 0

    # update all positions
    for i in xrange(1, num_rows):
        for j in xrange(1, num_cols):
            if board[i][0] == 0 or board[0][j] == 0:
                board[i][j] = 0

    # update first row and first col
    if first_row_attacked:
        for j in xrange(num_cols):
            board[0][j] = 0

    if first_col_attacked:
        for i in xrange(num_rows):
            board[i][0] = 0

    return board


def justify_text(words, line_length):
    """
    Question 22.8: After justification, each
    line must begin with a word, and each
    subsequent word must be separated from prior
    words with at least one blank. If a line
    contains more than one word, it should not
    end in a blank. The sequences of blanks within
    each line should be as close to equal in length
    as possible. with the longer blank sequences
    appearing at the initial part of the line.
    """

    # compute number of words that can
    # fit line by line
    cur_line_remaining = line_length
    result = []
    cur_line = []

    for word in words:
        # if cannot put word in current line,
        # distribute spaces and reset variables
        if len(word) > cur_line_remaining:
            # create and append line
            result.append(create_line(cur_line, line_length))
            cur_line_remaining = line_length
            cur_line = []

        # need space after word
        cur_line_remaining -= len(word) + 1
        cur_line.append(word)

    # final line case
    if len(cur_line) == 1:
        word = cur_line[0]
        num_spaces = line_length - len(word)
        result.append('{}{}'.format(word, ' ' * num_spaces))
    else:
        result.append(create_line(cur_line, line_length))

    return result


def create_line(line, length):
    """
    Create properly spaced line
    """

    full_line = []
    cur_len = sum([len(elt) for elt in line])
    remaining = length - cur_len
    expected_spaces = remaining // (len(line) - 1)
    overflow_spaces = remaining % (len(line) - 1)

    for elt in line[:-1]:
        overflow = ' ' if overflow_spaces else ''
        spaces = '{}{}'.format(' ' * expected_spaces, overflow)
        full_line.append(elt)
        full_line.append(spaces)

        if overflow_spaces:
            overflow_spaces -= 1

    full_line.append(line[-1])

    return ''.join(full_line)


def zip_linked_list(ls):
    """
    Question 22.10: Given a singly linked list, implement a zipping,
    which interleaves the beginning nodes in order and the end nodes
    in reverse
    """

    # make sure list can actually be zipped
    if ls is None or ls.next is None:
        return ls

    # first find end of list
    slow = ls
    fast = ls

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # slow next should now be right before reversible sector
    first_half_head = ls
    second_half_head = slow.next
    slow.next = None

    second_half_head = reverse_linked_list(second_half_head)

    first_half_iter = first_half_head
    second_half_iter = second_half_head

    while second_half_iter:
        temp = second_half_iter.next
        second_half_iter.next = first_half_iter.next
        first_half_iter.next = second_half_iter
        first_half_iter = first_half_iter.next.next
        second_half_iter = temp

    return first_half_head


def compute_circular_sorted_median(ls):
    """
    Question 22.12: Given a sorted circular linked list,
    find the median
    """

    if ls is None:
        return None

    if ls == ls.next:
        return float(ls.val)

    # use slow and fast to find size of cycle
    slow = ls
    fast = ls
    size = 0

    while True:
        slow = slow.next
        fast = fast.next.next
        size += 1

        if slow == fast:
            break

    # get middle element
    even = size % 2 == 0

    if even:
        half = (size // 2) - 1
    else:
        half = size // 2

    while half:
        ls = ls.next
        half -= 1

    if even:
        return float(ls.val + ls.next.val) / 2
    return ls.val


def longest_valid_parentheses(ls):
    """
    Question 22.13: Given a string, find the longest substring
    of matching parentheses
    """

    max_length = 0
    end = -1

    stack = []

    for idx, elt in enumerate(ls):
        if elt == '(':
            stack.append(idx)
        elif not len(stack):
            end = idx
        else:
            stack.pop()
            start = end if not len(stack) else stack[-1]
            max_length = max(max_length, idx - start)

    return max_length
