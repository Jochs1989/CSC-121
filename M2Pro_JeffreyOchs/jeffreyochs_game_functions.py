# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 13:11:16 2020

@author: ochsj6181
"""

# This will allow you to play rock, paper, scissors with 2 files
# 02/17/202
# CSC121- M2Pro Code Modularizing
# Jeffrey Ochs

import random

# Global constants
COMPUTER_WINS = 1
PLAYER_WINS = 2
TIE = 0
INVALID = 3
ROCK = 1
PAPER = 2
SCISSORS = 3

def getPlayerAndRandomResults():
    # Get computer number
    computer = random.randint(1, 3)

    # Get player number
    player = int(input('Enter 1 for rock, ' \
                       '2 for paper, 3 for scissors: '))

    print ('Computer chose', choiceString(computer))
    print ('You chose', choiceString(player))
        
    result = rockPaperScissors(computer, player)
    
    return result

# The rockPaperScissors function receives numbers representing the
# computer and player's choices.
# It returns 0 if there is a tie, 1 if the computer won, 2 if the 
# player won, or 3 if the player made an invalid choice.
def rockPaperScissors(computer, player):

    if(computer == player):
        return TIE
    
    if computer == ROCK: 
        if player == PAPER: 
            return PLAYER_WINS
        elif player == SCISSORS: 
            return COMPUTER_WINS
        else:
            return INVALID
    elif computer == PAPER: 
        if player == ROCK: 
            return COMPUTER_WINS
        elif player == SCISSORS: 
            return PLAYER_WINS
        else:
            return INVALID
    else: #computer chose scissors
        if player == ROCK: 
            return PLAYER_WINS
        elif player == PAPER: 
            return COMPUTER_WINS
        else:
            return INVALID
            
# The choiceString function displays a choice in string format
def choiceString(choice):
    if choice == ROCK:
        return 'rock'
    elif choice == PAPER:
        return 'paper'
    elif choice == SCISSORS:
        return 'scissors'
    else:
        return 'something went wrong'