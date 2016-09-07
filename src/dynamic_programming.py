'''
Chapter 17
'''
def count_score_combinations(score):
    '''
    Question 17.1: Given that you can form score either
    2, 3, or 7 points, calculate the ways you can acheive
    this score
    '''
    ways_to_score = [2,3,7]
    scores = ([[1] + ([0] * score)]) * len(ways_to_score)

    for play_idx in xrange(len(ways_to_score)):
        for idx in xrange(1, score + 1):
            without_play = scores[play_idx-1][idx] if play_idx >= 1 else 0
            with_play = scores[play_idx][idx-ways_to_score[play_idx]] if \
                    idx >= ways_to_score[play_idx] else 0
            scores[play_idx][idx] = without_play + with_play
    return scores[-1][-1]

def calculate_levenshtein_distance(first_word, second_word):
    '''
    Question 17.2
    Given that edits can be insertion, deletion, or substitution
    of a single character, calculate the Levenshtein distance
    between two words.
    '''
    '''
    idea: given m = len(first_word) and k = len(second_word),
    create an m x k matrix.
    Each cell can be reached either from horizontal left cell,
    vertical up cell, or diagonal cell.
    The value of cell is calculated as minimum of ways that can
    be reached, + 1 if value in first_word[cell] != second_word[cell]
    or + 0 if value in first_word[cell] == second_word[cell]
    '''
    matrix = []
    for idx_first in xrange(len(first_word)):
        row = []
        for idx_second in xrange(len(second_word)):
            cands = set()
            if idx_first > 0 and idx_second > 0:
                cands.add(matrix[idx_first-1][idx_second-1])
            if idx_first > 0:
                cands.add(matrix[idx_first-1][idx_second])
            if idx_second > 0:
                cands.add(row[idx_second-1])
            lowest = min(cands) if len(cands) else 0
            val = 1 + lowest if first_word[idx_first] != second_word[idx_second] else lowest
            row.append(val)

        matrix.append(row)
    return matrix[-1][-1]
