class Board:

    EMPTY = [None, None, None, None, None, None, None, None, None]
    WINNING_POSITIONS = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    def __init__(self):
        self.board = Board.EMPTY

    def move(self, player, position):
        self.board[position] = player.name.upper()

    def reset(self):
        self.board = Board.EMPTY

    def is_winner(self, t):
        v1 = self.board[t[0]]
        v2 = self.board[t[1]]
        v3 = self.board[t[2]]

        if v1 == v2 and v2 == v3 and v1 is not None:
            return True

        return False

    def has_winner(self):
        for index in range(8):
            positions = Board.WINNING_POSITIONS[index]
            if self.is_winner(positions):
                return index
        return None

    def get_winner(self, index):
        winning_tuple = Board.WINNING_POSITIONS[index]
        return self.board[winning_tuple[0]]

    def empty_positions(self):
        positions = []
        for index in range(9):
            if self.board[index] is None:
                positions.append(index)
        return positions

    def state(self):

        board_state = ''

        for index in range(9):
            state = self.board[index]
            if state is None:
                board_state += '0'
            elif self == 'X':
                board_state += '1'
            else:
                board_state += '2'

        return board_state

    def show(self):

        board = []

        for item in self.board:
            board.append( item ) if item else board.append(' ')

        return " {0} | {1} | {2} \n" \
               "===|===|===\n" \
               " {3} | {4} | {5} \n" \
               "===|===|===\n" \
               " {6} | {7} | {8} \n".format(*board)
