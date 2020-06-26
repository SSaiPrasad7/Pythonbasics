import sys

from TicTacToe.GameRules import GameRules
from TicTacToe.Screen import Screen, board
from TicTacToe.UserDetails import UserDetails
from TicTacToe.UserPosition import UserPosition

while 1:
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
            player1 = UserPosition().setPosition_1(players_list)
            player1_won = GameRules().winCondition(player1, players_list)
            if player1_won == True:
                break
            player2 = UserPosition().setPosition_2(players_list)
            player2_won = GameRules().winCondition(player2, players_list)
            if player2_won == True:
                break
    else:
        sys.exit("Thank you")
