import sys
import copy

def checkRight(row,col,board,color):
	figures = ""
	if color == "white": figures = "qr" 
	else: figures = "QR"
	if col < 8:
		if board[row][col] == "#":
			return checkRight(row,col+1,board,color)
		if board[row][col] in figures:
			return True
	return False
def checkLeft(row,col,board,color):
	figures = ""
	if color == "white": figures = "qr"
	else: figures = "QR"
	if col > -1:
		if board[row][col] == "#":
			return checkLeft(row,col-1,board,color)
		if board[row][col] in figures:
			return True
	return False
def checkDown(row,col,board,color):
	figures = ""
	if color == "white": figures = "qr"
	else: figures = "QR"
	if row < 8:
		if board[row][col] == "#":
			return checkDown(row+1,col,board,color)
		if board[row][col] in figures:
			return True
	return False
def checkUp(row,col,board,color):
	figures = ""
	if color == "white": figures = "qr"
	else: figures = "QR"
	if row > -1:
		if board[row][col] == "#":
			return checkUp(row-1,col,board,color)
		if board[row][col] in figures:
			return True
	return False

def checkDownRight(row,col,board,color):
	figures = ""
	if color == "white": figures = "qb"
	else: figures = "QB"
	if row == 7 or col == 7:
		if board[row][col] in figures:
			return True
	else:
		if board[row][col] == "#":
			return checkDownRight(row+1,col+1,board,color)
		if board[row][col] in figures:
			return True
	return False
def checkDownLeft(row,col,board,color):
	figures = ""
	if color == "white": figures = "qb"
	else: figures = "QB"
	if row == 7 or col == 0:
		if board[row][col] in figures:
			return True
	else:
		if board[row][col] == "#":
			return checkDownLeft(row+1,col-1,board,color)
		if board[row][col] in figures:
			return True
	return False
def checkUpRight(row,col,board,color):
	figures = ""
	if color == "white": figures = "qb"
	else: figures = "QB"
	if row == 0 or col == 7:
		if board[row][col] in figures:
			return True
	else:
		if board[row][col] == "#":
			return checkUpRight(row-1,col+1,board,color)
		if board[row][col] in figures:
			return True
	return False
def checkUpLeft(row,col,board,color):
	figures = ""
	if color == "white": figures = "qb"
	else: figures = "QB"
	if row == 0 or col == 0:
		if board[row][col] in figures:
			return True
	else:
		if board[row][col] == "#":
			return checkUpLeft(row-1,col-1,board,color)
		if board[row][col] in figures:
			return True
	return False
def checkPawn(row,col,board,color):
	figures = ""
	if color == "white": figures,pawn = "n","p"
	else: figures,pawn = "N","P"
	if row+1 <= 7 and col - 1 >= 0:
		if board[row+1][col-1] == pawn:
			return True
	if row+1 <= 7 and col + 1 <= 7:
		if board[row+1][col+1] == pawn:
			return True	
	return False
def checkKnight(row,col,board,color):
	figures = ""
	if color == "white": figures,pawn = "n","p"
	else: figures,pawn = "N","P"
	if row-2 >= 0 and col-1 >= 0 and board[row-2][col-1] == figures:
		return True
	if row-1 >= 0 and col-2 >= 0 and board[row-1][col-2] == figures:
		return True
	if row-1 >= 0 and col+2 <= 7 and board[row-1][col+2] == figures:
		return True
	if row-2 >= 0 and col+1 <= 7 and board[row-2][col+1] == figures:
		return True
	if row+1 <= 7 and col+2 <= 7 and board[row+1][col+2] == figures:
		return True
	if row+2 <= 7 and col+1 <= 7 and board[row+2][col+1] == figures:
		return True
	if row+1 <= 7 and col-2 >= 0 and board[row+1][col-2] == figures:
		return True
	if row+2 <= 7 and col-1 >= 0 and board[row+2][col-1] == figures:
		return True
	return False

def check(king,board,color):
	if king[1]+1 <=7:
		if checkRight(king[0],king[1]+1,board,color): return True
	if king[1]-1 >= 0:
		if checkLeft(king[0],king[1]-1,board,color): return True
	if king[0]-1 >= 0:
		if checkUp(king[0]-1,king[1],board,color): return True
	if king[0]+1 <= 7:
		if checkDown(king[0]+1,king[1],board,color): return True
	if king[0]-1 >= 0 and king[1]-1 >= 0:
		if checkUpLeft(king[0]-1,king[1]-1,board,color): return True
	if king[0]-1 >= 0 and king[1]+1 <= 7:
		if checkUpRight(king[0]-1,king[1]+1,board,color): return True
	if king[0]+1<=7 and king[1]-1 >= 0:
		if checkDownLeft(king[0]+1,king[1]-1,board,color): return True
	if king[0]+1 <= 7 and king[1]+1 <= 7:
		if checkDownRight(king[0]+1,king[1]+1,board,color): return True
	if checkPawn(king[0],king[1],board,color): return True
	if checkKnight(king[0],king[1],board,color): return True
	return False
def waysToGiveACheck(board):
	pawns = []
	king = (0,0)
	me = (0,0)
	for i in range(8):
		if board[1][i] == "P":
			pawns.append((1,i))
	for i in range(8):
		for j in range(8):
			if board[i][j] == "k":
				king = (i,j)
			elif board[i][j] == "K":
				me = (i,j)
	sol = 0
	for pawn in pawns:
		temp_board = copy.deepcopy(board)
		if temp_board[0][pawn[1]] == "#":
			temp_board[0][pawn[1]] = "P"
			temp_board[1][pawn[1]] = "#"
			if not check(me,temp_board,"white"):
				if check(king,temp_board,"black"): sol = max(sol,4)
				temp_board[0][pawn[1]] = "Q"
				if check(king,temp_board,"black"): sol = max(sol,2)
				temp_board[0][pawn[1]] = "N"
				if check(king,temp_board,"black"): sol = max(sol,1)
			else:
				if check(king,board,"black"): sol = max(sol,4)

	if len(pawns) == 0:
		if check(king,board,"black"): sol = max(sol,4)		
			
	return sol
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        board = []
        for board_i in range(8):
           board_t = list(input().strip().split(' ')[0])
           board.append(board_t)
        result = waysToGiveACheck(board)
        print(result)