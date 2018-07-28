from board import Board


class StateManager(dict):

    NO_TRANSITION = -1

    def add_state(self, board):
        state = self.calc_state(board)
        transition = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
        count = 0

        if not self.has_key(state):
            for index, item in board:
                if item != Board.EMPTY:
                    transition[index] = 0
                else:
                    count += 1

            if count > 0:
                equal_probability = 1.0/count

                for index, item in transition:
                    if item == 0:
                        transition[index] = equal_probability

            self[state] = transition

