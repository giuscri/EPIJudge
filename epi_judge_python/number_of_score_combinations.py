from test_framework import generic_test

from functools import reduce
from itertools import product

def num_combinations_for_final_score(final_score, individual_play_scores):
    upper_bounds = map(lambda s, final_score=final_score: final_score // s, individual_play_scores)
    iterables = tuple(map(lambda b: tuple(range(b + 1)), upper_bounds))

    n = 0
    for coefficients in product(*iterables):
        if reduce(lambda a, p: a + p[0] * p[1], zip(coefficients, individual_play_scores), 0) == final_score:
            n += 1
    return n

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
