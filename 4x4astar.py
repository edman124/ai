from collections import deque
import sys
from heapq import heappush, heappop

a=list(sys.argv[1].lower())
# a= ['a','b','c','d','e','f','g','h', '_', 'i','j','k','m','n','o','l']

def heur(a, n):
	ind=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','_']
	ret = 0
	for i in range(len(a)):
		ret+=abs(i%4-(ind.index(a[i]))%4)+abs(i//4-(ind.index(a[i]))//4)
	return ret/2 + n

def astar(a):
	print('run')
	if iCount(a):
		print("running")
		astr=''.join(a)
		pq = []
		heappush(pq, (heur(a, 0), a))
		v = set()
		lencount=0;
		step={''.join(a):0}
		while True:
			# if len(dq)==0:
		 #		print("impossible")
		 #		break
			tmp = heappop(pq)
			# print(tmp)
			# pprint(tmp[0])
			if tmp[1] == ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','_']:
				print("working")
				pat=ppprint(''.join(tmp[1]),step)
				print("Path:")
				for i in range(len(pat)-1,-1,-1):
					pprint(pat[i])
				print("Number of Steps: " + lencount)
				break
			for i in moves(tmp[1]):
				point = tmp[1].index('_')
				tmp[1][point], tmp[1][i] = tmp[1][i], tmp[1][point]
				tmpstr=''.join(tmp[1])
				if not tmpstr in step or astr:
					lencount+=1					
					lag = tmp[1][:]
					heappush(pq, (heur(lag, lencount), lag))
					step[''.join(lag)]=tmpstr
				tmp[1][point], tmp[1][i] = tmp[1][i], tmp[1][point]
		else:
			print("impossible")

def ppprint(a, dic):
	ret=[]
	while a in dic:
		ret.append(a)
		a=dic[a]
	return ret


def pprint(a):
	print(a[0:4])
	print(a[4:8])
	print(a[8:12])
	print(a[12:16])
	print()

def iCount(a):
	t=a.index('_')
	a1=a[0:t]+a[t+1::]
	x= sum([1 for i in range(len(a1)-1) for g in range(i+1, len(a1)) if a1[i]>a1[g]])
	if (3-t//4)%2==x%2:
		return True
	return False

def moves(a):
	t = a.index('_')
	tmp = []
	if t//4 > 0: tmp.append(t-4)
	if t%4 > 0: tmp.append(t-1)
	if t//4 < 3: tmp.append(t+4)
	if t%4 < 3: tmp.append(t+1)
	return tmp

astar(a)