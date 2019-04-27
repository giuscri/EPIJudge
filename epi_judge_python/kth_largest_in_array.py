from test_framework import generic_test
from random import randint

def partition(A, pivot):
    """Partitions A into three: elements smaller than, elements equal to,
    elements greater than a _pivot_.

    Returns the array partitioned in place and the index of the first
    position of the partition containing elements greater than the pivot.

    The pivot is guaranteed to exist."""
    if len(A) <= 1:
        return A, len(A)

    i, j = 0, len(A) - 1
    while i < j:
        while i < len(A) and A[i] <= pivot:
            i += 1
        while j >= 0 and A[j] > pivot:
            j -= 1

        if i >= j:
            break
        elif i not in range(len(A)):
            break
        elif j not in range(len(A)):
            break
        else:
            A[i], A[j] = A[j], A[i]

    r = j + 1

    i, j = 0, r - 1 # if r was correct, j must be exactly the index before it!
    while i < j:
        while i < len(A) and A[i] < pivot:
            i += 1
        while j >= 0 and A[j] == pivot:
            j -= 1

        if i >= j:
            break
        elif i not in range(len(A)):
            break
        elif j not in range(len(A)):
            break
        else:
            A[i], A[j] = A[j], A[i]

    return A, r

def _partition(A, pivot):
    A = [x for x in A if x < pivot] + [x for x in A if x == pivot] + [x for x in A if x > pivot]
    r = len([x for x in A if x < pivot]) + len([x for x in A if x == pivot])
    return A, r

def _compare_partition_functions():
    for _ in range(1000):
        A = [randint(0, 10) for _ in range(10)]
        prepartitioned_A = A[:]
        copyof_A = A[:]
        pivot = A[randint(0, 9)]
        A, expected = _partition(A, pivot)
        copyof_A, actual = partition(copyof_A, pivot)
        assert expected == actual, prepartitioned_A

# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k, A):
    if not A:
        return None

    pivot_idx = randint(0, len(A) - 1)
    pivot = A[pivot_idx]
    A, greater_than_pivot_partition_start = partition(A, pivot)
    assert A[greater_than_pivot_partition_start - 1] == pivot
    h = len(A) - greater_than_pivot_partition_start
    if h == k - 1:
        return A[greater_than_pivot_partition_start - 1]
    elif h > k - 1:
        return find_kth_largest(k, A[greater_than_pivot_partition_start:])
    elif h < k - 1:
        return find_kth_largest(k - h - 1, A[:greater_than_pivot_partition_start - 1])

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
