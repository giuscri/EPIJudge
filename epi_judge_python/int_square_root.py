from test_framework import generic_test
from math import sqrt, floor

def square_root(k):
    if k == 0:
        return 0

    previous = 0
    current = 1
    while current ** 2 <= k:
        previous = current
        current += 1

    return previous


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
