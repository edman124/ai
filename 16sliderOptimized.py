import sys, collections, Queue, time

puzzle = sys.argv[1].upper()
lookUpChildren = [
    [1,4],
    [0,2,5],
    [1,3,6],
    [2,7],
    [0,5,8],
    [1,4,6,9],
    [2,5,7,10],
    [3,6,11],
    [4,9,12],
    [5,8,10,13],
    [6,9,11,14],
    [7,10,15],
    [8,13],
    [9,12,14],
    [10,13,15],
    [11,14]
]
lookUpManhattan = {
    "1":[0,0],
    "2":[0,1],
    "3": [0,2],
    "4": [0,3],
    "5": [1,0],
    "6": [1,1],
    "7": [1,2],
    "8": [1,3],
    "9": [2,0],
    "A": [2,1],
    "B": [2,2],
    "C": [2,3],
    "D": [3,0],
    "E": [3,1],
    "F": [3,2],
    "_": [3,3]
}
def swapChar(string, ind1, ind2):
    maxI = max(ind1,ind2)
    minI = min(ind1,ind2)
    return string[0:minI] + string[maxI] + string[minI+1:maxI] + string[minI] + string[maxI+1:]
def getChildren(puz):
    spaceInd = puz.index("_")
    return [swapChar(puz,spaceInd,k) for k in lookUpChildren[spaceInd]]
def parityPuzzle(puz):
    puz = puz.replace("_","")
    return (sum([1 for i in range(len(puz)-1) for j in range(i+1,len(puz)) if int(puz[i],16) > int(puz[j],16)]))&1
def parityRow(puz):
    return (3-puz.index("_")//4)&1
def heur(puz):
    h = 0
    for i in range(len(puz)):
        rowdif = abs(lookUpManhattan[puz[i]][0]-i//4)
        coldif = abs(lookUpManhattan[puz[i]][1]-i%4)
        h += (rowdif+coldif)
    return h
def constructDict(puz):
    if(parityRow(puz)==parityPuzzle(puz)):
        path = {puz:None}
        parseMe = Queue.PriorityQueue()
        checked = set([puz])
        tmp = [puz,0]
        QueueCount = 0
        while not tmp[0] == "123456789ABCDEF_":
            countFrom = tmp[1]
            for child in getChildren(tmp[0]):
                if child not in checked:
                    path[child] = tmp[0]
                    checked.add(child)
                    parseMe.put((countFrom+1+heur(child),[child,countFrom+1]))
            tmp = parseMe.get()[1]
            QueueCount += 1
        return [path,QueueCount]
    else:
        return 0
def pprint(puz):
    return puz[0:4]+"\n"+puz[4:8]+"\n"+puz[8:12]+"\n"+puz[12:16]+"\n\n"
def astar(puz):
    count = 0
    dict = constructDict(puz)
    QueueCount = dict[1]
    if dict[0]:
        tmp = "123456789ABCDEF_"
        toret = pprint(tmp)
        while not dict[0][tmp] == None:
            count += 1
            toret = pprint(dict[0][tmp]) + toret
            tmp = dict[0][tmp]
    else:
        toret = "impossible"
    return [toret,count,QueueCount]
def solveiDA(puz):
    keys = []
    values = []
    dict={
        keys:values
    }
start = time.clock()
solu = solve(puzzle)
print("path:")
print(solu[0])
print("steps: %i" % solu[1])
print("states removed: %i" % solu[2])
end = time.clock()
print("time: %f" % (end-start))