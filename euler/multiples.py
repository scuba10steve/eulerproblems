import time


# Project Euler problem 1 solution
# Result: 233168, pass

def sumMultiples(x, y, max):
    i = 1
    x_mult = []
    y_mult = []
    z_mult = []

    # initialize multiple lists
    while i < max:
        prod = x * i
        # print("Product: " + str(prod))
        if prod >= max:
            break
        x_mult.append(prod)
        i += 1

    i = 1
    while i < max:
        prod = y * i
        # print("Product: " + str(prod))
        if prod >= max:
            break
        y_mult.append(prod)
        i += 1

    i = 1
    z = x * y
    while i < max:
        prod = z * i
        if prod >= max:
            break
        z_mult.append(prod)
        i += 1

    # sum them
    sum = 0
    i = 0
    print("Length x: ", len(x_mult))
    while i < len(x_mult):
        sum = sum + x_mult[i]
        i += 1

    prev = sum
    print("Sum x: ", sum)

    i = 0
    print("Length y: ", len(y_mult))
    while i < len(y_mult):
        sum = sum + y_mult[i]
        i += 1

    i = 0
    while i < len(z_mult):
        sum = sum - z_mult[i]
        i += 1

    print("Sum y: ", sum - prev)
    return sum

t1 = time.time()
print("Started: ", str(t1))
print(sumMultiples(3, 5, 1000))
t = time.time()
print("Finished: ", str(t))
print("Elapsed: ", str(t - t1))
