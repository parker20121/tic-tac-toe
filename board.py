

class Board:

	def __init__(self):
		self.board = []
		
	def move( self, player, position ):
		self.board[position] = player
		
	def reset(self):
		self.board = []
		
	def has_winner(self, p1, p2, p3):
		v1 = self.board[p1]
		v2 = self.board[p2]
		v3 = self.board[p3]
		
		if v1 == v2 and v2 == v3 and v1 != '':
			return True
			
		return false
		