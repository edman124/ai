from collections import deque
import sys

a=list(sys.argv[1].lower())
print(a)
# a= ['a','b','c','d','e','f','g','h', '_', 'i','j','k','m','n','o','l']


def pprint(a):
	print(a[0:4])
	print(a[4:8])
	print(a[8:12])
	print(a[12:16])
	print()

def iCount(a):
	t=a.index('_')
	a1=a[0:t]+a[t+1::]
	print(a1)
	x= sum([1 for i in range(len(a1)-1) for g in range(i+1, len(a1)) if a1[i]>a1[g]])
	if (3-t//4)%2==x%2:
		return True
	return False

def bfs(a):
	if iCount(a):
	    dq = deque()
	    dq.appendleft((a, []))
	    v = set()
	    while True:
	    	# print("test")
	    	# if len(dq)==0:
	     #        print("impossible")
	     #        break
	    	tmp = dq.pop()
	    	# pprint(tmp[0])
	    	if tmp[0] == ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','_']:
	            print("Path:")
	            for i in tmp[1]: pprint(i)
	            print("Number of Steps: " + str(len(tmp[1])))
	            break
	    	can = tmp[1].copy()
	    	can.append(tmp[0])
	    	for i in moves(tmp[0]):
	            point = tmp[0].index('_')
	            tmp[0][point], tmp[0][i] = tmp[0][i], tmp[0][point]
	            if not tuple(tmp[0]) in v:
	                dq.appendleft((tmp[0].copy(), can))
	                v.add(tuple(tmp[0]))
	            tmp[0][point], tmp[0][i] = tmp[0][i], tmp[0][point]
	else:
		print("impossible")

def moves(a):
    t = a.index('_')
    tmp = []
    if t//4 > 0: tmp.append(t-4)
    if t%4 > 0: tmp.append(t-1)
    if t//4 < 3: tmp.append(t+4)
    if t%4 < 3: tmp.append(t+1)
    return tmp

bfs(a)