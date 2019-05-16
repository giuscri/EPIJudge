from threading import Thread, RLock, get_ident, Condition
from time import sleep
from random import randint

import sys

ODD, EVEN = 0, 1
CURRENT_TURN = EVEN
CONDITION = Condition()
N = 100

def print_odd_numbers():
    for i in range(1, N + 1, 2):
        wait_turn(ODD)
        print(i)
        toggle_turn()

def print_even_numbers():
    for i in range(0, N + 1, 2):
        wait_turn(EVEN)
        print(i)
        toggle_turn()

def wait_turn(turn):
    if turn != CURRENT_TURN:
        CONDITION.acquire()
        CONDITION.wait() # wait() releases the lock and reacquire it when it wakes up
        CONDITION.release()

def toggle_turn():
    global CURRENT_TURN
    CURRENT_TURN = (CURRENT_TURN + 1) % 2

    CONDITION.acquire()
    CONDITION.notify()
    CONDITION.release()

t1, t2 = Thread(target=print_even_numbers), Thread(target=print_odd_numbers)

for thread in [t1, t2]:
    thread.start()

for thread in [t1, t2]:
    thread.join()
