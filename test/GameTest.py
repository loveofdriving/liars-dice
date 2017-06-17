'''
Created on Jun 16, 2017

@author: Paul Stone
'''
import unittest
from liarsdice import Game

class Test(unittest.TestCase):

    def testRollDice(self):
        
        # Test a single die
        hand = Game.roll_dice(1)
        self.assertEquals(1, len(hand))
        self.assertIn(hand[0], range(1,7))
        
        # Test 10 dice
        hand = Game.roll_dice(10)
        self.assertEquals(10, len(hand))
        for die in hand:
            self.assertIn(die, range(1,7))


if __name__ == "__main__":
    unittest.main()