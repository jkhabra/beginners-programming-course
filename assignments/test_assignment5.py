from assignment5 import (get_word_score,
                         display_hand,
                         update_hand,
                         is_valid_word,
                         load_words)

hand1 = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}
hand3 = {'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2}
hand5 = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
hand7 = {'m': 1, 'n': 2, 't': 1, 'o': 1, 's': 3, 'e': 1, 'r': 2}


def test_get_word():
    assert get_word_score('', 7) == 0
    assert get_word_score('it', 7) == 2
    assert get_word_score('was', 7) == 6
    assert get_word_score('scored', 7) == 9
    assert get_word_score('waybill', 7) == 65
    assert get_word_score('outgnaw', 7) == 61
    assert get_word_score('outgnawn', 8) == 62
    assert get_word_score('evil', 7) == 7


def test_display_hand():
    assert display_hand(hand1) == 'aqllmui'
    assert display_hand(hand3) == 'evvnill'
    assert display_hand(hand5) == 'hello'
    assert display_hand(hand7) == 'mnntossserr'


def test_update_hand():
    expected_hand1 = {'l': 1, 'm': 1}
    expected_hand2 = {'a': 0, 'q': 0, 'l': 1, 'm': 1, 'u': 0, 'i': 0}
    expected_hand3 = {'v': 1, 'n': 1, 'l': 1}
    expected_hand4 = {'e': 0, 'v': 1, 'n': 1, 'i': 0, 'l': 1}
    expected_hand5 = {}
    expected_hand6 = {'h': 0, 'e': 0, 'l': 0, 'o': 0}
    expected_hand7 = {'m': 0, 'n': 1, 't': 0, 'o': 0, 's': 2, 'e': 0, 'r': 1}
    expected_hand8 = {'n': 1, 's': 2, 'r': 1}

    assert update_hand(hand1, 'quail') == expected_hand1 or expected_hand2
    assert update_hand(hand3, 'evil') == expected_hand3 or expected_hand4
    assert update_hand(hand5, 'hello') == expected_hand5 or expected_hand6
    assert update_hand(hand7, 'monster') == expected_hand7 or expected_hand8


def test_is_valid_word():
    word_list = load_words()
    hand1 = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}
    hand3 = {'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2}
    hand5 = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    hand7 = {'m': 1, 'n': 2, 't': 1, 'o': 1, 's': 3, 'e': 1, 'r': 2}
    hand9 = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}
    hand10 = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u': 2}
    hand11 = {'d': 1, '0': 1, 'm': 1, 'e': 1}

    assert is_valid_word('hello', hand5, word_list) is True
    assert is_valid_word('hell', hand5, word_list) is True
    assert is_valid_word('rapture', hand9, word_list) is False
    assert is_valid_word('evil', hand3, word_list) is True
    assert is_valid_word('monster', hand7, word_list) is True
    assert is_valid_word('quail', hand1, word_list) is True
    assert is_valid_word('honey', hand10, word_list) is False
    assert is_valid_word('d0me', hand11, word_list) is False
