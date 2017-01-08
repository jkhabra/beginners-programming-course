def is_possible(num, a=6, b=9, c=20):
    """Returns True if it is possible to make a combination of
       `a`,`b`,`c` which is equal to `num`"""
    for x in range(0, num):
        for y in range(0, num):
            for z in range(0, num):
                if x * a + y * b + z * c == num:
                    return True
    return False


def max_impossible(a=6, b=9, c=20):
    """Return the biggest number that can't be made with the combination
       of a, b, c"""
    count = 0
    not_possible = 1
    max_impossible = not_possible

    while True:
        if is_possible(not_possible, a, b, c):
            count += 1
        else:
            count = 0
            max_impossible = not_possible

        if count == 6:
            return max_impossible

        not_possible += 1
