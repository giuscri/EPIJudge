import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def has_cycle(head):
    slow_iterator = head
    fast_iterator = head
    element_of_cycle = None
    while fast_iterator:
        if slow_iterator.next and fast_iterator.next and fast_iterator.next.next:
            slow_iterator = slow_iterator.next
            fast_iterator = fast_iterator.next.next
        else:
            return None

        if slow_iterator is fast_iterator:
            element_of_cycle = slow_iterator
            break

    cycle_len = 1
    iterator = element_of_cycle.next
    while iterator is not element_of_cycle:
        cycle_len += 1
        iterator = iterator.next

    iterator1 = head
    iterator2 = iterator1
    for _ in range(cycle_len):
        iterator2 = iterator2.next

    while iterator1 is not iterator2:
        iterator1 = iterator1.next
        iterator2 = iterator2.next

    return iterator1

@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError("Can't cycle empty list")
        cycle_start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == cycle_idx:
                cycle_start = cursor
            cursor = cursor.next
            cycle_length += 1 if cycle_start is not None else 0

        if cursor.data == cycle_idx:
            cycle_start = cursor
        if cycle_start is None:
            raise RuntimeError("Can't find a cycle start")
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure("Found a non-existing cycle")
    else:
        if result is None:
            raise TestFailure("Existing cycle was not found")
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    "Returned node does not belong to the cycle or is not the closest node to the head"
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            "Returned node does not belong to the cycle or is not the closest node to the head"
        )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_list_cyclic.py", 'is_list_cyclic.tsv', has_cycle_wrapper))
