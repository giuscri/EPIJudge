from test_framework import generic_test


def merge_two_sorted_arrays(A, m, B, n):
    for i in range(len(B)):
        A[m + i] = B[i]
    A.sort()
    return A


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sorted_arrays_merge.py",
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
