import sys, time
board = list("...........................ox......xo...........................")
direction = (-8,8,-1,1,-7,-9,9,7)
empty, played = {*range(64)}, {"x":set(),"o":set()}
playedMove=0
turn = "x"
if len(sys.argv) == 2:
    playedMove=int(sys.argv[1])
elif len(sys.argv) == 3:
    if len(sys.argv[1])>60:
        board = list(sys.argv[1].lower())
        if sum([1 for i in range(len(board)) if board[i] == "."])&1:
            turn = "o"
        else:
            turn = "x"
    else:
        turn=sys.argv[1]
    playedMove=sys.argv[2]
elif len(sys.argv) > 3:
    board = list(sys.argv[1].lower())
    turn = sys.argv[2].lower()
    playedMove=sys.argv[3]
for i in played:
    for j in range(64):
        if board[j] == i:
            played[i].add(j)
            empty -= {j}
board[playedMove]=turn
empty -={playedMove}
played[turn].add(playedMove)
def nextTurn(turn):
    if turn == "x": return "o"
    return "x"
def formatPrint(board):
    for i in range(8):
        print(board[i*8:i*8+8])
def valid(ind, nextInd):
	if nextInd<0 or nextInd>63:
		return False
	if abs(ind%8-(nextInd%8))>1:
		return False
	return True
def sameAdj(ind,turn,direct):
    ret=[]
    while ind in played[turn]:
        print(ind)
        ret.append(ind)
        if valid(ind,ind+direct):
            ind += direct
        else: break
    if board[ind] == nextTurn(turn):
        print("in")
        return ret
    return ""
def possAdj(ind, turn):
    ret = []
    for i in direction:
        if ind + i in played[nextTurn(turn)]:
            ret.append((ind+i,i))
    return ret
def stonesTurned(ind, turn):
    ret = []
    for i in possAdj(ind,turn):
        x=sameAdj(i[0], nextTurn(turn), i[1])
        print("debug same adj:"+str(x))
        if x:
            ret=ret+x
    return ret
def updateSets(ind,turn):
    enemy=nextTurn(turn)
    for i in stonesTurned(ind,turn):
        board[i]=turn
        played[turn].add(i)
        played[enemy].remove(i)
updateSets(playedMove,turn)
formatPrint(board)
print(''.join(board))
print(str(len(played['x']))+"/"+str(len(played['o'])))


