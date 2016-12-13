def is_palindrome(object):
    if type(object) is int:
        return is_palindrome_str(str(object))
    else:
        return is_palindrome_str(object)


def is_palindrome_str(object):
    i = 0
    j = len(object) - 1

    while (i != j) and (j >= i):
        if object[i] != object[j]:
            return False
        if j == i:
            break

        i += 1
        j -= 1

    return True
