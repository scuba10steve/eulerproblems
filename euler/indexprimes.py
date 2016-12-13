from util import primality
import time


# Project Euler problem 7 solution
# Result: 233168, pass


def is_prime(num):
    return primality.primality_test(num)


primes = [1, 2]


def index_primes():
    i = 3
    while len(primes) < 10001:
        while is_prime(i) != True:
            i += 2

        print("Next Prime found: ", i)
        primes.append(i)
        i += 2

t1 = time.time()
print("Started: ", str(t1))

index_primes()
print(primes.pop())
t = time.time()

print("Finished: ", str(t))
print("Elapsed: ", str(t - t1))
