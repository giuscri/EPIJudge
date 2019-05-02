from test_framework import generic_test

def _find_first_greater_than_k(tree, k, smallest_larger_than_k_node):
    if tree is None:
        return smallest_larger_than_k_node

    if k < tree.data:
        if smallest_larger_than_k_node is None or smallest_larger_than_k_node.data > tree.data:
            smallest_larger_than_k_node = tree

        return _find_first_greater_than_k(tree.left, k, smallest_larger_than_k_node)
    elif k > tree.data:
        return _find_first_greater_than_k(tree.right, k, smallest_larger_than_k_node)
    elif k == tree.data:
        return _find_first_greater_than_k(tree.right, k, smallest_larger_than_k_node)

def find_first_greater_than_k(tree, k):
    return _find_first_greater_than_k(tree, k, None)


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_first_greater_value_in_bst.py",
                                       'search_first_greater_value_in_bst.tsv',
                                       find_first_greater_than_k_wrapper))
