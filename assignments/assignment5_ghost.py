import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')

    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())

    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.
    """
    freq = {}

    for x in sequence:
        freq[x] = freq.get(x, 0) + 1

    return freq


wordlist = load_words()


def next_player(player):
    if player == 1:
        return 2
    return 1


def valid_fragment(fragment_str, wordlist):
    """
    Returns True if `fragment_str` is in `wordlist`
    """
    fragment_str_len = len(fragment_str)

    for word in wordlist:
        if word[0:fragment_str_len] == fragment_str:
            if len(word) > fragment_str_len:
                return True


def ghost():
    """
    `ghost` is main function of word game
    """
    fagment = []
    fagment_str = ""
    player = 1

    print('Welcome to ghost\n Player 1 goes first.')
    while True:
        print('Current word fragment: {}'.format(fagment_str))
        turn = input('player {} turn: '.format(player))

        if len(turn) == 1 and turn in string.ascii_letters:
            fagment.append(turn)
            fagment_str = ''.join(fagment)

            if fagment_str in wordlist:
                print("{} is a word".format(fagment_str))
                if len(fagment_str) > 3:
                        print('player ' + str(player) + ' loses')
                        break

            elif not valid_fragment(fagment_str, wordlist):
                print("can't make combination of these fragment")
                print("Player {} loses because no word begins with {}!"
                      .format(player, fagment_str))
                break
        else:
            print('Invalid word try again')
            player = next_player(player)

        player = next_player(player)


if __name__ == '__main__':
    ghost()
