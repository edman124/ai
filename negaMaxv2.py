import sys
corners = {0,7,63,56}
edges = {0:[[1,2,3,4,5,6],[8,16,24,32,40,48]],7:[[6,5,4,3,2,1],[15,23,31,39,47,55]],56:[[57,58,59,60,61,62],[48,40,32,24,16,8]],63:[[62,61,60,59,58,57],[55,47,39,31,23,15]]}
danger = {0:{1,8,9}, 7:{6,14,15}, 63:{62,53,54}, 56:{56,47,48}}
class Strategy():
    def bestStrategy(self,board,player,best.move, still_running):
        brd = ''.join(board).replace('?', '').replace('@','X')
        token = "X" if player == '@' else 'o'
        a = findMoves(brd, token)
        mv= goodMove(brd, a, token)
        mv1 = 1 + (mv // c8) *10 + (mv % c8)
        best.move.value = mv1
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
		empty=board.count('.')
		if empty<9:
			nm = negamax(board, turn, levels)
			print ("At level {}, nm gives {}".format(levels, nm))
			print ("and I pick {}".format(nm[-1]))
		else:
			a = findMoves(board, turn)
        	print(goodMove(board,a, turn))
	except IndexError:
		print("error")
def nextTurn(turn):
	if turn == "x": return "o"
	return "x"
def curTurn(board):
    return ['x','o'][len([1 for x in range(64) if board[x] == '.']) %2]
def goodMove(board,possMoves, turn):
    copy=possMoves
    for i in possMoves:
        if i in corners:
            return i
    for i in corners:
        if board[i]!=turn:
            possMoves=possMoves-danger[i]
    if possMoves:
        return possMoves.pop()
    return copy.pop()
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
if __name__=="__main__":
	main()
