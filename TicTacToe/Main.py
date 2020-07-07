'''
#Implementation of Two Player Tic-Tac-Toe game in Python.
'''

from Pythonbasics.TicTacToe.GameRules import GameRules
from Pythonbasics.TicTacToe.Screen import Screen
from Pythonbasics.TicTacToe.UserDetails import UserDetails
from Pythonbasics.TicTacToe.UserPosition import UserPosition


# from Pythonbasics.TicTacToe.Helper import Helper
# import json


#  This is  main which has all the Game play functionality.
# Read the config.json in to say config attribute
# config = Helper().readConfig("config.json")
# Now we will ask if player wants to start the game or not
# config["messages"]["wantToPlay"]

class Main:

    def startGame(self,option):
        if option == "Y":  # config.gameCtrls.acceptPlay:
            players_list = UserDetails().playerDetails()
            Screen().boardIntialize()
            Screen().outputDisplay()
            game_output=Main().gamePlay(players_list)
            return game_output
        else:
            print('Thank you for playing!!!')
            return False

    def gamePlay(self, players_list):
        player1_won = False
        player2_won = False
        while player1_won == False or player2_won == False:
            player1 = UserPosition().set_position_1(players_list)
            player1_won = GameRules().gameConditions(player1, players_list)
            if player1_won == True:
                return player1_won
            player2 = UserPosition().set_position_2(players_list)
            player2_won = GameRules().gameConditions(player2, players_list)
            if player2_won == True:
                return player2_won


if __name__ == "__main__":
    option_yn = UserDetails().wantToPlay()
    if Main().startGame(option_yn) == True:
        option_yn = UserDetails().wantToPlay()
        Main().startGame(option_yn)
