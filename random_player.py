from player import Player

import random


class RandomPlayer(Player):

    def __init__(self, name):
        Player.__init__(self, name)

    def next_move(self, board, open_positions):
        return random.choice( open_positions )