import sys

col = {'a': 0,'b': 1,'c': 2,'d': 3,'e': 4,'f': 5,'g': 6,'h': 7}
def main():
    board = sys.argv[1].lower()
    turn = sys.argv[2]  
    possmoves = findMoves(board,turn)
    # board = updateBoard(board,possmoves,-1)
    formatPrint(board)
    print(possmoves[0])
    # print("Moves taken: "+ ''.join(str(moves)))

def nextTurn(turn):
    if turn =='x':
        return 'o'
    return 'x'

def curTurn(board):
    return ['x','o'][len([1 for x in range(64) if board[x] == '.']) %2]


def printStats(board):
    tempboard = ''
    for i in board:
        if i in {'+','*'}:
            tempboard += '.'
        else:
            tempboard += i
    print('\n'+tempboard+ ' ', end='')
    print(board.count('x'),end = '' + '/')
    print(board.count('o'))

def formatPrint(board):
    print('\n'.join([''.join(board[n * 8:n * 8 + 8]) for n in range(8)]))

def findMoves(board, turn):
    neigh = []
    for x in range(len(board)):
        if board[x] == turn:
            mySet = findAdj(board, x)
            neigh.append(mySet)
    return neigh

def valid(board,ind,turn):
    lis = [-7,-8,-9,-1,1,7,8,9]
    changemove = []
    if ind//8 ==0 or ind//8==1:
        lis = [i for i in lis if i > 0 or i == -1]
    if ind%8 ==7 or ind%8==6:
        lis = [i for i in lis if i not in {-7,1,9}]
    if ind%8 ==0 or ind%8==1:
        lis = [i for i in lis if i not in {-9,-1,7}]
    if ind//8 ==7 or ind//8==6:
        lis = [i for i in lis if i < 0 or i == 1]
    for i in lis:
        temp = []
        line = (ind)//8
        if board[ind + i] in {turn,'.','*'}:
            continue
        else:
            count =1
            aa = True
            asdf = True
            while asdf and aa:
                if ind+i*count < 0 or ind + i*count > 63 or(line != (ind+i*count)//8 and i in (-1,1)):
                    aa = False
                    continue
                elif board[ind+i*count] in {'.','*'}:
                    aa = False
                    continue
                elif board[ind+i*count] == turn:
                    asdf = False
                    continue
                else:
                    temp.append(ind+i*count)
                    count+=1
        if not asdf:
            changemove.append(temp)
    for i in changemove:
        for x in i:
            board = ''.join(board[:x] + turn + board[x + 1:])
    board = board.replace('*','.')
    board = board.replace('+', turn)
    return board

def findAdj(board, ind):
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
    return possValues

def ifInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
def updateBoard(board, possmoves,ind):
    for i in possmoves:
        for x in i:
            if x == ind:
                board = ''.join(board[:x] + '+' + board[x + 1:])
            else:
                board = ''.join(board[:x]+'*'+board[x+1:])
    return board
main()