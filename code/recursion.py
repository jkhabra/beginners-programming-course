def length(ls):
    """Returns length of `ls` list"""
    if ls == []:
        return 0
    return 1 + length(ls[1:])


def total(ls):
    """Returns sum of all numbers from `ls`"""
    if ls == []:
        return 0
    return ls[0] + total(ls[1:])


def factorial(num):
    """Returns factorial of `num`"""
    if num <= 1:
        return 1
    return num * factorial(num - 1)


def is_palindrome(string):
    """Returns True if `string` is  palindrome, else False"""
    if len(string) <= 1:
        return True
    return string[0] == string[-1] and is_palindrome(string[1:-1])


def binary_search(ls, num):
    """Returns True if `num` exist in `ls`"""
    mid = len(ls) // 2
    print(mid, num, ls)

    if len(ls) < 1:
        return False

    if len(ls) == 1:
        return ls[0] == num

    if ls[mid] == num:
        return True

    if ls[mid] > num:
        return binary_search(ls[:mid], num)
    else:
        return binary_search(ls[mid:], num)


def fibonacci(num):
    """Returns `num`th number of fibonacci series"""
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num > 1:
        return fibonacci(num - 1) + fibonacci(num - 2)
