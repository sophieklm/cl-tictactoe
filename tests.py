import unittest
from tictactoe import TicTacToeGame, TicTacToeBoard

class TicTacToe_Tests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.game = TicTacToeGame()
        self.game.start()

    def test_board_creation(self):
        self.assertEqual(self.game.instance,[['.','.','.'],['.','.','.'],['.','.','.']])

    def test_current_player(self):
        self.assertEqual(self.game.current_player, '')

    def test_check_win(self):
        self.assertFalse(self.game.check_win())

    def test_receive_input(self):
        self.game.receive_input([0,0],'x')
        self.assertEqual(self.game.instance,[['x','.','.'],['.','.','.'],['.','.','.']])

    def test_rotate_player(self):
        self.game.current_player = 'x'
        self.game.rotate_player()
        self.assertEqual(self.game.current_player, 'o')

    def test_overwrite_impossible(self):
        self.game.current_player = 'x'
        self.game.receive_input([0,0],'x')
        self.game.rotate_player()
        self.game.receive_input([0,0],'o')
        self.assertEqual(self.game.instance,[['x','.','.'],['.','.','.'],['.','.','.']])

if __name__ == '__main__':
    unittest.main()
