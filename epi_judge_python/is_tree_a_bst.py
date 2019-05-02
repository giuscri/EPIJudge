from test_framework import generic_test

from math import inf

def _is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):

    # If tree is emtpy, say it's still a BST but you should never reach this
    # point from another recursive call.
    if tree is None:
        return True, None, None

    # If tree is a leaf, it's a BST and its min and max are its value.
    if tree.left is None and tree.right is None:
        return True, tree.data, tree.data

    minimum_on_left, maximum_on_left = inf, -inf
    minimum_on_right, maximum_on_right = inf, -inf

    if tree.left is not None:
        bst, minimum_on_left, maximum_on_left = _is_binary_tree_bst(tree.left)
        if not bst or maximum_on_left > tree.data:
            return False, None, None

    if tree.right is not None:
        bst, minimum_on_right, maximum_on_right = _is_binary_tree_bst(tree.right)
        if not bst or minimum_on_right < tree.data:
            return False, None, None

    return True, min(minimum_on_left, minimum_on_right, tree.data), max(maximum_on_right, maximum_on_left, tree.data)

def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    bst, _, _ = _is_binary_tree_bst(tree, low_range, high_range)
    return bst

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
