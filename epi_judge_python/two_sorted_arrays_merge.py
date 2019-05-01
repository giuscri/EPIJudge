from test_framework import generic_test


def merge_two_sorted_arrays(A, m, B, n):
    """Merges A and B, where A has enough entries to store them both.

    The idea is the keep three indices: i, j and k. i points to the next item
    of A to process, j to the next item of B to process and k points to the
    next entry of A that we can overwrite.

    The procedure runs in O(1) memory and it has a time complexity of O(|A|).
    """

    i, j, k = m - 1, n - 1, len(A) - 1
    while k >= 0:
        if i < 0:
            assert j >= 0
            A[k] = B[j]
            k -= 1
            j -= 1
        elif j < 0:
            assert i >=0
            A[k] = A[i]
            k -= 1
            i -= 1
        elif A[i] > B[j]:
            A[k] = A[i]
            i -= 1
            k -= 1
        else:
            A[k] = B[j]
            j -= 1
            k -= 1

    return A

def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sorted_arrays_merge.py",
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
