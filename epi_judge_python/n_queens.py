from test_framework import generic_test

def non_attacking_placements(board):
    if len(board) < 1:
        return [[]]

    placements = []

    first_board_row = board[0]
    for i, square in enumerate(first_board_row):
        if square == 1: # square is disabled
            continue

        copied_board = [row[:] for row in board]
        for j, row in enumerate(copied_board):
            row[i] = 1
            if i - j >= 0:
                row[i - j] = 1
            if i + j < len(row):
                row[i + j] = 1

        placements.extend(map(lambda placement: [i] + placement, non_attacking_placements(copied_board[1:])))

    return placements

def n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    return non_attacking_placements(board)

def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("n_queens.py", 'n_queens.tsv', n_queens,
                                       comp))
