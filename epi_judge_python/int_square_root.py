from test_framework import generic_test
from math import sqrt, floor

def square_root(k):
    start, stop = 0, k
    candidate = start + (stop - start) // 2
    while start <= stop:
        if candidate ** 2 > k:
            start, stop = start, candidate - 1
        elif candidate ** 2 <= k and (candidate + 1) ** 2 > k:
            return candidate
        elif candidate ** 2 < k:
            start, stop = candidate + 1, stop

        candidate = start + (stop - start) // 2

    raise ValueError("you shouldn't be here")

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
