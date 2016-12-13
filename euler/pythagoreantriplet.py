import math
import time

# Project Euler problem 9 solution
# Result: 31875000; pass

def theorem_test(a, b, c):
    product = math.pow(a, 2) + math.pow(b, 2)
    return product == math.pow(c, 2)
    

def triplet(a, b, c):
    return a * b * c

def find_solution():
    for x in range(1, 1000):
        for y in range(1, 1000):
            for z in range(1, 1000):
                if theorem_test(x, y, z) and (x + y + z) == 1000:
                    print("found values for a, b, c")
                    print("a: %d, b: %d, c: %d" % (x, y, z))
                    retval = x*y*z
                    print(str(retval))
                    return retval

def main():
    t1 = time.time()
    print("Started: ", str(t1))

    find_solution()
    
    t = time.time()
    print("Finished: ", str(t))
    print("Elapsed: ", str(t - t1))

if __name__ == "__main__":
    main()
