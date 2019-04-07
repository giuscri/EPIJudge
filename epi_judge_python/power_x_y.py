from test_framework import generic_test


def power(x, y):
    if y == 0:
        return 1
    if y == 1:
        return x
    elif y == -1:
        return 1 / x

    abs_y = abs(y)

    p = power(x, abs_y >> 1)
    r = None
    if abs_y & 1 == 1:
        r = p * p * x
    else:
        r = p * p

    if y < 0:
        return 1 / r
    else:
        return r


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))
