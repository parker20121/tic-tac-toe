class Player:

    def __init__(self, name):
        self.name = name
        self.games_won = 0
        self.games_lost = 0
        self.games_tied = 0
        self.moves = []

    def won_game(self):
        self.games_won += 1

    def lost_game(self):
        self.games_lost += 1

    def tied_game(self):
        self.games_tied += 1

    def stats(self):
        print "player: {0} won: {1} lost: {2} tied: {3}\n".format(self.name, self.games_won, self.games_lost, self.games_tied)

    def reset(self):
        self.moves = []

	def next_move(self, board):
        return -1

    def learn(self):
        return
