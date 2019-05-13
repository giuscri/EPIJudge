from test_framework import generic_test

def _has_three_sum(A, t, k):
    if k == 0:
        return t == 0

    for element in A:
        if _has_three_sum(A, t - element, k - 1):
            return True

    return False

def has_three_sum(A, t):
    return _has_three_sum(A, t, 3)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("three_sum.py", "three_sum.tsv",
                                       has_three_sum))
