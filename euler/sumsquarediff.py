import math
import time

# Project Euler problem 6 solution
# Result: 25174150, pass


def sum_squares(mx):
    sm = 0
    for i in range(1, mx):
        sm += math.pow(i, 2)

    return sm


def square_of_sum(mx):
    sm = 0
    sm = (mx * (mx + 1))/2

    return math.pow(sm, 2)

t1 = time.time()
print("Started: ", str(t1))
print(square_of_sum(100) - sum_squares(100))
t = time.time()
print("Finished: ", str(t))
print("Elapsed: ", str(t - t1))
