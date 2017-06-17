'''
Created on Jun 16, 2017

@author: Paul Stone
'''
from liarsdice.Bid import Bid, Challenge
from liarsdice.players.AbstractPlayer import AbstractPlayer

class HumanPlayer(AbstractPlayer):
    '''
    HumanPlayer that chooses what to bid next.
    '''


    def __init__(self, player_name):
        '''
        Constructor
        '''
        super(HumanPlayer, self).__init__(player_name)
    
    def get_bid(self, hand, opp_num_dice, previous_bid):
        '''
        Get the bid given the player's own list of dice (hand),
        the number of dice the opponent has, and the previous
        bid from the opponent.  The previous_bid will be None
        if we're creating an opening bid right now.
        '''
        
        print("Your hand:", hand)
        print("Opponent has", opp_num_dice, "dice.")
        print("Opponent's previous bid was", previous_bid)
        
        bid_str = input(str(self) + " bid: ")
        if not bid_str:
            return None
        elif bid_str.upper() == "C":
            return Challenge()
        elif len(bid_str) == 3:
            return Bid(int(bid_str[0]), int(bid_str[2]))
        elif len(bid_str) == 4:
            return Bid(int(bid_str[0:2]), int(bid_str[3]))
        else:
            return None