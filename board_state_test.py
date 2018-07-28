from board import Board
from board_state import BoardState

import unittest


class BoardStateTest(unittest.TestCase):

    def test_no_state(self):
        state = BoardState.calc( Board.EMPTY )
        self.assertEqual(0, state, "Board state not zero: {0}".format(state))

    def test_no_state(self):
        board = ['x', None, None, None, None, None, None, None, None]
        state = BoardState.calc( board )
        self.assertEqual(0, state, "Board state not zero: {0}".format(state))



if __name__ == '__main__':
    unittest.main()
