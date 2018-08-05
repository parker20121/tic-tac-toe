from board import Board

import unittest


class BoardTest(unittest.TestCase):

    def test_winner_x(self):
        board_state = ['x', 'x', 'x', None, None, None, None, None, None]
        b = Board()
        b.board = board_state
        self.assertNotEqual( -1, b.has_winner() )

    def test_move(self):
        b = Board()
        b.move("X", 0)
        b.move("X", 1)
        b.move("X", 2)
        self.assertNotEqual( -1, b.has_winner() )

    def test_empty_positons(self):
        b = Board()
        b.move("X", 0)
        b.move("O", 1)
        b.move("X", 4)
        # print b.empty_positions()
        self.assertEqual( 6, len(b.empty_positions()) )

    def test_has_no_wineer(self):
        b = Board()
        self.assertEqual( -1, b.has_winner() )


if __name__ == '__main__':
    unittest.main()
