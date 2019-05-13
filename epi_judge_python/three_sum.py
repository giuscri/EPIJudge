from test_framework import generic_test

def _has_three_sum(A, t, k, cache):
    if k == 0:
        return t == 0

    if (k, t) in cache:
        return cache[(k, t)]

    for element in A:
        has = _has_three_sum(A, t - element, k - 1, cache)
        cache[(k, t)] = has
        if has:
            return has

    cache[(k, t)] = False
    return cache[(k, t)]

def has_three_sum(A, t):
    return _has_three_sum(A, t, 3, dict())


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("three_sum.py", "three_sum.tsv",
                                       has_three_sum))
