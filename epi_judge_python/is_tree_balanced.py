from test_framework import generic_test

def compute_if_balanced_and_whats_height(tree):
    """Return whether tree is balanced and what's its height."""

    if not tree:
        return True, -1

    l_balanced, l_height = compute_if_balanced_and_whats_height(tree.left)
    r_balanced, r_height = compute_if_balanced_and_whats_height(tree.right)
    height = max(l_height, r_height) + 1

    if not l_balanced or not r_balanced:
        return False, height
    else:
        return abs(l_height - r_height) <= 1, height

def is_balanced_binary_tree(tree):
    is_balanced, _ = compute_if_balanced_and_whats_height(tree)
    return is_balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
