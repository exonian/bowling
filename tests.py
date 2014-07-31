import unittest

from score import Game

class SetsBalls(unittest.TestCase):

    def testNoArg(self):
        game = Game()
        self.failUnless(game.balls=='')

    def testEmptyArg(self):
        game = Game('')
        self.failUnless(game.balls=='')

    def testStringProvided(self):
        balls = '13283332'
        game = Game(balls)
        self.failUnless(game.balls==balls)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
