def merge_sort(A):
    if A is None or len(A) <= 1:
        return A

    A[:len(A) // 2] = merge_sort(A[:len(A) // 2])
    A[len(A) // 2:] = merge_sort(A[len(A) // 2:])
    A[:] = merge(A[:len(A) // 2], A[len(A) // 2:])

    return A

def merge(A, B):
    """Returns C as the array merged from the two sorted array A and B."""
    if A is None:
        A = []
    if B is None:
        B = []

    assert sorted(A) == A, "A should be sorted"
    assert sorted(B) == B, "B should be sorted"

    i, j, C = 0, 0, []

    while i in range(len(A)) and j in range(len(B)):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    if i not in range(len(A)): # A has been traversed completely
        while j in range(len(B)):
            C.append(B[j])
            j += 1
    elif j not in range(len(B)): # B has been traversed completely
        while i in range(len(A)):
            C.append(A[i])
            i += 1
    else:
        raise Error("you shouldn't be here")

    return C

if __name__ == "__main__":
    # test merge() on empty arrays
    assert merge([], []) == []

    # test merge() when one array is None
    assert merge(None, []) == []
    assert merge([], None) == []

    # test merge() on common case
    assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

    # test merge() when one array is unsorted
    try:
        merge([5, 3, 1], [])
        assert False
    except AssertionError:
        assert True

    # test merge_sort() on empty array
    assert merge_sort([]) == []

    # test merge_sort() when array is None
    assert merge_sort(None) is None

    # test merge_sort() on common case
    assert merge_sort([4, 3, 6, 1]) == [1, 3, 4, 6]
