'''
Created on Jun 16, 2017

@author: Paul Stone
'''
from random import randint, getrandbits
from copy import deepcopy
from liarsdice.players.HumanPlayer import HumanPlayer
from liarsdice.players.DumbComputerPlayer import DumbComputerPlayer
from liarsdice.Bid import Challenge

NUMBER_OF_GAMES = 2
PLAYER_1_CLASS = HumanPlayer
PLAYER_2_CLASS = DumbComputerPlayer

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
    
    # Get player 1's roll
    p1_hand = roll_dice(p1_num_dice)
    # print(p1_hand)
    
    # Get player 2's roll
    p2_hand = roll_dice(p2_num_dice)
    # print(p2_hand)
    
    # No bid yet
    previous_bid = None
    
    # Start with player 1?
    turn_player_1 = p1_goes_first
    
    # Loop until someone challenges a bid
    while True:
        # Whoever's turn it is, get their bid
        if turn_player_1:
            # Pass in a copy of the bid so that the player can't edit the original
            bid = player_1.get_bid(p1_hand, len(p2_hand), deepcopy(previous_bid))
            print(player_1, "bids", bid)
            # If the bid is invalid, p1 loses round
            if bid == None or not bid.is_valid(previous_bid):
                print("Invalid bid. %s loses round." % player_1)
                return False
        else:
            # Pass in a copy of the bid so that the player can't edit the original
            bid = player_2.get_bid(p2_hand, len(p1_hand), deepcopy(previous_bid))
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
        player_1.inform_round_result(turn_player_1, p1_hand, p2_hand)
        player_2.inform_round_result(not turn_player_1, p2_hand, p1_hand)
        return turn_player_1
    else:
        # The bid was a good one, so the challenger loses. If it was 
        # player 1 doing the challenging, return False.
        print("The bid was good. The challenger loses the round!")
        player_1.inform_round_result(not turn_player_1, p1_hand, p2_hand)
        player_2.inform_round_result(turn_player_1, p2_hand, p1_hand)
        return not turn_player_1

def run_game(player_1, player_2):
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
            return False
        elif p2_num_dice == 0:
            print("%s wins!" % player_1)
            return True

if __name__ == '__main__':
    
    # Instantiate each player
    player_1 = PLAYER_1_CLASS("Player 1")
    player_2 = PLAYER_2_CLASS("Player 2")
    
    p1_win_count = 0
    p2_win_count = 0
    
    # Inform the players that a new opponent is starting
    player_1.starting_new_opponent()
    player_2.starting_new_opponent()
    
    for game_num in range(NUMBER_OF_GAMES):
    
        print("Running game number %d" % (game_num + 1))
        
        # Inform the players that a new game is starting
        player_1.starting_new_game()
        player_2.starting_new_game()
        
        # Run the game
        p1_is_winner = run_game(player_1, player_2)
        
        # Tell each side whether they won or lost
        player_1.inform_game_result(p1_is_winner)
        player_2.inform_game_result(not p1_is_winner)
        
        # Increment the win count
        if p1_is_winner:
            p1_win_count += 1
        else:
            p2_win_count += 1
            
    print("Final win totals:")
    print("%s: %d" % (player_1, p1_win_count))
    print("%s: %d" % (player_2, p2_win_count))
