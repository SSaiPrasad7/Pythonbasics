from Pythonbasics.TicTacToe.GameRules import GameRules
from Pythonbasics.TicTacToe.Screen import board, Screen
from Pythonbasics.TicTacToe.UserDetails import UserDetails
import unittest


class GameRulesTest(unittest.TestCase):
    def test_game_conditions(self):
        Screen().boardIntialize()
        player_list = UserDetails().playerDetails()
        board[1] = board[9] = board[6]
        test_value = GameRules().gameConditions(player="sai", players_list=player_list)
        self.assertEqual(False, test_value)

    def test_check_rows(self):
        Screen().boardIntialize()
        board[4] = board[5] = board[6]
        test_value_1 = GameRules().checkRows()
        self.assertEqual(True, test_value_1)

    def test_check_columns(self):
        Screen().boardIntialize()
        board[3] = board[6] = board[9]
        test_value_2 = GameRules().checkColumns()
        self.assertEqual(True, test_value_2)

    def test_check_diagonals(self):
        Screen().boardIntialize()
        board[1] = board[5] = board[9]
        test_value_3 = GameRules().checkDiagonals()
        self.assertEqual(True, test_value_3)
        board[3] = board[5] = board[7]
        test_value_4 = GameRules().checkDiagonals()
        self.assertEqual(True, test_value_4)

    def test_check_tie_condition(self):
        Screen().boardIntialize()
        players_list = UserDetails().playerDetails()
        player_icons = list(players_list.values())
        board[1:6] = [player_icons[0] if board[i] == '2' else player_icons[1] for i in range(1, 6)]
        board[6:10] = [player_icons[1] if board[i] == '8' else player_icons[0] for i in range(6, 10)]
        test_value_5 = GameRules().tieCondition(players_list)
        self.assertEqual(True, test_value_5)
