import sys, time
from collections import deque
lookupmoves = [
[(0,3,1),(0,5,2)],
[(1,6,3),(1,8,4)],
[(2,7,4),(2,9,5)],
[(3,0,1),(3,5,4),(12,7),(10,6)],
[(4,11,7),(4,13,8)],
[(5,0,2),(5,3,4),(5,12,8),(5,14,9)],
[(6,1,3),(6,8,7)],
[(7,2,4),(7,9,8)],
[(8,1,4),(8,6,7)],
[(9,2,5),(9,7,8)],
[(10,3,6),(10,12,11)],
[(11,4,7),(11,13,12)],
[(12,3,7),(12,5,8),(12,10,11),(12,14,13)],
[(13,4,8),(13,11,12)],
[(14,5,9),(14,12,13)]
] #(space index, peg to move, postion to check)
space=sys.argv[1]
puzzle=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
puzzle[int(space)]='_'
def convert(a):
    ret=''
    for val in a:
        ret+=val
    return ret
def moves(a): #take in array
    ind=[]
    for i in range(15):
        if a[i]=='_':
            ind.append(i)
    tmp = []
    for index in ind:
        for item in lookupmoves[index]:
            tmp.append(item)
    print(tmp)
    return tmp
def swapChar(a, start, dest, remove): #a is array
    print("inswap")
    tmp=a
    tmp[start],tmp[dest]=tmp[dest],tmp[start]
    tmp[remove]='_'
    print(a)
    return a
def getChildren(a):
    children=[]
    for move in moves(a):
        print("inchild:"+str(move))
        if a[move[2]]!='_':
            children.append(swapChar(a,move[0],move[1],move[2]))
    return children
def isgoal(a):
    count=0
    for num in a:
        if num=='_':
            count+=1
    if count ==14:
        return True
    return False
def constructDict(a):
    print("inconstr")
    parseMe=deque()
    parseMe.appendleft(a)
    path = {convert(a):None}
    checked = set(convert(a))
    print("stillinconstr")
    while len(parseMe)!=0:
        tmp = parseMe.pop()
        if isgoal(tmp):
            print("printing")
            print(path[convert(tmp)])
            return (path, convert(tmp))
        for child in getChildren(tmp):
            if convert(child) not in checked:
                path[convert(child)] = convert(tmp)
                print(path)
                checked.add(convert(child))
                parseMe.appendleft(child)

def pprint(a):
    return a[0]+"\n"+a[1:3]+"\n"+a[3:6]+"\n"+a[6:10]+"\n"+a[10:15]+"\n\n"
def bfs(a):
    print("inbfs")
    constr= constructDict(a)
    dic=constr[0]
    tmp=constr[1]
    if dic:
        toret = pprint(tmp)
        while not dic[tmp] == None:
            # print(tmp)
            toret = pprint(dic[0][tmp]) + toret
            tmp = dic[tmp]
    else:
        toret = "impossible"
    return toret

# start = time.clock()
solu = bfs(puzzle)

print(solu)

