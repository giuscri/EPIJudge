from threading import Thread, Condition, Lock
from time import sleep
from random import randint

TURN = 0 # 0 for even, 1 for odd
CONDITION = Condition()
N = 10

TOGGLE_TURN = Lock()
def toggle_turn():
  with TOGGLE_TURN:
    global TURN
    TURN = (TURN+1) % 2

CHECK_TURN_LOCK = Lock()
def check_turn(turn):
  CHECK_TURN_LOCK.acquire()
  while TURN != turn:
    with CONDITION:
      # Just before `wait()`ing, release CHECK_TURN_LOCK as Object.wait()
      # releases the Object monitor in Java
      CHECK_TURN_LOCK.release()
      CONDITION.wait()

  if CHECK_TURN_LOCK.locked():
    CHECK_TURN_LOCK.release()

def print_even_numbers():
  for counter in range(0, N+1, 2):
    # Introduce some evil
    sleep(randint(0, 4))

    # check_turn() does acquire a Lock, enters a while-loop and doesn't exit
    # until TURN it's 0 -- it doesn't do busy waiting though. Then the Lock is
    # released.
    check_turn(0)

    print(counter)

    # toggle_turn() does acquire a Lock, changes the value of TURN, then
    # releases the Lock.
    toggle_turn()

    with CONDITION:
      CONDITION.notify()

def print_odd_numbers():
  for counter in range(1, N+1, 2):
    # Introduce some evil
    sleep(randint(0, 4))

    # check_turn() does acquire a Lock, enters a while-loop and doesn't exit
    # until TURN it's 1 -- it doesn't do busy waiting though. Then the Lock is
    # released.
    check_turn(1)

    print(counter)

    # toggle_turn() does acquire a Lock, changes the value of TURN, then
    # releases the Lock.
    toggle_turn()

    with CONDITION:
      CONDITION.notify()

even_numbers_thread = Thread(target=print_even_numbers)
odd_numbers_thread = Thread(target=print_odd_numbers)

odd_numbers_thread.start()
even_numbers_thread.start()

for thread in (even_numbers_thread, odd_numbers_thread):
  thread.join()

print("completed!")
