import sys, collections, queue, time

puzzle = sys.argv[1].upper()

def moves(a):
    t = a.index('_')
    tmp = []
    if t//4 > 0: tmp.append(t-4)
    if t%4 > 0: tmp.append(t-1)
    if t//4 < 3: tmp.append(t+4)
    if t%4 < 3: tmp.append(t+1)
    return tmp
def swapChar(string, ind1, ind2):
    maxI = max(ind1,ind2)
    minI = min(ind1,ind2)
    return string[0:minI] + string[maxI] + string[minI+1:maxI] + string[minI] + string[maxI+1:]
def getChildren(puz):
    spaceInd = puz.index('_')
    return [swapChar(puz,spaceInd,k) for k in moves(puz)]
# def parityPuzzle(puz):
#     puz = puz.replace("_","")
#     return (sum([1 for i in range(len(puz)-1) for j in range(i+1,len(puz)) if int(puz[i],16) > int(puz[j],16)]))&1
# def parityRow(puz):
#     return (3-puz.index("_")//4)&1
def iCount(puz):
    t=puz.index('_')
    a1=puz[0:t]+puz[t+1::]
    x= sum([1 for i in range(len(a1)-1) for g in range(i+1, len(a1)) if a1[i]>a1[g]])
    if (3-t//4)%2==x%2:
        return True
    return False

def heur(puz):
    ind='123456789ABCDEF_'
    ret = 0
    for i in range(len(puz)):
        if puz[i]!='_':
            ret+=abs(i&3-(ind.index(puz[i]))&3)+abs((i>>2)-((ind.index(puz[i]))>>2))
    return ret
def constructDict(puz):
    if(iCount(puz)):
        path = {puz:None}
        parseMe = queue.PriorityQueue()  #openset
        # memset123 = {}
        checked = set()    #closedset
        parseMe.put((0,0, puz))
        queueCount = 0
        # while 

        while True:
            tmp=parseMe.get()
            countFrom = tmp[1]
            if tmp[2] == "123456789ABCDEF_":
                break
            
            checked.add(tmp[2])
            for child in getChildren(tmp[2]):
                if(child not in checked):
                    # print("In loop")
                    # print(tmp[2], child)
                    h=-(countFrom)+1+heur(child)
                    path[child] = tmp[2]
                    parseMe.put((h,countFrom-1,child))
                    # memset123[child]=h
            queueCount += 1
        print("returning")
        return [path,queueCount]
    else:
        return 0
def pprint(puz):
    return puz[0:4]+"\n"+puz[4:8]+"\n"+puz[8:12]+"\n"+puz[12:16]+"\n\n"
def astar(puz):
    count = 0
    dic = constructDict(puz)
    queueCount = dic[1]
    if dic[0]:
        tmp = "123456789ABCDEF_"
        toret = pprint(tmp)
        while not dic[0][tmp] == None:
            # print(tmp)
            count += 1
            toret = pprint(dic[0][tmp]) + toret
            tmp = dic[0][tmp]
    else:
        toret = "impossible"
    return [toret,count,queueCount]
start = time.clock()
solu = astar(puzzle)

print("path:")
print(solu[0])
print("steps: %i" % solu[1])
print("states removed: %i" % solu[2])
end = time.clock()
print("time: %f" % (end-start))