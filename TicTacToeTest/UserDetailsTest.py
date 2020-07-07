from Pythonbasics.TicTacToe.UserDetails import UserDetails
import unittest


class UserDetailsTest(unittest.TestCase):
    def test_want_to_play(self):
        test_choice = UserDetails().wantToPlay()
        self.assertEqual(1,len(test_choice))

    def test_player_details(self):
        test_players_list = UserDetails().playerDetails()
        self.assertEqual(2,len(test_players_list))

    def test_player_icons(self):
        original_icons = ['!', '@', '#', '$', '%', '^', '&', '*', 'X', 'O']
        icons=UserDetails().playerIcons('sai',{},original_icons)
        self.assertEqual(9,len(icons))
