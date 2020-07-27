from Pythonbasics.TicTacToe.Helper import Helper

# Read the English.json in to say config attribute
config = Helper().readConfig("config1.json")

board = []


class Screen():
    def boardIntialize(self):
        original_board = config["board"]["originalBoard"]
        board.extend(original_board)

    def outputDisplay(self):
        '''
        This function prints out the board.
        "board" is a list of 10 strings representing the board (ignore index 0)
        '''
        print(config["board"]["display"])
        for i in range(1, 10, 3):
            print(config["board"]["line"])
            print("|", board[i], "|", board[i + 1], "|", board[i + 2], "|")

        print(config["board"]["line"])
        return True
