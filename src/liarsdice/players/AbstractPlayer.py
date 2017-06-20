'''
Created on Jun 16, 2017

@author: Paul Stone
'''

class AbstractPlayer(object):
    '''
    Abstract Player that chooses what to bid next.
    Must implement get_bid.
    '''

    def __init__(self, player_name):
        '''
        Constructor
        '''
        self.player_name = player_name
    
    def __repr__(self):
        return self.player_name
        
    def starting_new_opponent(self):
        '''
        Inform the player that a new round of games is starting.
        '''
        pass
    
    def starting_new_game(self):
        '''
        Inform the player that a new game is starting.
        '''
        pass
    
    def get_bid(self, hand, opp_num_dice, previous_bid):
        '''
        Get the bid given the player's own list of dice (hand),
        the number of dice the opponent has, and the previous
        bid from the opponent.  The previous_bid will be None
        if we're creating an opening bid right now.
        '''
        raise NotImplementedError("Subclasses should implement this")

    def inform_round_result(self, you_won, your_hand, opp_hand):
        '''
        After a single round of bidding is over, inform the player
        of its hand and the opponent hand.
        '''
        pass
    
    def inform_game_result(self, you_won):
        '''
        After a game is over, the player will be informed of whether it
        won or lost with a boolean.
        '''
        pass

