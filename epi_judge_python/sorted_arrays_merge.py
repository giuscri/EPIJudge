from test_framework import generic_test

class HeapNode:
    """A node in the heap.

    It stores an integer, the index of the array the integer is coming from,
    and the index of the integer in that array."""

    def __init__(self, value, from_array_idx, in_array_idx):
        self.value = value
        self.from_array_idx = from_array_idx
        self.in_array_idx = in_array_idx

    def __repr__(self):
        return f"({self.value}, {self.from_array_idx}, {self.in_array_idx})"

def minimum(min_heap):
    """Returns minimum value stored in min_heap."""

    if min_heap is None or min_heap == []:
        return None

    return min_heap[0]

def insert(min_heap, n):
    """Inserts node `n` into provided min_heap."""

    if min_heap is None:
        min_heap = []

    min_heap.append(n)
    child_idx = len(min_heap) - 1
    while child_idx >= 0:
        parent_idx = (child_idx - 1) // 2

        if parent_idx >= 0 and min_heap[child_idx].value < min_heap[parent_idx].value:
            min_heap[child_idx], min_heap[parent_idx] = min_heap[parent_idx], min_heap[child_idx]
        else:
            break # we don't need to check this further

        child_idx = parent_idx

    return min_heap

def extract_minimum(min_heap):
    """Pops out mininum from min_heap, returns min_heap with its properties restored."""

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

        if right_child_idx < len(min_heap) and min_heap[right_child_idx].value < min_heap[left_child_idx].value:
            child_idx = right_child_idx
        else:
            child_idx = left_child_idx

        if min_heap[child_idx].value < min_heap[parent_idx].value:
            min_heap[child_idx], min_heap[parent_idx] = min_heap[parent_idx], min_heap[child_idx]
            parent_idx = child_idx
        else:
            break # we don't need to check this further

    return previous_minimum, min_heap

def merge_sorted_arrays(sorted_arrays):
    min_heap = None
    for i, array in enumerate(sorted_arrays):
        if not array:
            continue

        min_heap = insert(min_heap, HeapNode(array[0], i, 0))

    r = []
    while minimum(min_heap) is not None: # minimum() returns None when the heap is empty
        m, min_heap = extract_minimum(min_heap)
        r.append(m.value)
        if m.in_array_idx + 1 < len(sorted_arrays[m.from_array_idx]):
            n = HeapNode(sorted_arrays[m.from_array_idx][m.in_array_idx + 1], m.from_array_idx, m.in_array_idx + 1)
            min_heap = insert(min_heap, n)

    return r

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
