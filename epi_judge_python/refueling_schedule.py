import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

MPG = 20


# gallons[i] is the amount of gas in city i, and distances[i] is the
# distance city i to the next city.
def find_ample_city(gallons, distances):
    assert len(gallons) == len(distances), "`gallons` and `distances` should have the same length"

    n = len(gallons)

    for distance in distances:
        assert distance % MPG == 0, "each distance should be multiple of MPG"

    ample_city, tank, i = 0, 0, 0
    while ample_city < n:
        tank += gallons[i]
        if MPG * tank >= distances[i]:
            tank -= distances[i] // MPG # remove the miles needed to reach the next city
            i = (i + 1) % n

            if ample_city == i:
                return ample_city
        else:
            tank = 0
            ample_city = i + 1
            i = (i + 1) % n

    return -1

@enable_executor_hook
def find_ample_city_wrapper(executor, gallons, distances):
    result = executor.run(
        functools.partial(find_ample_city, gallons, distances))
    num_cities = len(gallons)
    tank = 0
    for i in range(num_cities):
        city = (result + i) % num_cities
        tank += gallons[city] * MPG - distances[city]
        if tank < 0:
            raise TestFailure('Out of gas on city {}'.format(i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("refueling_schedule.py",
                                       'refueling_schedule.tsv',
                                       find_ample_city_wrapper))
