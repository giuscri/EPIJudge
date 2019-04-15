from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):
    if not square_matrix:
        return []

    N = len(square_matrix)
    padding = 0
    r = []
    while N - 2*padding > 1:
        x = y = padding

        for _ in range(N - 2*padding):
            r.append(square_matrix[x][y])
            y += 1
        x += 1
        y -= 1
        for _ in range(N - 2*padding - 1):
            r.append(square_matrix[x][y])
            x += 1
        x -= 1
        y -= 1
        for _ in range(N - 2*padding - 1):
            r.append(square_matrix[x][y])
            y -= 1
        y += 1
        x -= 1
        for _ in range(N - 2*padding - 2):
            r.append(square_matrix[x][y])
            x -= 1

        padding += 1

    if N - 2*padding == 1:
        r.append(square_matrix[padding][padding])

    return r


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
