from test_framework import generic_test
from test_framework.test_failure import TestFailure

from math import inf

class LruCache:
    """Implements LRU cache of book prices.

    The LRU policy is implemented by storing, together with the book price,
    the _rank_. The rank is incremented throughout the life of the cache.
    It's like a ticking clock: each time a new element enters the cache the
    rank is incremented. Hence, the element with the lowest rank is the
    element that's the oldest.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.n = 0
        self.current_rank = 0
        self.dict = dict()
        return

    def lookup(self, isbn):
        """Lookups price book. Returns -1 if there's no book for that ISBN."""

        price, rank = self.dict.get(isbn, (-1, None))
        if price >= 0: # book is in cache
            self.dict[isbn] = (price, self.current_rank)

            # Prepare current_rank for the next assignment
            self.current_rank += 1

        return price

    def insert(self, isbn, price):
        """Inserts price for `isbn`, removes LRU element if exceeding capacity."""

        if isbn in self.dict.keys():
            # Just update the rank of the cache entry

            price, rank = self.dict[isbn]
            self.dict[isbn] = (price, self.current_rank)

            # Prepare `current_rank` for the next assignment
            self.current_rank += 1

            return # we don't want to replace values already in the cache

        if self.n >= self.capacity:
            lowest_rank = inf
            isbn_with_lowest_rank = None
            for key in self.dict:
                _, rank = self.dict[key]
                if rank < lowest_rank:
                    lowest_rank = rank
                    isbn_with_lowest_rank = key

            self.erase(isbn_with_lowest_rank)

        self.dict[isbn] = (price, self.current_rank)

        # Increment the number of keys stored in the cache
        self.n += 1

        # Increment rank for the next insertion
        self.current_rank += 1

        return

    def erase(self, isbn):
        if isbn not in self.dict:
            return False

        del self.dict[isbn] # https://stackoverflow.com/questions/51800639/complexity-of-deleting-a-key-from-python-ordered-dict
        self.n -= 1
        return True


def run_test(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure(
                    'Lookup: expected ' + str(cmd[2]) + ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure(
                    'Erase: expected ' + str(cmd[2]) + ', got ' + str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lru_cache.py", 'lru_cache.tsv',
                                       run_test))
