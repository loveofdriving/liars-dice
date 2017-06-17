'''
Created on Jun 16, 2017

@author: Paul Stone
'''
from random import randint
from time import sleep
from liarsdice.Bid import Bid, Challenge
from liarsdice.players.AbstractPlayer import AbstractPlayer

class DumbComputerPlayer(AbstractPlayer):
    '''
    DumbComputerPlayer that chooses what to bid next.
    '''


    def __init__(self, player_name):
        '''
        Constructor
        '''
        super(DumbComputerPlayer, self).__init__(player_name)
    
    def get_bid(self, hand, opp_num_dice, previous_bid):
        
        print("Computer deciding on move...")
        sleep(1)
        # If we're opening the bidding, just pick a random face and quantity
        if not previous_bid:
            return Bid(randint(1, 6), randint(1, 6))
        
        # If we can tell that the opponent's guess is impossible, call him a liar
        if opp_num_dice + hand.count(previous_bid.face) < previous_bid.quantity:
            print("Ha! There can't possibly be that many %ds. Liar!" % previous_bid.face)
            return Challenge()
        
        # Otherwise, just up the quantity by 1 (hey, we said dumb right?)
        return Bid(previous_bid.quantity + 1, previous_bid.face)