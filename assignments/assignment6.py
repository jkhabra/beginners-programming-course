import random
import time

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
   }


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters
    Depending on the size of the word list, this function may
    take a while to finish
    """
    print("Loading word list from file..")
    WORDLIST_FILENAME = "words.txt"

    inFile = open(WORDLIST_FILENAME, 'r')
    wordlist = []

    for line in inFile:
        wordlist.append(line.strip().lower())

    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence
    """
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


def get_word_score(word, n=7):
    """
    Returns score for a `word` and score is the sum of the points for
    letters in the `word`, plus 50 points if all `n` letters
    are used on the first go
    """
    score = 0

    for i in word:
        score += SCRABBLE_LETTER_VALUES[i]

    if len(word) == n:
        score += 50

    return score


def display_hand(hand):
    """
    Returns the letters currently in the hand
    """
    letters = ""

    for i in hand.keys():
        for j in range(hand[i]):
            letters += i

    return letters


def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters
    At least n/3 of the letters in the hand should be VOWELS
    """
    hand = {}
    num_vowels = n // 3

    for i in range(num_vowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

        for i in range(num_vowels, n):
            x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
            hand[x] = hand.get(x, 0) + 1

    return hand


def update_hand(hand, word):
    """
    Returns the updated `hand`, that uses the letters in `word`
    """
    for i in word:
        hand[i] -= 1

    return hand


def is_valid_word(word, hand, arrangement_dict):
    """
    Returns True if `word` is in the` word_list` and is entirely
    composed of letters in the `hand` Otherwise, returns False
    """
    h = dict(hand)
    if arrangement_dict.get(word, None):
        for letter in word:
            if h.get(letter, 0) == 0:
                return False
            else:
                h[letter] -= 1
    else:
        return False
    return True


def play_hand(hand, word_list):
    total_scour = 0
    time_limit = float(input('Enter time limit, in seconds, for players: '))

    while True:
        num_letters = 0
        start_time = time.time()

        print("Current Hand: " + display_hand(hand))
        word = pick_best_word_faster(hand, arrangement_dict)
        end_time = time.time()
        total_time = end_time - start_time
        time_limit -= total_time

        for i in hand.keys():
            for j in range(hand[i]):
                num_letters += 1

        if num_letters <= 1:
            print("game over sucker")
            print("Final Score {}".format(total_scour))
            break

        if word == '.':
            print('It took {} seconds to provide an answer'.format(total_time))
            print("Final Score is {}".format(total_scour))
            break

        print("remaining time is {}".format(time_limit))

        if time_limit < 0:
            print('Time is over! try again')
            break

        if is_valid_word(word, hand, arrangement_dict):
            score = get_word_score(word, num_letters)
            update_hand(hand, word)
            total_scour += score
            print('It took {} seconds to provide an answer'.format(total_time))
            print("{} earned: {} points. Total Score: {} points"
                  .format(word, score, total_scour))
        else:
            print('It took {} seconds to provide an answer'.format(total_time))
            print("Invalid word, try again", word)

    else:
        print("Final Score {}".format(total_scour))


def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands
    """
    # TO DO ...

    hand = deal_hand(HAND_SIZE)  # random init

    while True:
        cmd = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')

        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), word_list)
            print()

        elif cmd == 'r':
            play_hand(hand.copy(), word_list)
            print()

        elif cmd == 'e':
            break

        else:
            print("Invalid command.")


def get_words_to_points(word_list):
    """
    Return a dict that maps every word in `word_list` to its point value
    """
    points_dict = {}

    for i in word_list:
        points_dict[i] = get_word_score(i)

    return points_dict


def get_time_limit(points_dict, k):
    """
    Return the time limit for the computer player as a function of the
    multiplier k.
    points_dict should be the same dictionary that is created by
    get_words_to_points.
    """
    start_time = time.time()
    # Do some computation. The only purpose of the computation is so we can
    # figure out how long your computer takes to perform a known task.
    for word in points_dict:
        get_frequency_dict(word)
        get_word_score(word, HAND_SIZE)

    end_time = time.time()
    return (end_time - start_time) * k


def get_combination(hand_str, string):
    """
    Returns all possible combination of `hand_str` from `string`
    """
    for i in hand_str:
        if string.find(i) != -1:
            string = string.replace(i, '', 1)

    if len(string) == 0:
                return True
    return False


def pick_best_word(hand, points_dict):
    """
    Return the highest scoring word from points_dict that can be made with the
    hand & Return '.' if no words can be made with the given hand
    """
    hand_str = display_hand(hand)
    valid_words = {}

    for i in points_dict.keys():
        if get_combination(hand_str, i):
            valid_words[i] = get_word_score(i)
    if valid_words == {}:
        return "."
    return max(valid_words, key=valid_words.get)


def pick_best_word_faster(hand, arrangements_dict):
    """
    Return the highest scoring word from `arrangements_dict` that can be made with the
    hand & Return '.' if no words can be made with the given hand
    """
    hand_str = display_hand(hand)
    valid_words = {}

    for i in arrangements_dict.keys():
        if get_combination(hand_str, i):
            valid_words[i] = get_word_score(i)
    if valid_words == {}:
        return "."
    return max(valid_words, key=valid_words.get)


def get_word_rearrangements(word_list):
    """
    Return highest scoring words faster than pick_best_word
    """
    arrangements_dict = {}

    for w in word_list:
        arrangements_dict[''.join(sorted(w))] = w

    return arrangements_dict


if __name__ == '__main__':
    hand1 = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}
    word_list = load_words()
    points_dict = get_words_to_points(word_list)
    arrangement_dict = get_word_rearrangements(word_list)
    comp_time_limit = get_time_limit(points_dict, 1)

    play_hand(hand1, word_list)
