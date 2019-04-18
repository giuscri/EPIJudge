from test_framework import generic_test

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head is None

    def inject(self, x):
        if self.tail is None:
            assert self.head is None
            self.head = Node(x, None)
            self.tail = self.head
        else:
            self.tail.next = Node(x, None)
            self.tail = self.tail.next

    def pop(self):
        if self.head is self.tail:
            x = self.head.data
            self.head = None
            self.tail = None
            return x
        elif self.head is None:
            assert self.tail is None
            return None
        else:
            x = self.head.data
            self.head = self.head.next
            return x

def binary_tree_depth_order(tree):
    if not tree:
        return []

    q1, q2 = Deque(), Deque()
    Q = [q1, q2]
    Q_idx = 0
    q1.inject(tree)
    result = []
    while not q1.empty() or not q2.empty():
        r = []
        while not Q[Q_idx].empty():
            n = Q[Q_idx].pop()
            r.append(n.data)
            if n.left is not None:
                Q[(Q_idx + 1) % 2].inject(n.left)
            if n.right is not None:
                Q[(Q_idx + 1) % 2].inject(n.right)
        result.append(r)
        Q_idx = (Q_idx + 1) % 2
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
