from util import primality
from util import timing


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

timing.set_start_time()

index_primes()
print(primes.pop())

timing.get_elapsed()
