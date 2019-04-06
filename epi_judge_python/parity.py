from test_framework import generic_test

LOOKUP_TABLE = None

def return_lookup_table(): # O(2**k)
    global LOOKUP_TABLE
    if LOOKUP_TABLE: return LOOKUP_TABLE

    lookup_table = dict()
    for x in range(2**16):
        lookup_table[x] = _parity(x)

    LOOKUP_TABLE = lookup_table

    return LOOKUP_TABLE


def _parity(x): # O(log(n)) - assuming that the XOR of two words is constant!
    x = x ^ (x >> 32)
    x = x ^ (x >> 16)
    x = x ^ (x >> 8)
    x = x ^ (x >> 4)
    x = x ^ (x >> 2)
    x = x ^ (x >> 1)
    return x & 1


def parity(x): # O(n/k)
    """Returns 1 if the number of 1s in the word is odd; otherwise, returns 0.
    """
    # We want to run this code for a very large number of 64-bit words. So we
    # want something that performs better than the straightforward approach,
    # and we expect to do the same computation over and over. That may mean
    # that we'd like to do some precomputation step if that allows us to
    # perform better on the single case.
    lookup_table = return_lookup_table()
    return lookup_table[x & (2**16 - 1)] ^ lookup_table[(x >> 16) & (2**16 - 1)] ^ lookup_table[(x >> 32) & (2**16 - 1)] ^ lookup_table[(x >> 48) & (2**16 - 1)]

# overall complexity is `O(2**k) * O(log(n)) + m * O(n/k)`, where m is the number of words.


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
