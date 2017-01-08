def is_possible(num, a=6, b=9, c=20):
    """Returns True if it is possible to make a combination of
       `a`,`b`,`c` which is equal to `num`"""
    for x in range(0, num):
        for y in range(0, num):
            for z in range(0, num):
                if x * a + y * b + z * c == num:
                    return True
    return False


def max_impossible(number):
    """Return the biggest ~number~ that can't be make a combination of 6, 7, 8
       """
    count = 0
    max_num = 0

    for i in range(number):
        if is_possible(i):
            count += 1
        else:
            count = 0
            max_num = i

        if count == 6:
            return max_num
