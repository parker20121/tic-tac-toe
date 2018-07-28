class BoardState:

    BASE3 = [1.0, 3.0, 9.0, 27.0, 81.0, 243.0, 729.0, 2187.0]

    @staticmethod
    def calc(board):
        total = 0

        for index in range(0, 8):
            position = board[index]

            if position is None:
                value = 0
            elif position == 'x':
                value = 1
            else:
                value = 2

            total += (BoardState.BASE3[index] * value)

        return total

    @staticmethod
    def board(state):
        return []