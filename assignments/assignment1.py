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
