def partition(A, pivot):
  """Returns the index of pivot in A."""

  smaller_than_pivot = [x for x in A if x < pivot]
  equal_to_pivot = [x for x in A if x == pivot]
  larger_than_pivot = [x for x in A if x > pivot]
  A[:] = smaller_than_pivot + equal_to_pivot + larger_than_pivot
  return A, len(smaller_than_pivot), len(smaller_than_pivot) + len(equal_to_pivot)

assert partition([1, 2, 3, 4], 2) == ([1, 2, 3, 4], 1, 2)
assert partition([1, 4, -1, 8, 3, 9, -7], 8) == ([1, 4, -1, 3, -7, 8, 9], 5, 6)

def _quicksort(A, start, stop):
  assert start >= 0 and stop >= 0

  if stop-start <= 1: # A is already sorted
    return A

  mid = (start + stop-1) // 2
  pivot = A[mid]
  A, i, j = partition(A, pivot)
  _quicksort(A, start, i)
  _quicksort(A, j, stop)
  return A

def quicksort(A):
  #assert len(set(A)) == len(A) # implementation assumes you have no duplicates
  return _quicksort(A, 0, len(A))

A = [1, 3, 2, 9, 4]
assert quicksort(A) == sorted(A)

A = [1, 3, 2, 3, 2]
assert quicksort(A) == sorted([1, 3, 2, 3, 2])
