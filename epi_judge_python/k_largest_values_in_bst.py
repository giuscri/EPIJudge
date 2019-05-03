from test_framework import generic_test, test_utils

def find_k_largest_in_bst(tree, k):
    if tree is None:
        return []

    result = []
    stack = [tree]
    pushed = set()

    while len(result) < k and len(stack) > 0:
        node = stack.pop()
        if node.left is None and node.right is None:
            result.append(node.data)
        elif (node.left is not None and node.left in pushed) or (node.right is not None and node.right in pushed):
            result.append(node.data)
        else:
            if node.left is not None:
                stack.append(node.left)
                pushed.add(node.left)

            stack.append(node)
            pushed.add(node)

            if node.right is not None:
                stack.append(node.right)
                pushed.add(node.right)

    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
