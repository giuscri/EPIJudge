def partition(A, pivot):
  mid_start, mid_end = -1, -1

  i, j = 0, len(A)-1
  while True:
    while i < len(A) and A[i] < pivot:
      i += 1

    while j >= 0 and A[j] >= pivot:
      j -= 1

    if i >= j:
      break

    A[i], A[j] = A[j], A[i]

  mid_start = i
  i, j = mid_start, len(A)-1
  while True:
    while i < len(A) and A[i] == pivot:
      i += 1

    while j >= 0 and A[j] > pivot:
      j -= 1

    if i >= j:
      break

    A[i], A[j] = A[j], A[i]

  mid_end = i
  return A, mid_start, mid_end

assert partition([1, 2, 3, 4], 2) == ([1, 2, 3, 4], 1, 2)
assert partition([1, 4, -1, 8, 3, 9, -7], 8) == ([1, 4, -1, -7, 3, 8, 9], 5, 6)

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
  return _quicksort(A, 0, len(A))

A = [1, 3, 2, 9, 4]
assert quicksort(A) == sorted(A)

A = [1, 3, 2, 3, 2]
assert quicksort(A) == sorted([1, 3, 2, 3, 2])
