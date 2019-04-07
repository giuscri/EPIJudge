import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size, s):
    many_as, many_bs = 0, 0
    for i in range(size):
        if s[i] == "b":
            s[i] = ""
            size -= 1
            many_bs += 1
        elif s[i] == "a":
            many_as += 1

    res_size = 2 * many_as + (size - many_as)
    j = len(s) - 1
    i = size + many_bs - 1
    while i >= 0:
        if s[i] in ["c", "d"]:
            s[j] = s[i]
            j -= 1
            i -= 1
        elif s[i] == "a":
            s[j] = "d"
            s[j - 1] = "d"
            j -= 2
            i -= 1
        elif s[i] == "":
            i -= 1

    j += 1
    i = 0
    while i < res_size:
        s[i] = s[j]
        i += 1
        j += 1

    return res_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    replace_and_remove(1, ["a", ""])
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
