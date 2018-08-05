from player import Player


class RLPlayer(Player):

    def __init__(self, name):
        Player.__init__(self, name)
        self.move_history = []
        self.memory = dict()

    def reset(self):
        self.move_history = []

    def learn(self, reward):
        return

    def next_move(self, board, open_positions):
        state = board.state()

        if state in self.memory:

        else:
            memory[ state ] = []

        return 0

