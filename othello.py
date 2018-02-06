import sys,time
board=sys.argv[1]
turn='o'
symbol=['o','x']
def legalMoves(board, turn): #8x8  0 or 1 as O X
	enemy=symbol[(symbol.index(turn)+1)%2]
	moves=set()
	for ind, val in enumerate(board):
		if val!=turn:
			continue
		print(checkAdj(board, turn, ind))
		for adjInd in checkAdj(board, turn, ind):
			x=checkLegal(board,turn,ind,adjInd)
			print(x)
			if x!=-1:
				moves.add(x)
	return moves
def checkLegal(board, turn, ind, ind2):
	enemy=symbol[(symbol.index(turn)+1)%2]
	change=ind2-ind
	# row=ind//8
	col=ind%8
	# rownew=ind2//8
	colnew=ind2%8
	while ind2<64 and ind>-1:
		if abs(col-colnew)>1: #check in board
			return -1
		if board[ind2]=='.':
			return ind2
		if board[ind2]==turn:
			return -1
		ind=ind2
		ind2+=change
		col=colnew
		colnew=ind2%8
	return -1
def checkAdj(board, turn, ind):
	enemy=0
	up=False
	down=False
	left=False
	right=False
	if turn==0:
		enemy=1
	ret=[]
	if ind//8 > 0 and board[ind-8]==enemy: 
		ret.append(ind-8)
		up=True
	if ind%8 > 0 and board[ind-1]==enemy: 
		ret.append(ind-1)
		left=True
	if ind//8 < 8 and board[ind+8]==enemy: 
		ret.append(ind+8)
		down=True
	if ind%8 < 8 and board[ind+1]==enemy: 
		ret.append(ind+1)
		right=True
	if up:
		if right:
			ret.append(ind-7)
		if left:
			ret.append(ind-9)
	if down:
		if right:
			ret.append(ind+9)
		if left:
			ret.append(ind+7)
	return ret
print(legalMoves(board,turn))