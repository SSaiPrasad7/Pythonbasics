import unittest
from Pythonbasics.TicTacToe.Main import Main
from Pythonbasics.TicTacToe.Screen import Screen
from Pythonbasics.TicTacToe.UserDetails import UserDetails


class MainTest(unittest.TestCase):
    def test_start_game(self):
        test_option=Main().startGame('N')
        self.assertEqual(False,test_option)
    def test_game_play(self):
        players_list=UserDetails().playerDetails()
        Screen().boardIntialize()
        winner=Main().gamePlay(players_list)
        self.assertEqual(True,winner)