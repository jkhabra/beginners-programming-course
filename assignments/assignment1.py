from math import log10


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def get_primes(numbers):
    primes = []

    for i in range(2, numbers):
        if is_prime(i) is True:
            primes.append(i)

    return primes


def prime_log_sum(num):
    sum_of_log = 0

    if num == 0:
        return ()

    for i in get_primes(num):
        sum_of_log += log10(i)
        ratio = sum_of_log / num

    return (sum_of_log, num, ratio)
