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
