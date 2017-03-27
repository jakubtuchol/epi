"""
Chapter 14: Sorting
"""
from collections import defaultdict


def compute_intersection(arr_1, arr_2):
    """
    Question 14.1: Compute the intersection of two sorted arrays
    """
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


def inplace_mergesort(long_arr, long_bound, short_arr, short_bound):
    """
    Question 14.2: Implement mergesort in-place
    """
    write_idx = long_bound + short_bound - 1
    long_idx = long_bound - 1
    short_idx = short_bound - 1

    while long_idx >= 0 and short_idx >= 0:
        if long_arr[long_idx] > short_arr[short_idx]:
            long_arr[write_idx] = long_arr[long_idx]
            long_idx -= 1
        else:
            long_arr[write_idx] = short_arr[short_idx]
            short_idx -= 1
        write_idx -= 1

    while short_idx >= 0:
        long_arr[write_idx] = short_arr[short_idx]
        write_idx -= 1
        short_idx -= 1


def count_occurrences(sentence):
    """
    Question 14.3: Count frequencies of
    characters in a string
    """
    seen = defaultdict(int)
    for char in sentence.lower():
        seen[char] += 1

    output = []
    for key, val in seen.iteritems():
        output.append((key, val))
    return output


def remove_repeated_first_names(names):
    """
    Question 14.4: Remove duplicate first names
    from input array
    """

    seen = set()
    output = []
    for name in names:
        if name[0] not in seen:
            output.append(name)
            seen.add(name[0])
    return output


def find_max_simultaneous_events(events):
    """
    Question 14.5: Given a list of intervals representing
    start and end times of events, find the maximum number
    of simultaneous events that we can schedule
    """
    transitions = []
    simultaneous = 0
    max_simultaneous = 0

    for event in events:
        transitions.append((event[0], True))
        transitions.append((event[1], False))

    sorted_transitions = sorted(transitions, key=lambda x: x[0])

    for transition in sorted_transitions:
        if transition[1]:
            simultaneous += 1
        else:
            simultaneous -= 1
        max_simultaneous = max(simultaneous, max_simultaneous)
    return max_simultaneous


def add_interval(intervals, interval_to_add):
    """
    Question 14.6: Takes an array of disjoint intervals
    with integer endpoints, sorted by increasing order of
    left endpoint, and an interval to add, and returns the
    union of the intervals in the array and the added interval
    """
    processed_intervals = []
    begin_add, end_add = interval_to_add

    merge_begin = None
    merge_end = None
    merging = False

    for interval in intervals:
        begin, end = interval

        # if prior to interval_to_add, then add to processed
        if end < begin_add:
            processed_intervals.append(interval)
        # if after interval_to_add, then add to processed
        elif begin > end_add:
            if merging:
                merging = False
                processed_intervals.append((merge_begin, merge_end))
            processed_intervals.append(interval)
        # else end >= begin_add and begin <= end_add
        else:
            if merge_begin is None:
                merge_begin = begin_add if begin_add < begin else begin
            merge_end = end_add if end_add > end else end
            merging = True

    return processed_intervals
