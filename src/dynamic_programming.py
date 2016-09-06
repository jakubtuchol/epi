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
    scores = [1] + ([0] * score)

    for idx in xrange(1, score + 1):
        print('handling score {}'.format(idx))
        min_seven = idx - 7
        min_three = idx - 3
        min_two = idx - 2
        score_seven = 0 if min_seven < 0 else scores[min_seven]
        print('min_seven is {}, score_seven is {}'.format(min_seven, score_seven))
        score_three = 0 if min_three < 0 else scores[min_three]
        print('min_three is {}, score_three is {}'.format(min_three, score_three))
        score_two = 0 if min_two < 0 else scores[min_two]
        print('min_two is {}, score_two is {}'.format(min_two, score_two))
        scores[idx] = score_seven + score_three + score_two
    print('scores are {}'.format(scores))
    return scores[-1]
