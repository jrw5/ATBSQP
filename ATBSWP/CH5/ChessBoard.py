#Joel Wheatley
#1/14/20





##
colors = ['b', 'w']
pieces = ['king', 'queen', 'bishop', 'rook', 'knight', 'pawn']
boardState = {'1h':'bking', '6c':'wqueen', '2g':'bbishop', '5h':'bqueen', '3e':'wking'}

def mkBoard():
	letters = ['a', 'b', 'c','d','e','f','g']
	numbers = range(8)
	board = []
	for i in letters:
		for j in numbers:
			board.append(i+str(j))
	return board


def countPiece(piece, color, boardstate):

	return False

def isBoardValid(boardstate):

	return True

def onBoard(piece, board):
	return True

board = mkBoard()

isBoardValid(boardState)

