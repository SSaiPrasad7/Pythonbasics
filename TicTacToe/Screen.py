board = []


class Screen:
    def boardIntialize(self):
        original_board = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        board.extend(original_board)


    def outputDisplay(self):
        '''
        This function prints out the board.
        "board" is a list of 10 strings representing the board (ignore index 0)
        '''
        print("This is the current board position:")
        for i in range(1,10,3):
            print("-------------")
            print("|", board[i], "|", board[i+1], "|", board[i+2], "|")
        print("-------------")
        return True

