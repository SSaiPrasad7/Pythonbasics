'''
#Implementation of Two Player Tic-Tac-Toe game in Python.
'''
import sys

from Pythonbasics.TicTacToe.GameRules import GameRules
from Pythonbasics.TicTacToe.Screen import board, Screen
from Pythonbasics.TicTacToe.UserDetails import UserDetails
from Pythonbasics.TicTacToe.UserPosition import UserPosition

#  This is  main which has all the Game play functionality.
if __name__ == "__main__":
    while 1:
        # Now we will ask if player wants to start the game or not
        print("Do you want to play the game??")
        option_yn = UserDetails().wantToPlay()
        if option_yn == "Y":
            print("Welcome to Tic Tac Toe Game")
            players_list = UserDetails().playerDetails()
            print("Players list with icons respectively:", players_list)
            original_board = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            board.extend(original_board)
            Screen().outputDislay()
            player1_won = False
            player2_won = False
            while player1_won == False or player2_won == False:
                player1 = UserPosition().set_position_1(players_list)
                player1_won = GameRules().gameConditions(player1, players_list)
                if player1_won == True:
                    break
                player2 = UserPosition().set_position_2(players_list)
                player2_won = GameRules().gameConditions(player2, players_list)
                if player2_won == True:
                    break
        else:
            sys.exit("Thank you for playing!!!")
