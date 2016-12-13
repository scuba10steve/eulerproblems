from util import primality
import time

# Project Euler problem 3 solution
# Result: 71, 839, 1471, 6857; pass

def is_prime(num):
    return primality.primality_test(num)


def largest_prime(num):
    prime_factors = []
    allprimes = []
    for i in range(3, num, 2):
        if is_prime(i) and num % i == 0:
            num = num / i
            print("num %d, factor %i" % (num, i))
            prime_factors.append(i)
            if num == 1:
                break

    return prime_factors

t1 = time.time()
print("Started: ", str(t1))
largest_prime(600851475143)
t = time.time()
print("Finished: ", str(t))
print("Elapsed: ", str(t - t1))
