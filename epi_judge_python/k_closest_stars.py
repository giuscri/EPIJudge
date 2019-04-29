import functools
import math

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class Star:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __lt__(self, rhs):
        return self.distance < rhs.distance

    def __repr__(self):
        return str(self.distance)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, rhs):
        return math.isclose(self.distance, rhs.distance)

def maximum(max_heap):
    """Returns maximum value stored in max_heap."""

    if max_heap is None or max_heap == []:
        return None

    return max_heap[0]

def insert(max_heap, star):
    """Inserts star into provided max_heap."""

    if max_heap is None:
        max_heap = []

    max_heap.append(star)
    child_idx = len(max_heap) - 1

    while child_idx >= 0:
        parent_idx = (child_idx - 1) // 2

        if parent_idx >= 0 and max_heap[child_idx] > max_heap[parent_idx]:
            max_heap[child_idx], max_heap[parent_idx] = max_heap[parent_idx], max_heap[child_idx]
        else:
            break # we don't need to check this further

        child_idx = parent_idx

    return max_heap

def extract_maximum(max_heap):
    """Pops out maxinum from max_heap, returns max_heap with max_heap properties restored."""

    if max_heap is None or max_heap == []:
        return None, max_heap

    max_heap[0], max_heap[-1] = max_heap[-1], max_heap[0]
    previous_maximum = max_heap[-1]
    max_heap = max_heap[:-1] # slicing off the root just moved to the end of the array
    parent_idx = 0
    while parent_idx < len(max_heap):
        left_child_idx = 2 * parent_idx + 1
        right_child_idx = 2 * parent_idx + 2

        if left_child_idx >= len(max_heap):
            break # parent was a leaf

        if right_child_idx < len(max_heap) and max_heap[right_child_idx] > max_heap[left_child_idx]:
            child_idx = right_child_idx
        else:
            child_idx = left_child_idx

        if max_heap[child_idx] > max_heap[parent_idx]:
            max_heap[child_idx], max_heap[parent_idx] = max_heap[parent_idx], max_heap[child_idx]
            parent_idx = child_idx
        else:
            break # we don't need to check this further

    return previous_maximum, max_heap

def find_closest_k_stars(stars, k):
    max_heap = []
    for star in stars:
        if len(max_heap) < k:
            max_heap = insert(max_heap, star)
            continue

        if star < maximum(max_heap):
            _, max_heap = extract_maximum(max_heap)
            max_heap = insert(max_heap, star)

    r = []
    for _ in range(k):
        m, max_heap = extract_maximum(max_heap)
        r.append(m)

    r.reverse()
    return r


def comp(expected_output, output):
    if len(output) != len(expected_output):
        return False
    return all(
        math.isclose(s.distance, d)
        for s, d in zip(sorted(output), expected_output))


@enable_executor_hook
def find_closest_k_stars_wrapper(executor, stars, k):
    stars = [Star(*a) for a in stars]
    return executor.run(
        functools.partial(find_closest_k_stars, iter(stars), k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("k_closest_stars.py",
                                       "k_closest_stars.tsv",
                                       find_closest_k_stars_wrapper, comp))
