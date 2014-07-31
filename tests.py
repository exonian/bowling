import unittest

from score import Game, InvalidFrame


class SetsBalls(unittest.TestCase):

    def testNoArg(self):
        game = Game()
        self.assertEqual(game.balls, '')

    def testEmptyArg(self):
        game = Game('')
        self.assertEqual(game.balls, '')

    def testStringProvided(self):
        balls = '13283332'
        game = Game(balls)
        self.assertEqual(game.balls, balls)


class MakesBallsArray(unittest.TestCase):

    def testBallsArrayLength(self):
        balls = '45397X93'
        game = Game(balls)
        ba = game._make_balls_array()
        self.assertEqual(len(ba), len(balls))

    def testBallsArrayValues(self):
        balls = '3200715'
        game = Game(balls)
        ba = game._make_balls_array()
        self.assertEqual(ba, [3,2,0,0,7,1,5])

    def testCatchesBadValues(self):
        balls = 'O3200715'
        game = Game(balls)
        self.assertRaises(ValueError, game._make_balls_array)


class CatchesBadFramesArray(unittest.TestCase):

    def testStrikeAsSecondBall(self):
        game = Game('343X3')
        self.assertRaises(InvalidFrame, game.calculate_score)

    def testTwoBallsOverTen(self):
        game = Game('3547')
        self.assertRaises(InvalidFrame, game.calculate_score)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
