from assignment1 import is_prime, get_primes


def test_is_prime():
    assert is_prime(12) is False
    assert is_prime(7) is True
    assert is_prime(103) is True
    assert is_prime(99) is False
    assert is_prime(21) is False


def test_prime_numes():
    assert get_primes(10) == [2, 3, 5, 7]
    assert get_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert get_primes(5) == [2, 3]
    assert get_primes(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                               43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
