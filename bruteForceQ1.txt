import sys, collections, Queue, time
lookuphex = [
set(1,2,3,7,8,9),
set(3,4,5,9,10,11),
set(6,7,8,13,14,15),
set(10,11,12,17,18,19),
set(14,15,16,20,21,22),
set(16,17,18,22,23,24),
set(8,9,10,15,16,17)
]
middlehex = [8,9,10,15,16,17]
pzl=[]
c=1
for i in range(24)
	if i+1 in middlehex:
		pzl.append(c)
		c+=1
	pzl.append('.')
def bruteForce(pzl):
	if not isValid:
		return ""
	if isSolved:
		return pzl
	unfilled=pzl.index('.')
	for i in rang(6):
		pzl[unfilled]=i
		bf = bruteForce(pzl)
		if bf!="":
			return pzl
		pzl[unfilled]='.'
	return ""
def isSolved(pzl):
	if isValid:
		if '.' not in pzl:
			return True
	return False
def isValid(pzl):
	for hex in lookuphex:
		mem=set('.')
		for ind in hex:
			if pzl[ind-1] not in mem:
				return False
			mem.add(pzl[ind-1])
	return True
print(bruteForce(pzl))