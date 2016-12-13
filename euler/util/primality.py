import sys, argparse


def primality_test(number):
    if number == 2:
        return True
    elif number % 2 == 0:
        return False
    elif number == 3:
        return True
    elif number % 3 == 0:
        return False
    elif number == 5:
        return True
    elif number % 5 == 0:
        return False
    else:
        i = 7
        while i * i <= number:
            if number % i == 0:
                return False
            i += 2

        return True


def handle_args():
    parser = argparse.ArgumentParser(description='Process integers')
    parser.add_argument('-n', type=int, help='an integer to calculate')
    args = parser.parse_args()

    if args.n:
        return args.n
    else:
        return None


def main():
    num = handle_args()
    if num:
        print(num)
    else:
        num = int(input("Enter a number for primalityTest: "))

    retval = primality_test(num)
    print(retval)


if __name__ == "__main__":
    main()
