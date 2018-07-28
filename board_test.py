from board import Board

import unittest


class BoardTest(unittest.TestCase):

    def test_winner_x(self):
        board_state = ['x', 'x', 'x', None, None, None, None, None, None]
        b = Board()
        b.board = board_state
        self.assertTrue( b.check_winner() )


if __name__ == '__main__':
    unittest.main()
