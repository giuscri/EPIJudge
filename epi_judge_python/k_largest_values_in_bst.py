from test_framework import generic_test, test_utils

def _find_k_largest_in_bst(tree, k, r):
    if k == 0:
        return r, k

    if tree.right is not None:
        r, k = _find_k_largest_in_bst(tree.right, k, r)
    if k == 0:
        return r, k

    r.append(tree.data)
    k -= 1
    if k == 0:
        return r, k

    if tree.left is not None:
        r, k = _find_k_largest_in_bst(tree.left, k, r)

    return r, k

def find_k_largest_in_bst(tree, k):
    r, k = _find_k_largest_in_bst(tree, k, [])
    assert k == 0
    return r

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
