from threading import Thread, RLock, get_ident
from time import sleep
from random import randint

import sys

LOCK = RLock()
COUNTER = 0

def print_and_increase(only_odd=True):
    global COUNTER

    i, only_even = 0, not only_odd

    while i < 100:
        LOCK.acquire()

        if COUNTER % 2 == 0 and only_even:
            COUNTER += 1
            i += 1
            print(f"{COUNTER} - printed by thread {get_ident()}")
        elif COUNTER % 2 != 0 and only_odd:
            COUNTER += 1
            i += 1
            print(f"{COUNTER} - printed by thread {get_ident()}")

        LOCK.release()

t1, t2 = Thread(target=print_and_increase, kwargs={"only_odd": True}), Thread(target=print_and_increase, kwargs={"only_odd": False})

for thread in [t1, t2]:
    thread.start()

for thread in [t1, t2]:
    thread.join()
