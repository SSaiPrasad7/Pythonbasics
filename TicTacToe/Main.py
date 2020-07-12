'''
#Implementation of Two Player Tic-Tac-Toe game in Python.
'''

from Pythonbasics.TicTacToe.GameRules import GameRules
from Pythonbasics.TicTacToe.Screen import Screen, config
from Pythonbasics.TicTacToe.UserDetails import UserDetails
from Pythonbasics.TicTacToe.UserPosition import UserPosition


class Main:
    def play(self):
        # Now we will ask if player wants to start the game or not
        option_yn = UserDetails().wantToPlay()
        if Main().startGame(option_yn) == True:
            Main().play()
    def startGame(self, option):
        if option == config["gameControls"]["acceptPlay"]:
            players_list = UserDetails().playerDetails()
            Screen().boardIntialize()
            Screen().outputDisplay()
            game_output = Main().gamePlay(players_list)
            return game_output
        else:
            print(config["endGame"]["message"])
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


#  This is  main which has all the Game play functionality.
if __name__ == "__main__":
    Main().play()
