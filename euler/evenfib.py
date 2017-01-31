from euler.util import timing

# Project Euler problem 2 solution
# Result: 4613732, pass

fibs = [0, 1, 1]


def learn_fib():
    for i in range(0, 40):
        calcnextfib = fibs[len(fibs) - 1] + fibs[len(fibs) - 2]
        if calcnextfib >= 4000000:
            print("max fib val reached\n")
            break
        else:
            print(str(calcnextfib))
            fibs.append(calcnextfib)


def sumevenfibs():
    s = 0
    for i in range(0, len(fibs)):
        # print(fibs[i])
        if fibs[i] % 2 == 0:
            print(str(fibs[i]))
            s += fibs[i]

    return s

timing.set_start_time()
learn_fib()
s = sumevenfibs()
print(str(s))
timing.get_elapsed()