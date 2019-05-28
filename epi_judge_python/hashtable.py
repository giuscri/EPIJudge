from random import randint
from functools import partial

def universal_hashing(k, m, p, a, b):
    return ((a * hash(k) + b) % p) % m

class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.next = None

class HashTable:
    def __init__(self):
        self.n = 0
        self.m = 3
        self.table = [None for _ in range(self.m)]

        self.p = 9181
        self.a = randint(0, self.p-1)
        self.b = randint(0, self.p-1)

    def rehash(self, m_primed):
        prev_table = self.table[:]
        self.m = m_primed
        self.n = 0
        self.table = [None for _ in range(self.m)]

        for head in prev_table:
            it = head
            while it:
                self.insert(it.k, it.v)
                it = it.next

    def search(self, k):
        idx = universal_hashing(k, self.m, self.p, self.a, self.b)
        it = self.table[idx]
        while it:
            if it.k == k:
                return it.v

            it = it.next

        return None

    def insert(self, k, v):
        self.delete(k)

        idx = universal_hashing(k, self.m, self.p, self.a, self.b)
        nxt = self.table[idx]
        self.table[idx] = Node(k, v)
        self.table[idx].next = nxt
        self.n += 1

        if self.n >= self.m:
            self.rehash(self.m * 2)

    def delete(self, k):
        idx = universal_hashing(k, self.m, self.p, self.a, self.b)
        prev, it = None, self.table[idx]
        while it:
            if it.k == k:
                break

            prev = it
            it = it.next

        if not it:
            return False

        if prev:
            prev.next = it.next
        else:
            self.table[idx] = it.next

        self.n -= 1

        if self.n < self.m // 4:
            self.rehash(self.m // 4)

        return True

if __name__ == "__main__":
    t = HashTable()

    for i in range(7):
        t.insert(i, "nothing")
