from collections import deque
import sys
# s=sys.argv[1]
# a=[]
# ind=s.index('_')
# for i in range(ind):
#     a.append(int(s[i]))
# a.append(0)
# for i in range(ind+1,9):
#     a.append(int(s[i]))

# sys.stdout = open('8pData.txt','wt')

a=[1,2,3,4,5,6,7,8,0]
num=31

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

def bfsMax(a):
    v = set()
    dq = deque()
    dq.appendleft((a, []))
    while True:
        # if(len(dq)==0):
        #     print("impossible")
        #     break
        tmp = dq.pop()
        
        can = tmp[1].copy()
        can.append(convert(tmp[0]))
        for i in moves(tmp[0]):
            point = tmp[0].index(0)
            tmp[0][point], tmp[0][i] = tmp[0][i], tmp[0][point]
            if not convert(tmp[0]) in v:
                dq.appendleft((tmp[0].copy(), can))
                v.add(convert(tmp[0]))
            tmp[0][point], tmp[0][i] = tmp[0][i], tmp[0][point]

        if len(dq)==0:
                return (len(tmp[1]), tmp[0])
                break


def bfsCount(a, n):
    v = set()
    dq = deque()
    dq.appendleft((a, []))
    c=0;
    while True:
        # if(len(dq)==0):
        #     print("impossible")
        #     break
        if len(dq)==0:
            print("none")
            return False
        tmp = dq.pop()
        if len(tmp[1]) == n and checkic(tmp[0],a):
            print(tmp[0])   
            #print(str(convert(tmp[0]))[::-1] + "0")
            # pprint('087654321')
            print("Number of Steps: " + str(len(tmp[1])))
            return True
        else:
            can = tmp[1].copy()
            can.append(convert(tmp[0]))
            for i in moves(tmp[0]):
                point = tmp[0].index(0)
                tmp[0][point], tmp[0][i] = tmp[0][i], tmp[0][point]
                if not convert(tmp[0]) in v:
                    dq.appendleft((tmp[0].copy(), can))
                    v.add(convert(tmp[0]))
                tmp[0][point], tmp[0][i] = tmp[0][i], tmp[0][point]
   
def bfs(a):
    v = set()
    dq = deque()
    dq.appendleft((a, []))
    while True:
        if(len(dq)==0):
            print("impossible")
            break
        tmp = dq.pop()
        if convert(tmp[0]) == 87654321:
            print("Path:")
            for i in tmp[1]: pprint(i)
            #print(str(convert(tmp[0]))[::-1] + "0")
            pprint('087654321')
            print("Number of Steps: " + str(len(tmp[1])))
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
   
def bfsAll(max, a):
    for i in range(1,max+1):
        print(str(bfsCount(a,i)))

def check(a, b):
    boo=True
    for i in range(9):
        if b[i]==a[i]:
            boo=False
    return boo

def checkic(a, b):
    t=a.index(0)
    t1=b.index(0)
    a1=a[0:t]+a[t+1::]
    b1=b[0:t1]+b[t1+1::]

    x= sum([1 for i in range(len(a1)-1) for g in range(i+1, len(a1)) if b1.index(a1[i])>b1.index(a1[g])])
    if x<5:
        return True
    return False
    
def moves(a):
    t = a.index(0)
    tmp = []
    if t//3 > 0: tmp.append(t-3)
    if t%3 > 0: tmp.append(t-1)
    if t//3 < 2: tmp.append(t+3)
    if t%3 < 2: tmp.append(t+1)
    return tmp
def run(a, num):
    for i in range(num,0,-1):
        x=bfsCount(a,i)
        if x:
            break

# print(bfsMax(ab))
# print("9!/2")


# tup = bfsMax(ab)
# bfsAll(tup[0], ab)


run(a,num)

# print(tup[0]) 
# print(bfs(tup[1]))
# puz=bfsMax(a)[1]
# m=bfsMax(a)[0]
# print(m)
# b=[]
# for i in range(9):
#     b.append(int(puz[i]))
# bfs(b)
# bfsAll(m)



