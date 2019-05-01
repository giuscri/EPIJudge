from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    intersection = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if intersection == [] or A[i] != intersection[-1]:
                # don't want to insert duplicates in `intersection`
                intersection.append(A[i])

            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        elif A[i] > B[j]:
            j += 1
    return intersection


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
