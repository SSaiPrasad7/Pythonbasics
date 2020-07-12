from Pythonbasics.TicTacToe.Screen import board, config


class GameRules:
    def gameConditions(self, player, players_list):
        '''
         Evaluates whether there is a winner or a tie
        '''
        if self.checkRows() or self.checkColumns() or self.checkDiagonals():
            print(f"{player} " + config["game"]["won"])
            board.clear()
            return True
        elif self.tieCondition(players_list):
            print(config["game"]["tie"])
            board.clear()
            return True
        else:
            return False

    def checkRows(self):
        '''
         Checks whether the player has three of their marks in a horizontal row
        '''
        for i in range(1, 8, 3):
            if board[i] == board[i + 1] == board[i + 2]:
                return True

    def checkColumns(self):
        '''
         Checks whether the player has three of their marks in a vertical row
        '''
        for i in range(1, 4, 1):
            if board[i] == board[i + 3] == board[i + 6]:
                return True

    def checkDiagonals(self):
        '''
         Checks whether the player has three of their marks in a diagonal row
        '''
        for i in range(1, 2):
            if board[i] == board[i + 4] == board[i + 8]:
                return True
        for j in range(3, 4):
            if board[j] == board[j + 2] == board[j + 4]:
                return True

    def tieCondition(self, players_list):
        '''
         Checks whether there is a tie
        '''
        player_icons = list(players_list.values())
        if board.count(player_icons[0]) == 5 and board.count(player_icons[1]) == 4:
            return True
        elif board.count(player_icons[0]) == 4 and board.count(player_icons[1]) == 5:
            return True
        else:
            return False
