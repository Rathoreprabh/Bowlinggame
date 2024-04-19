import unittest
import BowlingGame

class BowlingGameTests(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def testAllZeroes(self):
        self.rollMultiple(0, 20)
        self.assertEqual(self.game.score(), 0,)

    def testAllOnes(self):
        
        self.rollMultiple(1, 20)
        self.assertEqual(self.game.score(), 20,)

    def testSingleSpare(self):
        self.game.roll(5)
        self.game.roll(5)  # This completes a spare
        self.game.roll(3)  # Roll after the spare
        self.rollMultiple(0, 17)
        self.assertEqual(self.game.score(), 16,)

    def testSingleStrike(self):
        self.game.roll(10)  # Strike
        self.game.roll(4)
        self.game.roll(3)
        self.rollMultiple(0, 16)
        self.assertEqual(self.game.score(), 24,)

    def testPerfectGame(self):
       
        self.rollMultiple(10, 12)
        self.assertEqual(self.game.score(), 300, )

    def testAllSpares(self):
        
        self.rollMultiple(5, 21)  # 21 rolls for a complete game with all spares
        self.assertEqual(self.game.score(), 150, )

    def rollMultiple(self, pins, rolls):
        
        for _ in range(rolls):
            self.game.roll(pins)

if __name__ == '__main__':
    unittest.main()
