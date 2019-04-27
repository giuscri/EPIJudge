from test_framework import generic_test

def maximum(max_heap):
    """Returns maximum value stored in max_heap."""

    if max_heap is None or max_heap == []:
        return None

    return max_heap[0]

def insert(max_heap, x):
    """Inserts `x` into provided max_heap."""
    if max_heap is None:
        max_heap = []

    max_heap.append(x)
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
    """Pops out maximum from max_heap, returns max_heap with its properties restored."""

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
            break

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

def merge_sorted_arrays(sorted_arrays):
    r = []
    max_heap = None
    for array in sorted_arrays:
        for x in array:
            max_heap = insert(max_heap, x)

    x, max_heap = extract_maximum(max_heap)
    while x is not None:
        r.append(x)
        x, max_heap = extract_maximum(max_heap)

    return list(reversed(r))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
