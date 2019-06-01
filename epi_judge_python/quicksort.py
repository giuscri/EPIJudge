def partition(A, pivot):
  """Returns the index of pivot in A."""

  i, j = 0, len(A)-1
  while True:
    while i < len(A) and A[i] < pivot:
      i += 1

    while j >= 0 and A[j] > pivot:
      j -= 1

    if i >= j:
      return A, j

    A[i], A[j] = A[j], A[i]

  raise RuntimeError("you should not be here")

assert partition([1, 2, 3, 4], 2) == ([1, 2, 3, 4], 1)
assert partition([1, 4, -1, 8, 3, 9, -7], 8) == ([1, 4, -1, -7, 3, 8, 9], 5)

def _quicksort(A, start, stop):
  assert start >= 0 and stop >= 0

  if stop-start <= 1: # A is already sorted
    return A

  mid = (start + stop-1) // 2
  pivot = A[mid]
  A, pivot_idx = partition(A, pivot)
  _quicksort(A, start, pivot_idx)
  _quicksort(A, pivot_idx+1, stop)
  return A

def quicksort(A):
  assert len(set(A)) == len(A) # implementation assumes you have no duplicates
  return _quicksort(A, 0, len(A))

A = [1, 3, 2, 9, 4]
assert quicksort(A) == sorted(A)

A = [1, 3, 2, 3, 2]
try:
  quicksort(A)
  assert False
except AssertionError:
  assert True
