#gameboard

class GameBoard:
	def __init__(self):
		self._board = [[0 for _ in range(7)] for _ in range(6)]
		self.PLAYER1 = 1
		self.PLAYER2 = 2

	def __str__(self):
		b_str = ""
		for row in self._board:
			b_str += "\n+---+---+---+---+---+---+---+"
			line = "\n"
			for item in row:

				if item == 1:
					symbol = "1"
				elif item == 2:
					symbol = "2"
				else:
					symbol = "-"

				line += "| " + symbol + " " 

			line += "|"
			b_str += line

		b_str += "\n+===+===+===+===+===+===+===+"
		b_str += "\n| 0 | 1 | 2 | 3 | 4 | 5 | 6 |"
		b_str += "\n+---+---+---+---+---+---+---+"

		return b_str

	def get_valid_moves(self):
		valid = set()
		for column in range(0,7):
			for row in range(0,6):
				if self._board[row][column] == 0:
					valid.add(column)
				else:
					break

		return valid


	def move(self, move, player):
		if player != self.PLAYER1 and player != self.PLAYER2:
			raise ValueError
		else:
			if move in self.get_valid_moves():
				for row in reversed(self._board):
					if row[move] == 0:
						row[move] = player
						break 
			else:
				raise ValueError
	def iswinner(self, player):
		


board = GameBoard()
print(board)
board.move(5, 1)
print(board)

