from assignment3 import (countSubStringMatch,
                         countSubStringMatchRecursive,
                         subStringMatchExact,
                         constrainedMatchPair,
                         getAllCombinations,
                         subStringMatchExactlyOneSub)

target1 = "foobarfoobarbarfoo"
target2 = "barfoomesaquencbar"
target3 = "foofoofoofoo"

key = "bar"


def has_same_items(col1, col2):
    for i in col1:
        assert i in col2
    for i in col2:
        assert i in col1


def test_countSubStringMatch():
    assert countSubStringMatch(target1, key) == 3
    assert countSubStringMatch(target2, key) == 2
    assert countSubStringMatch(target3, key) == 0


def test_countSubStringMatchRecursive():
    assert countSubStringMatchRecursive(target1, key) == 3
    assert countSubStringMatchRecursive(target2, key) == 2
    assert countSubStringMatchRecursive(target3, key) == 0


def test_subStringMatchExact():
    assert subStringMatchExact(target1, key) == (3, 9, 12)
    assert subStringMatchExact(target2, key) == (0, 15)
    assert subStringMatchExact(target3, key) == ()
    assert subStringMatchExact(target3, "") == (0, 1, 2, 3, 4, 5, 6,
                                                7, 8, 9, 10, 11)


def test_constrainedMatchPair():
    target1 = "foobarfooburborfootbooostr"
    target2 = "barfoomefsoafquoefnocbar"
    target3 = "atgacatgcacaagtatgcat"

    assert constrainedMatchPair((3, 9, 12, 19),
                                (5, 11, 14, 25), 1) == (3, 9, 12)

    assert constrainedMatchPair((3, 8, 12, 17),
                                (4, 5, 10, 15, 19), 1) == (3, 8, 17)

    assert constrainedMatchPair((0, 5, 15),
                                (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                                 14, 15, 16, 17, 18, 19, 20), 3) == (0, 5, 15)


def test_getAllCombinations():
    has_same_items(getAllCombinations("nbat"), [("nba", ""), ("nb", "t"),
                                                ("n", "at"), ("", "bat")])

    has_same_items(getAllCombinations("tom"), [("to", ""), ("t", "m"),
                                               ("", "om")])

    has_same_items(getAllCombinations("xyzi"), [("xyz", ""), ("xy", "i"),
                                                ("x", "zi"), ("", "yzi")])

    has_same_items(getAllCombinations("hope"), [("hop", ""), ("ho", "e"),
                                                ("h", "pe"), ("", "ope")])


def test_subStringMatchExactlyOneSub():
    target1 = "foobarfoobazborfoo"
    key1 = "bar"

    target2 = "barfoomefossaqufsoencbar"
    key2 = "foo"

    target3 = "abcdefgabddghaccd"
    key3 = "abcd"

    has_same_items(subStringMatchExactlyOneSub(target1, key1), (9, 12))
    has_same_items(subStringMatchExactlyOneSub(target2, key2), (8, 15))
    has_same_items(subStringMatchExactlyOneSub(target3, key3), (7, 13))
