import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

NUM_PEGS = 3

def _compute_tower_hanoi(num_rings, from_peg, to_peg):
    if num_rings == 1:
        return [(from_peg, to_peg)]

    intermediate_peg = {0, 1, 2}.difference({from_peg, to_peg}).pop()

    moves = _compute_tower_hanoi(num_rings - 1, from_peg, intermediate_peg)
    moves.append((from_peg, to_peg))
    moves.extend(_compute_tower_hanoi(num_rings - 1, intermediate_peg, to_peg))

    return moves

def compute_tower_hanoi(num_rings):
    return _compute_tower_hanoi(num_rings, 0, 1)


@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(
        1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure("Illegal move from {} to {}".format(
                pegs[from_peg][-1], pegs[to_peg][-1]))
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure("Pegs doesn't place in the right configuration")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("hanoi.py", 'hanoi.tsv',
                                       compute_tower_hanoi_wrapper))
