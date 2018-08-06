from player import Player

import random


class RLPlayer(Player):

    LEARNING_RATE = 0.1
    NO_ACTIONS = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    UNIFORM_ACTIONS = [1.0/9.0] * 9

    def __init__(self, name):
        Player.__init__(self, name)
        self.move_history = []
        self.memory = dict()

    def reset(self):
        self.move_history = []

    def learn(self, reward):

        for (state, next_move) in self.move_history:

        return

    def next_move(self, board, open_positions):
        state = board.state()
        actions = []

        if state in self.memory:
            actions = self.memory[ state ]
        else:
            actions = RLPlayer.NO_ACTIONS
            number_moves = len(open_positions)

            if number_moves > 0:
                for index in open_positions:
                    actions[index] = 1.0/number_moves

                self.memory[ state ] = actions
            else:
                self.memory[ state ] = RLPlayer.UNIFORM_ACTIONS

        next_move = random.choice( open_positions )
        self.move_history.append( (state, next_move) )

        return next_move

