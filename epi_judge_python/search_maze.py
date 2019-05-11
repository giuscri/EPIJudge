import collections
import copy
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

def create_coordinate_if_defined_and_not_wall(i, j, r, c, maze):
    if i not in range(r):
        return None
    if j not in range(c):
        return None
    if maze[i][j] == 1:
        return None

    return Coordinate(i, j)

def maze_as_graph(maze):
    G = dict()
    r, c = len(maze), len(maze[0])

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            vertex = create_coordinate_if_defined_and_not_wall(i, j, r, c, maze)
            if vertex is None:
                continue

            adjacent = create_coordinate_if_defined_and_not_wall(i-1, j, r, c, maze)
            if adjacent is not None:
                G[vertex] = G.get(vertex, []) + [adjacent]

            adjacent = create_coordinate_if_defined_and_not_wall(i, j-1, r, c, maze)
            if adjacent is not None:
                G[vertex] = G.get(vertex, []) + [adjacent]

            adjacent = create_coordinate_if_defined_and_not_wall(i, j+1, r, c, maze)
            if adjacent is not None:
                G[vertex] = G.get(vertex, []) + [adjacent]

            adjacent = create_coordinate_if_defined_and_not_wall(i+1, j, r, c, maze)
            if adjacent is not None:
                G[vertex] = G.get(vertex, []) + [adjacent]

    return G

def _search_maze(G, s, e, visited):
    visited.add(s)

    if s == e:
        return [e]

    for adjacent in G[s]:
        if adjacent in visited:
            continue

        path = _search_maze(G, adjacent, e, visited)
        if path is not None:
            return [s] + path

    return None

def search_maze(maze, s, e):
    G = maze_as_graph(maze)
    if s not in G:
        return None
    if e not in G:
        return None

    return _search_maze(G, s, e, set())

def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure("Path doesn't lay between start and end points")

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure("Path contains invalid segments")

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_maze.py", 'search_maze.tsv',
                                       search_maze_wrapper))
