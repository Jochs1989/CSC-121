
# This will allow you to play rock, paper, scissors with 2 files
# 02/17/202
# CSC121- M2Pro Code Modularizing
# Jeffrey Ochs


import jeffreyochs_game_functions as fn

# Global constants
COMPUTER_WINS = 1
PLAYER_WINS = 2
TIE = 0
INVALID = 3

# main function
def main():

    # Local Variable
    CHOICE = input("Would you like to play rock, paper," \
                   " scissors?  (yes/no) > ")
    
    while CHOICE != "no":
        
        if CHOICE == "yes":
            result = fn.getPlayerAndRandomResults()
            if result == TIE:
                print('You made the same choice as ' \
                      'the computer. Starting over')
                result = fn.getPlayerAndRandomResults()
            elif (result == COMPUTER_WINS):
                print ('The computer wins the game')
            elif result == PLAYER_WINS:
                print ('You win the game')
            else:
                print ('You made an invalid choice. No winner')
            CHOICE = input("Would you like to play again? (enter yes/no) > ")
        else:
            CHOICE = input("Invalid input. Please enter (yes/no): > ")
            
    print("Thank you for playing! Goodbye!")



# Call the main function.
if __name__ == "__main__":
    main()



