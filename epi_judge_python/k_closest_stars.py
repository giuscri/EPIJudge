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

def minimum(min_heap):
    """Returns minimum value stored in min_heap."""

    if min_heap is None or min_heap == []:
        return None

    return min_heap[0]

def insert(min_heap, star, k):
    """Inserts star into provided min_heap, truncate heap after the first k nodes."""

    if min_heap is None:
        min_heap = []

    min_heap.append(star)
    child_idx = len(min_heap) - 1

    while child_idx >= 0:
        parent_idx = (child_idx - 1) // 2

        if parent_idx >= 0 and min_heap[child_idx] < min_heap[parent_idx]:
            min_heap[child_idx], min_heap[parent_idx] = min_heap[parent_idx], min_heap[child_idx]
        else:
            break # we don't need to check this further

        child_idx = parent_idx

    maximum_idx = 0
    for i, star in enumerate(min_heap):
        if star > min_heap[maximum_idx]:
            maximum_idx = i

    min_heap[maximum_idx], min_heap[-1] = min_heap[-1], min_heap[maximum_idx]

    parent_idx = maximum_idx
    while parent_idx < len(min_heap):
        left_child_idx = 2 * parent_idx + 1
        right_child_idx = 2 * parent_idx + 2

        if left_child_idx >= len(min_heap):
            break # min_heap[parent_idx] is a leaf
        elif right_child_idx >= len(min_heap):
            child_idx = left_child_idx
        elif min_heap[left_child_idx] < min_heap[right_child_idx]:
            child_idx = left_child_idx
        else:
            child_idx = right_child_idx

        if min_heap[parent_idx] > min_heap[child_idx]:
            min_heap[parent_idx], min_heap[child_idx] = min_heap[child_idx], min_heap[parent_idx]
        else:
            break # we don't need to check this further

    return min_heap[:k]

def extract_minimum(min_heap):
    """Pops out mininum from min_heap, returns min_heap with min_heap properties restored."""

    if min_heap is None or min_heap == []:
        return None, min_heap

    min_heap[0], min_heap[-1] = min_heap[-1], min_heap[0]
    previous_minimum = min_heap[-1]
    min_heap = min_heap[:-1] # slicing off the root just moved to the end of the array
    parent_idx = 0
    while parent_idx < len(min_heap):
        left_child_idx = 2 * parent_idx + 1
        right_child_idx = 2 * parent_idx + 2

        if left_child_idx >= len(min_heap):
            break

        if right_child_idx < len(min_heap) and min_heap[right_child_idx] < min_heap[left_child_idx]:
            child_idx = right_child_idx
        else:
            child_idx = left_child_idx

        if min_heap[child_idx] < min_heap[parent_idx]:
            min_heap[child_idx], min_heap[parent_idx] = min_heap[parent_idx], min_heap[child_idx]
            parent_idx = child_idx
        else:
            break # we don't need to check this further

    return previous_minimum, min_heap

def find_closest_k_stars(stars, k):
    min_heap = None
    for star in stars:
        min_heap = insert(min_heap, star, k)

    r = []
    for _ in range(k):
        m, min_heap = extract_minimum(min_heap)
        r.append(m)

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
