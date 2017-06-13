import unittest
from tictactoe import TicTacToeGame, TicTacToeBoard

class TicTacToe_Tests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.game = TicTacToeGame()
        self.game.start()

    def test_board_creation(self):
        self.assertEquals(self.game.instance,[['.','.','.'],['.','.','.'],['.','.','.']])

    def test_current_player(self):
        self.assertEquals(self.game.current_player, '')

    def test_check_win(self):
        self.assertFalse(self.game.check_win())

if __name__ == '__main__':
    unittest.main()
