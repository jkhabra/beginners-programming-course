# import assignment10; reload(assignment10)
from assignment10 import Hand, Player, ComputerPlayer, Wordlist, getWordScore


class TestHand():

    def setup(self):
        self.h1 = Hand(10, {'o': 1, 'm': 1, 't': 1, 'e': 1, 'r': 1,
                            'n': 1, 's': 1})
        self.h2 = Hand(7, {'c': 1, 'e': 2, 'p': 1, 'r': 1, 'y': 1})
        self.h3 = Hand(0, {'p': 0, 'i': 0, 'n': 0, 'a': 0})

    # def test_update(self):
        # assert self.h1.update('no') == 'mters'
       # assert self.h2.update('pee') == 'cry'

    def test_containsLetters(self):
        assert self.h1.containsLetters('mestr') is True
        assert self.h2.containsLetters('creep') is True
        assert self.h2.containsLetters('crap') is False
        assert self.h2.containsLetters('crow') is False

    def test_isEmpty(self):
        assert self.h1.isEmpty() is False
        assert self.h2.isEmpty() is False
        assert self.h3.isEmpty() is True

    def test_eq(self):
        assert self.h1.__eq__({'e': 1, 'm': 1, 'n': 1, 'o': 1, 'r': 1, 's': 1,
                               't': 1}) is True
        assert self.h2.__eq__({'c': 1, 'e': 2, 'p': 1, 'r': 1}) is False
        assert self.h2.__eq__({'c': 1, 'e': 2, 'p': 1, 'r': 1, 'y': 2}) is False

    def test_str(self):
        assert self.h1.__str__() == 'omterns'
        assert self.h2.__str__() == 'ceepry'


class TestPlayer():

    def setup(self):
        self.h1 = Player(1, {'o': 1, 'm': 1, 't': 1, 'e': 1, 'r': 1,
                             'n': 1, 's': 1})
        self.h2 = Player(2, {'c': 1, 'e': 2, 'p': 1, 'r': 1, 'y': 1})

    def test_getHand(self):
        assert self.h1.getHand() == 'omterns'
        assert self.h2.getHand() == 'ceepry'

    # def test_addPoints(self):
      #  assert self.h1.addPoints(9) == 9
      # assert self.h1.addPoints(2) == 11

    def test_getPoints(self):
        self.h2.addPoints(9)
        assert self.h1.getPoints() == 0
        assert self.h2.getPoints() == 9

    def test_getIdNum(self):
        assert self.h1.getIdNum() == 1
        assert self.h2.getIdNum() == 2

    def test_cmp(self):
        self.h1.addPoints(8)
        assert self.h2.__cmp__(3) == -1
        assert self.h1.__cmp__(7) == 1
        assert self.h1.__cmp__(8) == 0

    def test_str_(self):
        self.h1.addPoints(9)
        assert self.h1.__str__() == 'Player 1\n\n Score: 9.0\n'
        assert self.h2.__str__() == 'Player 2\n\n Score: 0.0\n'


def isClose(float1, float2):
    """
    Helper function - are two floating point values close?
    """
    return abs(float1 - float2) < .01


def testResult(boolean):
    """
    Helper function - print 'Test Failed' if boolean is false, 'Test
    Succeeded' otherwise.
    """
    if boolean:
        print('Test Succeeded')
    else:

        print('Test Failed')


def testHand():
    """
    Test the hand class. Add your own test cases
    """
    h = Hand(8, {'a':3, 'b':2, 'd':3})
    h.update('bad')
    testResult(h.containsLetters('aabdd') and not h.isEmpty())
    h.update('dad')
    testResult(h.containsLetters('ab') or not h.isEmpty())
    h.update('ab')
    testResult(h.isEmpty())


def testPlayer():
    """
    Test the Player class. Add your own test cases.
    """
    p = Player(1, Hand(6, {'c':1, 'a':1, 'b':1 ,'d':1, 'o':1, 'e':1}))
    testResult(type(p.getHand()) == Hand)
    p.addPoints(5.)
    p.addPoints(12.)
    testResult(isClose(p.getPoints(), 17))


def testComputerPlayer():
    """
    Test the ComputerPlayer class. Add your own test cases.
    """
    wordlist = Wordlist()
    p = ComputerPlayer(1, Hand(6, {'c':1, 'a':1, 'b':1 ,'d':1, 'o':1, 'e':1}))
    testResult(getWordScore(p.pickBestWord(wordlist)) == getWordScore('abode'))


def testAll():
    """
    Run all Tests
    """

    print("Uncomment the tests in this file as you complete each problem.")
    print('PROBLEM 2 -----------------------------------------')
    testHand()

    print('PROBLEM 3 -----------------------------------------')
    testPlayer()

    print('PROBLEM 4 -----------------------------------------')
    testComputerPlayer()


testAll()
