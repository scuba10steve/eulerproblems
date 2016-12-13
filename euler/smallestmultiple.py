from util import factorial
import time

# Project Euler problem 5 solution
# Result: ? fail


def is_divisible_1_20(num):
    divisible = False

    for i in range(2, 20):
        if num % i != 0:
            divisible = False
            break
        else:
            divisible = True

    return divisible

t1 = time.time()
print("Started: ", str(t1))
smallest_product = 0
i = 2
while i < factorial.factorial(20):
    if is_divisible_1_20(i):
        smallest_product = i
        print(i)
        break
    i += 20

print(smallest_product)
t = time.time()
print("Finished: ", str(t))
print("Elapsed: ", str(t - t1))
