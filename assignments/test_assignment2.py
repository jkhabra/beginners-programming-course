from assignment2 import is_possible, max_impossible


def test_is_possible():
    assert is_possible(50) is True
    assert is_possible(75, 7, 9, 19) is True
    assert is_possible(43) is False
    assert is_possible(5) is False
    assert is_possible(935759) is True
    assert is_possible(60, 5, 8, 15) is True
    assert is_possible(8900, 10, 15, 20) is True


def test_max_impossible():
    assert max_impossible() == 43
    assert max_impossible(10, 15, 22) == 83
    assert max_impossible(20, 1, 30) == 19
    assert max_impossible(25, 15, 11) == 57
