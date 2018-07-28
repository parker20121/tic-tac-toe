from board import Board
from player import Player


class Game:

    def __init__(self):
        self.x = Player('x')
        self.o = Player('o')
        self.states = []
        self.moves = []
        self.games_played = 0
        self.games_total = 1000

    def play(self):

        board = Board()

        while self.games_played < self.games_total:
            self.x.reset()
            self.o.reset()
            board.reset()

            current_player = self.x

            while not board.has_winner():

                if current_player == self.x:
                    current_player = self.o
                else:
                    current_player = self.x

            self.games_played += 1


