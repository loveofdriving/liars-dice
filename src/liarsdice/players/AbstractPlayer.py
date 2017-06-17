'''
Created on Jun 16, 2017

@author: Paul Stone
'''

class AbstractPlayer(object):
    '''
    Abstract Player that chooses what to bid next.
    '''


    def __init__(self, player_name):
        '''
        Constructor
        '''
        self.player_name = player_name
    
    def __repr__(self):
        return self.player_name
        
    def get_bid(self, hand, opp_num_dice, previous_bid):
        '''
        Get the bid given the player's own list of dice (hand),
        the number of dice the opponent has, and the previous
        bid from the opponent.  The previous_bid will be None
        if we're creating an opening bid right now.
        '''
        raise NotImplementedError("Subclasses should implement this")
