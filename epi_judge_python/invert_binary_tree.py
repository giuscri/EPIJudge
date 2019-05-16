def by_levels(binary_tree):
    """Returns a list with nodes sorted by increasing depth. Nodes at the
    same level appears from left to right."""

    if binary_tree is None:
        return binary_tree

    queue = [binary_tree]
    i = 0

    while i < len(queue):
        parent = queue[i]
        if parent.right is not None:
            queue.append(parent.right)
        if parent.left is not None:
            queue.append(parent.left)
        i += 1

    return queue


def mirror(binary_tree):
    """Returns binary_tree _inverted_."""

    if binary_tree is None:
        return binary_tree

    queue = [binary_tree]
    i = 0

    while i < len(queue):
        parent = queue[i]
        if parent.left is not None:
            queue.append(parent.left)
        if parent.right is not None:
            queue.append(parent.right)
        i += 1

    for i in range(len(queue)):
        parent = queue[i]
        if 2*i + 1 < len(queue):
            parent.left = queue[2*i + 1]
        if 2*i + 2 < len(queue):
            parent.right = queue[2*i + 2]

    return binary_tree

class Node:
    def __init__(self, payload, left=None, right=None):
        self.payload = payload
        self.left = left
        self.right = right

    def __repr__(self):
        return self.payload

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")

A.left = B
A.right = C

B.left = D
B.right = E

C.left = F
C.right = G

binary_tree = A
binary_tree = mirror(binary_tree)
print(by_levels(binary_tree))
