from Pythonbasics.TicTacToe.Screen import board


class GameRules:
    def winCondition(self, player, players_list):
        if self.checkRows() or self.checkColumns() or self.checkDiagonals():
            print(f"Congratulations!!{player} won the game.")
            board.clear()
            return True
        elif self.tieCondition(players_list):
            print("Game tied")
            board.clear()
            return True
        else:
            return False

    def checkRows(self):
        for i in range(1, 8, 3):
            if board[i] == board[i + 1] == board[i + 2]:
                return True

    def checkColumns(self):
        for i in range(1, 4, 1):
            if board[i] == board[i + 3] == board[i + 6]:
                return True

    def checkDiagonals(self):
        for i in range(1, 2):
            if board[i] == board[i + 4] == board[i + 8]:
                return True
        for j in range(3, 4):
            if board[j] == board[j + 2] == board[j + 4]:
                return True

    def tieCondition(self, players_list):
        player_icons = list(players_list.values())
        if board.count(player_icons[0]) == 5 and board.count(player_icons[1]) == 4:
            return True
        elif board.count(player_icons[0]) == 4 and board.count(player_icons[1]) == 5:
            return True
        else:
            return False
