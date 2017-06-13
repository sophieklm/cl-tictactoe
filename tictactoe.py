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
    Player marker
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
        self.current_player = ''

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
        if self.instance[r][c] == '.':
            self.instance[r][c] = marker
        elif self.instance[r][c] != '.':
            self.rotate_player()

    def rotate_player(self):
        if self.current_player == self.player_o:
            self.current_player = self.player_x
        elif self.current_player == self.player_x:
            self.current_player = self.player_o

    def main(self):
        self.current_player = raw_input("Who goes first, x or o? : ")
        while self.check_win() != True:
            position = raw_input('Enter a position for player {}, e.g. 0,2: '.format(self.current_player)).split(",")
            position = map(lambda a: int(a), position)
            self.receive_input(position, self.current_player)
            self.print_board()
            self.rotate_player()

if __name__ == '__main__':
    game = TicTacToeGame()
    game.start()
    game.main()
