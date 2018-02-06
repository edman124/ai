from collections import deque
import sys
r=list(sys.argv[1])
a=list()
v = set()
for num in r:
	a.append(int(num))

def convert(a):
    j = 0
    for i in range(len(a)): j += a[i] * 10 ** i
    return j
def heur(a):
	ans = 0
	for i in range(len(a)):
		if not a[i] == (i+1) % 9: ans += 1
	return ans

def pprint(a):
    if len(str(a)) == 8: print(str(a)[::-1] + "0")
    else: print(str(a)[::-1])
def bfs(a):
    dq = deque()
    dq.appendleft((a, []))
    while dq:
        tmp = dq.pop()
        if convert(tmp[0]) == 876543210:
            print("Path:")
            for i in tmp[1]: pprint(i)
            print(str(convert(tmp[0]))[::-1] + "0")
            print("Number of Steps: " + str(len(tmp[1])))
            break
        can = tmp[1].copy()
        can.append(convert(tmp[0]))
        for i in moves(tmp[0]):
            gg = tmp[0].index(0)
            tmp[0][gg], tmp[0][i] = tmp[0][i], tmp[0][gg]
            if not convert(tmp[0]) in v:
                dq.appendleft((tmp[0].copy(), can))
                v.add(convert(tmp[0]))
            tmp[0][gg], tmp[0][i] = tmp[0][i], tmp[0][gg]
   

def moves(a):
    t = a.index(0)
    tmp = []
    if t//3 > 0: tmp.append(t-3)
    if t%3 > 0: tmp.append(t-1)
    if t//3 < 2: tmp.append(t+3)
    if t%3 < 2: tmp.append(t+1)
    return tmp

bfs(a)
