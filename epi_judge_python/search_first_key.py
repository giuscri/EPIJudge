from test_framework import generic_test
from math import inf

def search_first_of_k(A, k):
    m = inf
    start, stop = 0, len(A) - 1
    while start <= stop:
        idx = start + (stop - start) // 2
        if A[idx] == k:
            m = min(m, idx)
            start, stop = start, idx - 1
        elif A[idx] > k:
            start, stop = start, idx - 1
        else:
            start, stop = idx + 1, stop
    return -1 if m is inf else m


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
