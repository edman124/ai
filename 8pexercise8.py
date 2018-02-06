import sys

from collections import deque


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
            break
        tmp = dq.pop()
        if len(tmp[1]) == n:
            print(tmp[0])
            break
            #print(str(convert(tmp[0]))[::-1] + "0")
            # pprint('087654321')
            # print("Number of Steps: " + str(len(tmp[1])))
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


def moves(a):
    t = a.index(0)
    tmp = []
    if t//3 > 0: tmp.append(t-3)
    if t%3 > 0: tmp.append(t-1)
    if t//3 < 2: tmp.append(t+3)
    if t%3 < 2: tmp.append(t+1)
    return tmp

def create():
	ab=[1,2,3,4,5,6,7,8,0]
	for i in range(1,32,2):
		bfsCount(ab, i)
		print(i)
	print("set size: 16")
create()


