from test_framework import generic_test

class ListNode:
    def __init__(self, data, nxt):
        self.data = data
        self.nxt = nxt

def merge_two_sorted_lists(L1, L2):
    R = None

    l1_it = L1
    l2_it = L2
    r_it = R

    while l1_it or l2_it:
        if not l1_it and l2_it:
            if r_it:
                r_it.next = l2_it
                r_it = r_it.next
            else:
                r_it = R = l2_it

            l2_it = l2_it.next
        elif l1_it and not l2_it:
            if r_it:
                r_it.next = l1_it
                r_it = r_it.next
            else:
                r_it = R = l1_it

            l1_it = l1_it.next
        elif l1_it.data < l2_it.data:
            if r_it:
                r_it.next = l1_it
                r_it = r_it.next
            else:
                r_it = R = l1_it

            l1_it = l1_it.next
        elif l2_it.data <= l1_it.data:
            if r_it:
                r_it.next = l2_it
                r_it = r_it.next
            else:
                r_it = R = l2_it

            l2_it = l2_it.next

    return R


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
