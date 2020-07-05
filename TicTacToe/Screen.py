board = []


class Screen:
    def outputDislay(self):
        '''
        This function prints out the board.
        "board" is a list of 10 strings representing the board (ignore index 0)
        '''
        print("This is the current board postion:")
        print("-------------")
        print("|", board[7], "|", board[8], "|", board[9], "|")
        print("-------------")
        print("|", board[4], "|", board[5], "|", board[6], "|")
        print("-------------")
        print("|", board[1], "|", board[2], "|", board[3], "|")
        print("-------------")
