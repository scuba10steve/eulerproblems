from util import primality
import time


# Project Euler problem 10 solution
# Result: , pass


def is_prime(number):
    return primality.primality_test(number)


def sieve(p_list):
    i = 0
    while i < len(p_list):
        p = p_list[i]
        if i + 1 >= len(p_list):
            break
        j = i + 1
        while j < len(p_list):
            if p_list[j] % p == 0:
                p_list.pop(j)
            j += 1

        i += 1

    # Returns a filtered list of primes
    print("size: ", len(p_list))
    return p_list

def generate_list(mx):
    ls = []
    for i in range(2, mx):
        ls.append(i)

    return ls


def main():

    t1 = time.time()
    print("Started: ", str(t1))
    p_list = generate_list(2000000)
    p_list = sieve(p_list)
    s = 0
    for item in p_list:
        s += item

    print("Sum = ", s)
    t = time.time()
    print("Finished: ", str(t))
    print("Elapsed: ", str(t - t1))


if __name__ == "__main__":
    main()

