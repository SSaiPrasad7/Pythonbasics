from Pythonbasics.TicTacToe.Screen import board, Screen


class UserPosition:
    def getPostion(self, player_icons):
        position = "sai"
        in_range = False
        while position.isdigit() == False or in_range == False:
            position = input("Enter the position between 1 to 9 ")
            if position.isdigit() == False:
                print("Sorry, but you did not enter an integer. Try again.")
            elif position not in board:
                print("Sorry, but you did not choose a value between 1 and 9.")
            else:
                in_range = True
                return int(position)

    def setPosition_1(self, players_list):
        players = list(players_list.keys())
        player_icons = list(players_list.values())
        print(f'{players[0]}')
        player1_position = self.getPostion(player_icons)
        board[player1_position] = player_icons[0]
        Screen().outputDislay()
        return players[0]

    def setPosition_2(self, players_list):
        players = list(players_list.keys())
        player_icons = list(players_list.values())
        print(f'{players[1]}')
        player2_position = self.getPostion(player_icons)
        board[player2_position] = player_icons[1]
        Screen().outputDislay()
        return players[1]
