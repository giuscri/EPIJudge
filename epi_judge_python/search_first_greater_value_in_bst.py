from test_framework import generic_test

def _find_first_greater_than_k(tree, k):
    if tree is None:
        return []

    sorted_keys = []
    sorted_keys.extend(_find_first_greater_than_k(tree.left, k))
    sorted_keys.append(tree.data)
    sorted_keys.extend(_find_first_greater_than_k(tree.right, k))

    return sorted_keys

def find_first_greater_than_k(tree, k):
    class R:
        def __init__(self, data):
            self.data = data

    sorted_keys = _find_first_greater_than_k(tree, k)
    previous = None
    for key in sorted_keys:
        if (previous is None or previous <= k) and key > k:
            return R(key)

        previous = key

    return None

def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_first_greater_value_in_bst.py",
                                       'search_first_greater_value_in_bst.tsv',
                                       find_first_greater_than_k_wrapper))
