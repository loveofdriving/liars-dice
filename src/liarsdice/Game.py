'''
Created on Jun 16, 2017

@author: Paul Stone
'''
from random import randint, getrandbits
from time import sleep
from liarsdice.players.HumanPlayer import HumanPlayer
from liarsdice.players.DumbComputerPlayer import DumbComputerPlayer
from liarsdice.Bid import Challenge

def roll_dice(num_dice):
    ''' Get list of random numbers between 1 and 6, of the size given '''
    dice = []
    for _ in range(num_dice):
        # Get a random dice roll and add it to the list
        dice.append(randint(1, 6))
    return dice

def run_round(player_1, player_2, p1_num_dice, p2_num_dice, p1_goes_first):
    '''
    Get random hands for each player and run a round of bids until a challenge is given.
    Return True if player 1 wins the round.  Return False if player 2 winds the round.
    '''
    print("Rolling dice...")
    sleep(1)
    
    # Get player 1's roll
    p1_hand = roll_dice(p1_num_dice)
    print(p1_hand)
    
    # Get player 2's roll
    p2_hand = roll_dice(p2_num_dice)
    print(p2_hand)
    
    # No bid yet
    previous_bid = None
    
    # Start with player 1?
    turn_player_1 = p1_goes_first
    
    # Loop until someone challenges a bid
    while True:
        # Whoever's turn it is, get their bid
        if turn_player_1:
            bid = player_1.get_bid(p1_hand, len(p2_hand), previous_bid)
            print(player_1, "bids", bid)
            # If the bid is invalid, p1 loses round
            if bid == None or not bid.is_valid(previous_bid):
                print("Invalid bid. %s loses round." % player_1)
                return False
        else:
            bid = player_2.get_bid(p2_hand, len(p1_hand), previous_bid)
            print(player_2, "bids", bid)
            # If the bid is invalid, p2 loses round
            if bid == None or not bid.is_valid(previous_bid):
                print("Invalid bid. %s loses round." % player_2)
                return True
        
        # Check if this was a challenge on a previous bid
        if isinstance(bid, Challenge):
            break
        
        # Save off the new bid
        previous_bid = bid
        
        # Switch whose turn it is
        turn_player_1 = not turn_player_1
        
        # Loop to the next turn
        print()
        
    # Handle the challenge - first step is evaluating the bid
    print("Handling the challenge of bid %s..." % previous_bid)
    print(p1_hand)
    print(p2_hand)
    
    # Count how many of the bid's face there are
    total = p1_hand.count(previous_bid.face) + p2_hand.count(previous_bid.face)
    print("There are %d total %ss" % (total, previous_bid.face))
    
    # Check if there are fewer of that face than the bid
    if total < previous_bid.quantity:
        # The bid was too high, so the challenger wins. If it was player 1
        # doing the challenging, return True. If it was player 2 doing
        # the challenging, return False
        print("The bid was too high. The challenger wins the round!")
        return turn_player_1
    else:
        # The bid was a good one, so the challenger loses. If it was 
        # player 1 doing the challenging, return False.
        print("The bid was good. The challenger loses the round!")
        return not turn_player_1
    
if __name__ == '__main__':
    
    # Instantiate each player
    player_1 = HumanPlayer("HumanPlayer 1")
    player_2 = DumbComputerPlayer("ComputerPlayer 2")
    
    # each player starts with 5 dice
    p1_num_dice = 5
    p2_num_dice = 5
    
    # choose a random side to go first
    p1_turn = bool(getrandbits(1))
    
    # Loop until someone runs out of dice
    while p1_num_dice > 0 and p2_num_dice > 0:
    
        if run_round(player_1, player_2, p1_num_dice, p2_num_dice, p1_turn):
            # player 1 win, p2 loses a dice
            p2_num_dice -= 1
            p1_turn = False
        else:
            # player 2 win, p1 loses a dice
            p1_num_dice -= 1
            p1_turn = True
        
        print()
        
    else:
        if p1_num_dice == 0:
            print("%s wins!" % player_2)
        elif p2_num_dice == 0:
            print("%s wins!" % player_1)