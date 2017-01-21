import random

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
    # with open('words.txt', 'r') as f:
    #  inFile = f.read()
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


def is_valid_word(word, hand, word_list):
    """
    Returns True if `word` is in the` word_list` and is entirely
    composed of letters in the `hand` Otherwise, returns False
    """
    h = dict(hand)
    if word.lower() in word_list:
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

    while True:
        num_letters = 0
        print("Current Hand: " + display_hand(hand))
        word = input("Enter word, or a . to indicate that you are finished: ")

        for i in hand.keys():
            for j in range(hand[i]):
                num_letters += 1

        if num_letters < 2:
            print("game over sucker")
            print("Final Score {}".format(total_scour))
            break

        if word == '.':
            print("Final Score is {}".format(total_scour))
            break

        if is_valid_word(word, hand, word_list):
            score = get_word_score(word, num_letters)
            update_hand(hand, word)
            total_scour += score
            print("{} earned: {} points. Total Score: {} points".format(word, score, total_scour))
        else:
            print("Invalid word, try again")

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
