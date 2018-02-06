import sys
corners = {0,7,63,56}
edges = {0:[[1,2,3,4,5,6],[8,16,24,32,40,48]],7:[[6,5,4,3,2,1],[15,23,31,39,47,55]],56:[[57,58,59,60,61,62],[48,40,32,24,16,8]],63:[[62,61,60,59,58,57],[55,47,39,31,23,15]]}
danger = {0:{1,8,9}, 7:{6,14,15}, 63:{62,53,54}, 56:{56,47,48}}
def main():
    board = "...........................ox......xo..........................."
    try:
        board = sys.argv[1].lower()
        turn = curTurn(board)
        if len(sys.argv) > 2:
            turn = sys.argv[2].lower()
        a = findMoves(board, turn)
        print(goodMove(board,a, turn))
    except IndexError:
        findMoves(board,'x')
        # board = changeBoard(board, possmoves)
        # printb(board)
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
# def safeEdges(board, turn):
#     if board[0]==turn:



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