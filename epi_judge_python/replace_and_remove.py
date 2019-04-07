import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size, s):
    write_idx = 0
    a_count = 0
    b_count = 0
    for c in s:
        if c == "":
            break

        if c != "b":
            s[write_idx] = c
            write_idx += 1

        if c == "a":
            a_count += 1
        elif c == "b":
            b_count += 1


    size -= b_count
    res_size = 2 * a_count + (size - a_count)
    j = res_size - 1
    i = write_idx - 1

    while i >= 0:
        if s[i] == "a":
            s[j] = s[j - 1] = "d"
            j -= 2
        else:
            s[j] = s[i]
            j -= 1
        i -= 1

    return res_size

@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
