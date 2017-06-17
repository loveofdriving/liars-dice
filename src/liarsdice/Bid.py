'''
Created on Jun 16, 2017

@author: Paul Stone
'''

_ENGLISH_NUMBERS = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten"}
_ENGLISH_PLURALS = {1:"ones", 2:"twos", 3:"threes", 4:"fours", 5:"fives", 6:"sixes"}

class Challenge(object):
    def is_valid(self, previous_bid):
        return previous_bid != None
    def __repr__(self):
        return "Liar!"
    
    def __eq__(self, other):
        ''' Always consider two Challenges to be equals ''' 
        if isinstance(other, self.__class__):
            return True
        return NotImplemented
    
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented
    
    def __hash__(self):
        ''' Since all Challenges are equal, return a constant hash code for all instances '''
        return 1

class Bid(object):
    '''
    A guess consisting of a quantity and the face of the die.
    '''

    def __init__(self, quantity, face):
        
        # Make sure the quantity is positive
        if quantity < 1:
            raise ValueError("Quantity must be positive")
        
        # Make sure face is a valid die face
        if face < 1 or face > 6:
            raise ValueError("Die face must be between 1 and 6, inclusive.")
        
        self.quantity = quantity
        self.face = face
    
    def is_valid(self, previous_bid):
        """
        See if this bid is valid given some previous bid.
        A new bid is valid if any of the following is true:
        - This is the opening bid (previous_bid is None)
        - The quantity is greater than the previous bid, regardless of the face
        - The face is higher than the previous bid and the quantity is the same or greater
        """
        if previous_bid == None:
            return True
        elif self.quantity > previous_bid.quantity:
            return True
        elif self.face > previous_bid.face and self.quantity >= previous_bid.quantity:
            return True
        else:
            return False

    def __repr__(self):
        return "%s %s" % (_ENGLISH_NUMBERS.get(self.quantity, self.quantity), str(_ENGLISH_NUMBERS[self.face] if self.quantity == 1 else _ENGLISH_PLURALS[self.face]))

    def __eq__(self, other):
        ''' Two bids are equal if they have the same quantity and face ''' 
        if isinstance(other, self.__class__):
            return self.quantity == other.quantity and self.face == other.face
        return NotImplemented
    
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented
    
    def __hash__(self):
        return hash((self.face, self.quantity))
