from util import palindrome
from util import timing

# Project Euler problem 4 solution
# Result: 906609, pass


def is_palindrome(object):
    return palindrome.is_palindrome(object)


def get_largest_palindrome():
    product = 0
    largest_product = 0

    for i in range(100, 999):
        for j in range(100, 999):
            product = i * j

            if largest_product == 0:
                if is_palindrome(product):
                    largest_product = product
            else:
                if is_palindrome(product):
                    # print(product)
                    if product > largest_product:
                        print("factor1: %d, factor2: %d" % (i, j))
                        largest_product = product

    return largest_product


timing.set_start_time()

print(str(get_largest_palindrome()))

timing.get_elapsed()