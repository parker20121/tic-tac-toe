from board import Board
from player import Player

import unittest


class BoardTest(unittest.TestCase):

    def test_winner_x(self):
        board_state = ['X', 'X', 'X', None, None, None, None, None, None]
        b = Board()
        b.board = board_state
        self.assertIsNotNone( b.has_winner() )

    def test_move(self):
        b = Board()
        p = Player('X')
        b.move(p, 0)
        b.move(p, 1)
        b.move(p, 2)
        self.assertNotEqual( -1, b.has_winner() )

    def test_empty_positons(self):
        b = Board()
        x = Player("X")
        o = Player("O")
        b.move(x, 0)
        b.move(o, 1)
        b.move(x, 4)
        # print b.empty_positions()
        self.assertEqual( 6, len(b.empty_positions()) )

    def test_has_no_wineer(self):
        b = Board()
        self.assertIsNone( b.has_winner() )

    def test_board_state(self):
        board_state = ['X', 'X', 'X', None, 'O', None, None, 'O', None]
        b = Board()
        b.board = board_state
        self.assertEqual('111020020', b.state(), "Board state not equal: {0}".format( b.state() ))


if __name__ == '__main__':
    unittest.main()
