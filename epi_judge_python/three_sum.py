from test_framework import generic_test

def has_two_sum(A, t):
    i, j = 0, len(A) - 1

    while i <= j:
        if A[i] + A[j] == t:
            return True
        elif A[i] + A[j] < t:
            i += 1
        elif A[j] + A[i] > t:
            j -= 1
        else:
            raise Error("You should not be here")

def has_three_sum(A, t):
    A.sort()

    for a in A:
        if has_two_sum(A, t - a):
            return True

    return False

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("three_sum.py", "three_sum.tsv",
                                       has_three_sum))
