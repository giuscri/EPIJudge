from test_framework import generic_test
from test_framework.test_failure import TestFailure

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self._top = None
        self._max = None

    def empty(self):
        return self._top is None

    def max(self):
        if not self._max:
            return None
        return self._max.data

    def pop(self):
        if not self._top:
            return None

        x = self._top.data
        self._top = self._top.next
        self._max = self._max.next
        return x

    def push(self, x):
        n = Node(x, self._top)
        if not self._max:
            m = Node(x, self._max)
        else:
            m = Node(max(self.max(), x), self._max)
        self._top = n
        self._max = m


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("stack_with_max.py",
                                       'stack_with_max.tsv', stack_tester))
