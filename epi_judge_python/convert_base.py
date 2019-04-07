from test_framework import generic_test


def convert_base(num_as_string, b1, b2):
    digit_to_number = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
    }
    assert len(digit_to_number.keys()) == 16

    number_to_digit = dict(map(lambda pair: (pair[1], pair[0]), digit_to_number.items()))
    assert len(number_to_digit.keys()) == 16

    negative = num_as_string[0] == "-"
    if negative:
        num_as_string = num_as_string[1:]

    n = 0
    for digit  in num_as_string:
        n = n * b1 + digit_to_number[digit]

    if n == 0:
        return "0" if not negative else "-0"

    r = ""
    while n > 0:
        r = number_to_digit[n % b2] + r
        n = n // b2

    if negative:
        r = "-" + r

    return r


if __name__ == '__main__':
    convert_base("0", 11, 7)

    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
