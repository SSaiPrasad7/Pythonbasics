from Pythonbasics.TicTacToe.UserDetails import UserDetails
from Pythonbasics.TicTacToe.UserPosition import UserPosition
from Pythonbasics.TicTacToe.Screen import Screen
import unittest


class UserDetailsTest(unittest.TestCase):
    def test_get_position(self):
        Screen().boardIntialize()
        new_position=UserPosition().getPostion("sai",['*','!'])
        self.assertEqual(int,type(new_position))
    def test_set_position1(self):
        player_list=UserDetails().playerDetails()
        players=list(player_list.keys())
        player1=UserPosition().set_position_1(player_list)
        self.assertEqual(players[0],player1)

    def test_set_position2(self):
        player_list = UserDetails().playerDetails()
        players=list(player_list.keys())
        player2=UserPosition().set_position_2(player_list)
        self.assertEqual(players[1],player2)