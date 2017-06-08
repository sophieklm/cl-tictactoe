class TicTacToeBoard():
    """
    TicTacToe board
    """
    def __init__(self):
        self.board = self.__create_board()

    def __create_board(self):
        board = []

        for row in range(3):
            board.append([])
            for column in range(3):
                board[row].append('.')

        return board

class TicTacToePlayer(object):
    """
    Player instance
    """
    def __init__(self, marker):
        self.player = self.__create_player(marker)

    def __create_player(self, marker):
        return marker


class TicTacToeGame():
    """
    Game stores state of board and checks if complete
    """
    def __init__(self):
        self.start_instance = TicTacToeBoard().board
        self.player_x = TicTacToePlayer('x').player
        self.player_o = TicTacToePlayer('o').player

    def start(self):
        self.game_over = False
        self.instance = []
        for i in xrange(3):
            self.instance.append([])
            for j in xrange(3):
                self.instance[i].append(self.start_instance[i][j])

    def input_marker(self, row, column, input_type):
        self.instance[row][column] = input_type

    def print_board(self):
        for row in self.instance:
            print(" ".join(row))

    def check_win(self):
        for row in xrange(3):
            if self.check_row(row):
                return True
        for column in xrange(3):
            if self.check_column(column):
                return True
        for row in xrange(3):
            for column in xrange(3):
                if self.check_diag1(row, column):
                    return True
        for row in xrange(3):
            for column in xrange(3):
                if self.check_diag2(row, column):
                    return True
        self.game_over = True
        return False

    def __check_block(self, block):
        return set(block) == set(["x","x","x"]) or set(block) == set(["o","o","o"])

    def check_row(self, row):
        return self.__check_block(self.instance[row])

    def check_column(self, column):
        return self.__check_block(
            [self.instance[row][column] for row in xrange(3)]
        )

    def check_diag1(self, row, column):
        return self.__check_block(
            [
                self.instance[i][i]
                for i in xrange(len(self.instance))
            ]
        )

    def check_diag2(self, row, column):
        return self.__check_block(
            [
                self.instance[i][len(self.instance)-1-i]
                for i in xrange(len(self.instance))
            ]
        )

    def receive_input(self, position, marker):
        r, c = position
        self.instance[r][c] = marker

    def main(self):
        while self.check_win() != True:
            position = raw_input("Enter a position for player x, e.g. 0,2: ").split(",")
            position = map(lambda a: int(a), position)
            self.receive_input(position, self.player_x)
            self.print_board()
            position = raw_input("Enter a position for player o, e.g. 0,2: ").split(",")
            position = map(lambda a: int(a), position)
            self.receive_input(position, self.player_o)
            self.print_board()

if __name__ == '__main__':
    game = TicTacToeGame()
    game.start()
    game.main()
