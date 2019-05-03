from test_framework import generic_test, test_utils

def count_nodes_in_bst(tree):
    if tree is None:
        return 0

    n = 1
    if tree.left is not None:
        n += count_nodes_in_bst(tree.left)
    if tree.right is not None:
        n += count_nodes_in_bst(tree.right)

    return n

def in_order_traversal(tree):
    if tree is None:
        return []

    sorted_keys = []

    if tree.left is not None:
        sorted_keys.extend(in_order_traversal(tree.left))

    sorted_keys.append(tree.data)

    if tree.right is not None:
        sorted_keys.extend(in_order_traversal(tree.right))

    return sorted_keys

def find_k_largest_in_bst(tree, k):
    n = count_nodes_in_bst(tree)
    sorted_keys = in_order_traversal(tree)
    k_largest = []
    for i in range(n - k, n):
        k_largest.append(sorted_keys[i])

    return k_largest


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
