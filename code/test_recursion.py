from recursion import (is_palindrome,
                       total,
                       fibonacci,
                       binary_search,
                       factorial,
                       length)


def test_length():
    assert length([1, 5, 6, 7]) == 4
    assert length([]) == 0
    assert length([4, 5, 6, 2, 8, 9]) == 6
    assert length([1]) == 1


def test_total():
    assert total([]) == 0
    assert total([2]) == 2
    assert total([3, 9, 4, 1]) == 17
    assert total([3, 9, 10, 11]) == 33


def test_fatorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(8) == 40320
    assert factorial(5) == 120
    assert factorial(9) == 362880


def test_is_palindrome():
    assert is_palindrome('') is True
    assert is_palindrome('a') is True
    assert is_palindrome('abba') is True
    assert is_palindrome('abbab') is False
    assert is_palindrome('kanak') is True
    assert is_palindrome('123123') is False


def test_binary_search():
    assert binary_search([1, 4, 8, 9], 9) is True
    assert binary_search([], 1) is False
    assert binary_search([2, 3, 9, 10, 29], 13) is False
    assert binary_search([13], 3) is False
    assert binary_search([2], 2) is True


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    assert fibonacci(15) == 610
