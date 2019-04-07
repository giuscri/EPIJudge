from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):
    negative = x < 0

    if x == 0:
        return "0"

    r = ""
    abs_x = abs(x)
    while abs_x:
        r = chr(0x30 + (abs_x % 10)) + r
        abs_x //= 10

    if negative:
        return "-" + r
    else:
        return r


def string_to_int(s):
    n = 0

    negative = s[0] == "-"
    if negative:
        s = s[1:]

    for digit in s:
        assert digit in "0123456789"
        n *= 10
        n += ord(digit) - 0x30

    if negative:
        return -1 * n
    else:
        return n


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
