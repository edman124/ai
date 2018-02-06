from Queue
import sys

a=list(sys.argv[1].lower())
print(a)
# a= ['a','b','c','d','e','f','g','h', '_', 'i','j','k','m','n','o','l']

def manhat2(a, goal):
	for i in range(len(a)

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

def moves(a):
    t = a.index('_')
    tmp = []
    if t//4 > 0: tmp.append(t-4)
    if t%4 > 0: tmp.append(t-1)
    if t//4 < 3: tmp.append(t+4)
    if t%4 < 3: tmp.append(t+1)
    return tmp