import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def depth(node):
    """Compute the depth for a node of a binary tree."""
    d = 0
    iterator = node.parent
    while iterator:
        d += 1
        iterator = iterator.parent
    return d

def lca(node0, node1):
    """Compute the lowest common ancestor of node0 and node1."""
    node0_depth = depth(node0)
    node1_depth = depth(node1)

    node0_ancestor = node0
    node1_ancestor = node1

    if node0_depth > node1_depth:
        while node0_depth > node1_depth:
            node0_ancestor = node0_ancestor.parent
            node0_depth -= 1
    elif node1_depth > node0_depth:
        while node1_depth > node0_depth:
            node1_ancestor = node1_ancestor.parent
            node1_depth -= 1

    while node0_ancestor is not node1_ancestor:
        if node0_ancestor is None or node1_ancestor is None:
            raise ValueError(f"{node0} and {node1} do not belong to the same tree.")

        node0_ancestor = node0_ancestor.parent
        node1_ancestor = node1_ancestor.parent

    return node0_ancestor


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor_with_parent.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
