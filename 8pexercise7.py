from collections import deque
import random
import time
# s=sys.argv[1]
# a=[]
# ind=s.index('_')
# for i in range(ind):
#     a.append(int(s[i]))
# a.append(0)
# for i in range(ind+1,9):
#     a.append(int(s[i]))

def convert(a):
    j = 0
    for i in range(len(a)):
        j += a[i] * 10 ** i
    return j

def ppprint(a):
    if len(str(a)) == 8: 
        return(str(a)[::-1] + "0")
    else: 
        return(str(a)[::-1])
def pprint(a):
    a=ppprint(a)
    n=a.index('0')
    if n<3:
        print(a[0:n], end='')
        print('_', end='')
        print(a[n+1:3])
        print(a[3:6])
        print(a[6:9]) 
    elif n<6:
        print(a[0:3])
        print(a[3:n], end='')
        print('_', end='')
        print(a[n+1:6])
        print(a[6:9])
    else:
        print(a[0:3])
        print(a[3:6])
        print(a[6:n], end='')
        print('_', end='')
        print(a[n+1:9])
    print()

def bfs(a):
    t=time.time()
    v = set()
    dq = deque()
    dq.appendleft((a, []))
    while True:
        if(len(dq)==0):
            return (time.time()-t,0,0,True)
            break
        tmp = dq.pop()
        if convert(tmp[0]) == 87654321:
            return (time.time()-t,len(tmp[1]), 1, False)
            break
        can = tmp[1].copy()
        can.append(convert(tmp[0]))
        for i in moves(tmp[0]):
            point = tmp[0].index(0)
            tmp[0][point], tmp[0][i] = tmp[0][i], tmp[0][point]
            if not convert(tmp[0]) in v:
                dq.appendleft((tmp[0].copy(), can))
                v.add(convert(tmp[0]))
            tmp[0][point], tmp[0][i] = tmp[0][i], tmp[0][point]
   
def rand():
    total=0
    stp=0
    tot=0
    imp=0
    impcount=0

    for i in range(1000):
        a=[]
        l=[0, 1, 2, 3, 4, 5, 6, 7, 8]
        for x in range(8,-1,-1):
            a.append(l.pop(int(random.randint(0,x))))
        tup = bfs(a)
        total+= tup[0]
        stp+=tup[1]
        tot+=tup[2]
        if tup[3]:
            imp+=tup[0]
            impcount+=1
    print("steps: "+str(stp/tot)) 
    print("avg time: "+str(total/1000))
    print("avg impossible time: "+ str(imp/impcount))

def moves(a):
    t = a.index(0)
    tmp = []
    if t//3 > 0: tmp.append(t-3)
    if t%3 > 0: tmp.append(t-1)
    if t//3 < 2: tmp.append(t+3)
    if t%3 < 2: tmp.append(t+1)
    return tmp

rand() 
