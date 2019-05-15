from test_framework import generic_test

from string import ascii_lowercase

def adjacent(word1, word2): # time: O(|word1|)
    """Returns True if word1 and word2 have the same length and differ only
    by one character."""

    if len(word1) != len(word2):
        return False

    n_different_characters = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            n_different_characters += 1
        if n_different_characters > 1:
            return False

    return True

def shortest_path(dictionary, source, destination):
    queue = [(source, 0)]
    visited = {source}

    while len(queue) > 0:
        vertex, n = queue.pop(0)

        if vertex == destination:
            return n

        for i in range(len(vertex)):
            for c in ascii_lowercase:
                adjacent = vertex[:i] + c + vertex[i+1:]

                if adjacent in visited:
                    continue

                if adjacent in dictionary:
                    queue.append((adjacent, n+1))
                    visited.add(adjacent)

    return -1

# Uses BFS to find the least steps of transformation.
def transform_string(D, s, t):
    return shortest_path(D, s, t)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_transformability.py",
                                       'string_transformability.tsv',
                                       transform_string))
