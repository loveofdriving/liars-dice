'''
Created on Jun 16, 2017

@author: Paul Stone
'''
import unittest
from liarsdice.Bid import Bid

class Test(unittest.TestCase):

    def testInit(self):
        bid = Bid(2, 3)
        self.assertEqual(2, bid.quantity)
        self.assertEqual(3, bid.face)
        self.assertEqual("two threes", str(bid))
        
        bid = Bid(1, 6)
        self.assertEqual(1, bid.quantity)
        self.assertEqual(6, bid.face)
        self.assertEqual("one six", str(bid))
        
    def testInit_LowQuantity(self):
        with self.assertRaises(ValueError):
            Bid(0, 1)
    
    def testInit_LowFace(self):
        with self.assertRaises(ValueError):
            Bid(1, 0)
    
    def testInit_HighFace(self):
        with self.assertRaises(ValueError):
            Bid(1, 7)

    def testIsValid(self):
        
        # Decrease face, decrease quantity - from 2 3s, bid 1 2
        self.assertFalse(Bid(1, 2).is_valid(Bid(2, 3)))
        
        # Decrease face, same quantity - from 2 3s, bid 1 3
        self.assertFalse(Bid(1, 3).is_valid(Bid(2, 3)))
        
        # Decrease face, increase quantity - from 2 3s, bid 3 1s
        self.assertTrue(Bid(3, 1).is_valid(Bid(2, 3)))

        # Same face, decrease quantity - from 2 3s, bid 1 3
        self.assertFalse(Bid(1, 3).is_valid(Bid(2, 3)))
        
        # Same face, same quantity - from 2 3s, bid 2 3s
        self.assertFalse(Bid(2, 3).is_valid(Bid(2, 3)))
        
        # Same face, increase quantity - from 1 3s, bid 2 3s
        self.assertTrue(Bid(2, 3).is_valid(Bid(1, 3)))

        # Increase face, decrease quantity - from 2 4s, bid 1 5
        self.assertFalse(Bid(1, 5).is_valid(Bid(2, 4)))

        # Increase face, same quantity - from 2 4s, bid 2 5s
        self.assertTrue(Bid(2, 5).is_valid(Bid(2, 4)))

        # Increase face, increase quantity - from 2 3s, bid 3 4s
        self.assertTrue(Bid(3, 4).is_valid(Bid(2, 3)))


if __name__ == "__main__":
    unittest.main()