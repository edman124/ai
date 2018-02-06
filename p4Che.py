import sys, time
board = "...........................ox......xo..........................."
direction = (-8,8,-1,1,-7,-9,9,7)
turn = "x"
if len(sys.argv) == 2:
    board = sys.argv[1].lower()
    if sum([1 for i in range(len(board)) if board[i] == "."])&1:
        turn = "o"
    else:
        turn = "x"
else:
    board = sys.argv[1].lower()
    turn = sys.argv[2].lower()
empty, played = {*range(64)}, {"x":set(),"o":set()}
for i in played:
    for j in range(64):
        if board[j] == i:
            played[i].add(j)
            empty -= {j}
def nextTurn(turn):
    if turn == "x": return "o"
    return "x"
def formatPrint(board):
    for i in range(8):
        print(board[i*8:i*8+8])
def sameAdj(ind,turn,direct):
    while ind in played[turn]:
        if valid(ind,ind+7):
            ind += direct
        else: break
    if ind in empty:
        return ind
    return ""
def valid(ind, nextInd):
    if nextInd<0 or nextInd>63:
        return False
    if abs(ind%8-(nextInd%8))>1:
        return False
    return True
def possAdj(ind, turn):
    ret = []
    for i in direction:
        if ind + i in played[nextTurn(turn)]:
            ret.append((ind+i,i))
    return ret
def pMoves(turn):
    ret = []
    for i in played[turn]:
        for j in possAdj(i,turn):
            x=sameAdj(j[0],nextTurn(turn),j[1])
            if x:
                ret.append(x)
    return ret

formatPrint(board)
print(pMoves(turn))