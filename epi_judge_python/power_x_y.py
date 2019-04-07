from test_framework import generic_test

from math import log2, floor

def power(x, y):
    if y == 0:
        return 1
    if y == 1:
        return x

    abs_y = abs(y)

    r = 1
    n_bits_in_y = floor(log2(abs_y)) + 1
    for shamt in range(n_bits_in_y - 1, -1, -1):
        if (abs_y >> shamt) & 1 == 1:
            r = r * r * x
        else:
            r = r * r

    if y < 0:
        return 1 / r
    else:
        return r


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))
