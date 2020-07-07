from Pythonbasics.TicTacToe.Screen import board, Screen


class UserPosition:
    def getPostion(self, player, player_icons):
        '''
         Getting the position from the user and validating the position
        '''
        while True:
            position = input(f"{player.capitalize()} enter the position between 1 to 9: ")
            try:
                if position.isdigit() == False or position in player_icons or position not in board:
                    raise ValueError
            except ValueError:
                print("Sorry, but you did not choose a value between 1 and 9 or Position may be filled.Try again")
                continue
            else:
                break
        return int(position)

    def set_position_1(self, players_list):
        '''
        Place the position on the board entered by Player1
        '''
        players = list(players_list.keys())
        players_icons = list(players_list.values())

        # Invoking getPosition function to get the position for player1

        player1_position = self.getPostion(players[0], players_icons)
        board[player1_position] = players_icons[0]
        Screen().outputDisplay()
        return players[0]

    def set_position_2(self, players_list):
        '''
        Place the position on the board entered by Player2
        '''
        players = list(players_list.keys())
        players_icons = list(players_list.values())

        # Invoking getPosition function to get the position for player2

        player2_position = self.getPostion(players[1], players_icons)
        board[player2_position] = players_icons[1]
        Screen().outputDisplay()
        return players[1]
