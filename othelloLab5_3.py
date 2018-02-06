import sys
corners = {0,7,63,55}
def main():
    board = "...........................ox......xo..........................."
    try:
        board = sys.argv[1].lower()
        turn = curTurn(board)
        if len(sys.argv) > 2:
            turn = sys.argv[2].lower()
        a = findMoves(board, turn)[0]
        print(a)
    except IndexError:
        findMoves(board,'x')
        # board = changeBoard(board, possmoves)
        # printb(board)
def curTurn(board):
    return ['x','o'][len([1 for x in range(64) if board[x] == '.']) %2]


def findMoves(board, turn):
    neigh = []
    for x in range(len(board)):
        if board[x] == turn:
            mySet = findNeigh(board, x)
            if mySet:
                for i in mySet:
                    neigh.append(i)
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