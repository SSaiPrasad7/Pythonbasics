import unittest

from Pythonbasics.TicTacToe.Screen import Screen, board


class ScreenTest(unittest.TestCase):
    def test_board_initialize(self):
        Screen().boardIntialize()
        self.assertEqual(10,len(board))
    def test_output_display(self):
        Screen().boardIntialize()
        self.assertEqual(True,Screen().outputDisplay())
