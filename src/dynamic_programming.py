"""
Chapter 17
"""
import attr
from attr.validators import instance_of


def count_score_combinations(score):
    """
    Question 17.1: Given that you can form score either
    2, 3, or 7 points, calculate the ways you can acheive
    this score
    """
    ways_to_score = [2, 3, 7]
    scores = ([[1] + ([0] * score)]) * len(ways_to_score)

    for play_idx in xrange(len(ways_to_score)):
        for idx in xrange(1, score + 1):
            without_play = scores[play_idx - 1][idx] if play_idx >= 1 else 0
            with_play = scores[play_idx][idx - ways_to_score[play_idx]] if \
                idx >= ways_to_score[play_idx] else 0
            scores[play_idx][idx] = without_play + with_play
    return scores[-1][-1]


def calculate_levenshtein_distance(first_word, second_word):
    """
    Question 17.2
    Given that edits can be insertion, deletion, or substitution
    of a single character, calculate the Levenshtein distance
    between two words.
    """
    """
    idea: given m = len(first_word) and k = len(second_word),
    create an m x k matrix.
    Each cell can be reached either from horizontal left cell,
    vertical up cell, or diagonal cell.
    The value of cell is calculated as minimum of ways that can
    be reached, + 1 if value in first_word[cell] != second_word[cell]
    or + 0 if value in first_word[cell] == second_word[cell]
    """
    matrix = []
    for idx_first in xrange(len(first_word)):
        row = []
        for idx_second in xrange(len(second_word)):
            cands = set()
            if idx_first > 0 and idx_second > 0:
                cands.add(matrix[idx_first - 1][idx_second - 1])
            if idx_first > 0:
                cands.add(matrix[idx_first - 1][idx_second])
            if idx_second > 0:
                cands.add(row[idx_second - 1])
            lowest = min(cands) if len(cands) else 0
            val = 1 + \
                lowest if first_word[idx_first] != second_word[
                    idx_second] else lowest
            row.append(val)

        matrix.append(row)
    return matrix[-1][-1]


def get_num_array_traversals(n, m):
    """
    Question 17.3: Count the number of ways
    to traverse a 2D array
    """
    matrix = []
    for row_num in xrange(n):
        row = [1]
        for col_num in xrange(1, m):
            if row_num == 0:
                row.append(row[-1])
            else:
                row.append(
                    matrix[row_num - 1][col_num] + row[-1]
                )
        matrix.append(row)
    return matrix[-1][-1]


@attr.s
class KObject(object):
    id = attr.ib(validator=instance_of(str))
    price = attr.ib(validator=instance_of(int))
    weight = attr.ib(validator=instance_of(int))


def optimize_knapsack(contents, capacity):
    """
    Question 17.6: Given a set of items with corresponding
    weights and values, as well as the maximum weight that you
    can carry, compute the items that should be chosen to
    maximize the carried value given the weight constraint
    """

    num_items = len(contents)
    table = [[0 for _ in xrange(capacity + 1)] for _ in xrange(num_items + 1)]

    for j in xrange(1, num_items + 1):
        item = contents[j - 1]
        for weight in xrange(1, capacity + 1):
            if item.weight > weight:
                table[j][weight] = table[j - 1][weight]
            else:
                table[j][weight] = max(
                    table[j - 1][weight],
                    table[j - 1][weight - item.weight] + item.price
                )

    result = []
    w = capacity
    for j in xrange(num_items, 0, -1):
        was_added = table[j][w] != table[j - 1][w]

        if was_added:
            item = contents[j - 1]
            result.append(item.id)
            w -= item.weight
    return result


def decompose_into_dictionary_words(ls, dictionary):
    """
    Question 17.7: Given a dictionary of words and a
    string, check whether the string can be decomposed
    into
    """
    cache = set()
    is_word, _ = decompose_helper(ls, dictionary, cache)
    return is_word


def decompose_helper(ls, dictionary, cache):
    """
    Helper for dictionary decomposition function
    """
    if ls in cache:
        return True, cache

    if not len(ls):
        return True, cache

    for idx in xrange(1, len(ls) + 1):
        if ls[:idx] in dictionary:
            decomposed, retcache = decompose_helper(
                ls[idx:], dictionary, cache)
            if decomposed:
                retcache.add(ls)
                return True, retcache

    return False, cache


def number_ways_climb_stairs(num_stairs, max_step):
    """
    Question 17.10: Given a number of stairs and the
    maximum number of stairs taken in a single step,
    find the number of ways to climb a set of stairs
    """
    num_ways = {}
    return compute_number_ways(num_stairs, max_step, num_ways)


def compute_number_ways(num_stairs, max_step, num_ways):
    """
    Helper for number of ways to climb, using cache to
    store intermediary values
    """

    if num_stairs <= 1:
        return 1

    if num_stairs in num_ways:
        return num_ways[num_stairs]

    ways = 0
    for idx in xrange(1, max_step + 1):
        remaining_stairs = num_stairs - idx
        if remaining_stairs in num_ways:
            ways += num_ways[remaining_stairs]
        else:
            ways += compute_number_ways(remaining_stairs, max_step, num_ways)
    num_ways[num_stairs] = ways

    return ways
