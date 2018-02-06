import sys
def main():
	board = "...........................ox......xo..........................."
	try:
		print("in")
		board = sys.argv[1].lower()
		turn = curTurn(board)
		levels=1
		if len(sys.argv) > 2:
			turn = sys.argv[2].lower()
		if len(sys.argv) >3:
			levels=int(sys.argv[3])
		nm = negamax(board, turn, levels)
		print ("At level {}, nm gives {}".format(levels, nm))
		print ("and I pick {}".format(nm[-1]))
	except IndexError:
		print("error")
def nextTurn(turn):
	if turn == "x": return "o"
	return "x"
def curTurn(board):
    return ['x','o'][len([1 for x in range(64) if board[x] == '.']) %2]
def negamax(board, turn, levels):

	if not levels: return [heur(board, turn)]

	lm = findMoves(board, turn)
	enemy=nextTurn(turn)
	if not lm: best = negamax(board, enemy, levels-1) + [-1]
	else: best = sorted([negamax(makeMove(board, turn, mv), enemy, levels-1) + [mv] for mv in lm])[0]
	return [-best[0]] + best[1:] 
def makeMove(board, turn, mv):
	return board[:mv]+turn+board[mv+1:]
def heur(board,turn):
	enemy=nextTurn(turn)
	us=0
	them=0
	for i in board:
		if i ==turn:
			us+=1
		elif i==enemy:
			them+=1
	return them-us
def findMoves(board, turn):
	neigh = set()
	for x in range(len(board)):
		if board[x] == turn:
			mySet = findNeigh(board, x)
			if mySet:
				for i in mySet:
					neigh.add(i)
	# print(neigh)
	# print(neigh[0][0])
	return neigh
def findNeigh(board, ind):
	row = ind // 8
	col = ind % 8
	mySet = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
	if col == 0 or col == 1:
		mySet = [i for i in mySet if i[1] != -1]
	if row == 0 or row == 1:
		mySet = [i for i in mySet if i[0] != -1]
	if col == 7 or col == 6:
		mySet = [i for i in mySet if i[1] != 1]
	if row == 7 or row == 6:
		mySet = [i for i in mySet if i[0] != 1]
	possValues = []
	for i in range(len(mySet)):
		z = mySet[i]
		newrow = row
		newcol = col
		changed = False
		while True:
			newrow += z[0]
			newcol += z[1]
			if newrow < 0 or newrow > 7 or newcol < 0 or newcol > 7:
				mySet[i] = ""
				break
			if board[newrow * 8 + newcol] == board[ind]:
				mySet[i] = ""
				break
			if board[newrow * 8 + newcol] == '.' and not changed:
				mySet[i] = ""
				break
			if board[newrow * 8 + newcol] == '.' and changed:
				possValues.append(newrow * 8 + newcol)
				break
			else:
				changed = True
	# if possValues:
	return possValues

main()
